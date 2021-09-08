import time
import sys

import apa
import traceback

#from region import Region
from point_region import PointRegion
from strand import Strand

# Strand Start: Where in the LED strip is the first LED
SS = 0 

# Color definitions: RGB tuples
DARK    = (0,0,0)
WHITE   = (32,32,32)
RED     = (32,0,0)
GREEN   = (0,32,0)
BLUE    = (0,0,32)

TOTAL_NUM_LEDS = 150

try:
    # Create a Strand with all LEDs 
    led_strand = Strand(TOTAL_NUM_LEDS)
    
    # Create a region with all LEDs that is DARK, ie all LEDs are off.
    # Use this to turn all LEDs off as needed.
    region_dark = led_strand.add_region(10, 
                                        "region10", 
                                        range(0,TOTAL_NUM_LEDS), 
                                        DARK)
    led_number = 0
    points = ()
    last_led = led_strand.num_leds
    sleep_time = 0
    persist_range = False
    process_flag = True
    move_flag = True
    if len(sys.argv) > 1:
        if '--' in sys.argv[1]:
            print('\npython led_locate.py arg1 arg2')
            print('    arg1:')
            print('        nothing: Light LEDs all in sequence')
            print('        --help: Provide this help message')
            print('        -1: Turn off all LEDs')
            print('        n = an integer:  First led to light')
            print("        '1,2,3': light LEDs 1 2 3")
            print('    arg2:')
            print('        nothing: Loop timer of 1 second is used')
            print('        d = a decimal: Loop timer setting in seconds')
            print('        n = an integer: Last LED to light')
            print('        ''nomove'' = when arg1 is a tuple, do not move the last led')
            print('    When looping, ctrl-c breaks the loop')
            
            led_number = -1
        else: 
            if ',' in sys.argv[1]:    
                # we have a tuple of values
                points = eval('('+sys.argv[1]+')')
            else:   
                led_number = int(sys.argv[1])
            if led_number < 0:
                process_flag = False
    if len(sys.argv) > 2:
        if '.' in sys.argv[2]:
            sleep_time = float(sys.argv[2])
        elif sys.argv[2] == 'nomove':
            move_flag = False
        else:
            sleep_time = 0.0
            persist_range = True
            last_led = int(sys.argv[2])
    try:        
        if len(points) > 0:
            print('We have a tuple:', points)
            moving_point = points[len(points)-1]
            while True:
                print(moving_point)
                test_region = led_strand.add_point_region(0, 
                                             "region0", 
                                             points, 
                                             WHITE)
                test_region.set_led_num(len(points)-1, GREEN) #RED)
                led_strand.set_region(test_region)
                led_strand.write_leds()
                if not move_flag:
                    break
                # Modify the points to make a different region with the moving_point
                # incremented
                moving_point += 1
                if moving_point == last_led:
                    moving_point = 0
                lpoints = list(points[:-1])
                lpoints.append(moving_point)
                points = tuple(lpoints)
                time.sleep(0.9)            
                led_strand.set_region(region_dark)
                led_strand.write_leds()
            
        else:        
            while process_flag:
                print('LED number:', led_number)
                region_dark.set_led_num(led_number, WHITE)
                led_strand.set_region(region_dark)
        			    
                led_strand.write_leds()
                if not persist_range:
                    region_dark.set_led_num(led_number, DARK)
                led_number += 1
                if led_number >= last_led:
                    led_number = 0
                    break
                time.sleep(sleep_time)	
    except Exception as ex:
        print('Caught Exception: ',ex)
        traceback.print_exc()
        print('Stopping display...')
    			
finally:
    print('BYE!')
    # if -1 was passed as the first argument on cmd line,,
    # turn off the LED strand
    if not process_flag:
        led_strand.ledstrip.reset_leds()
