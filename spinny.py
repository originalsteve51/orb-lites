import time
import random
import apa

from point_region import PointRegion
from strand import Strand

# Strand Start: Where in the LED strip is the first LED
SS = 0 

NUMBER_OF_LEDS = 210

STEP_TIME = 0
PAUSE_TIME = 0.0

# Color definitions: RGB tuples
DARK    = (0,0,0)
WHITE   = (32,32,32)
RED     = (16,0,0)
GREEN   = (0,32,0)
BLUE    = (0,0,32)
DARK_GREEN = (0,20,0)
DARK_BLUE = (0,0,10)
DARK_RED = (10,0,0)
YELLOW = (25,25,0)
LIGHT_YELLOW = (10,10,0)
PURPLE = (32,0,32)
DARK_PURPLE = (10,0,32)
BLUE_GREEN = (0,10,10)

# Strand point definitions
# Each is a tuple containing a tuple of LED numbers and a color for the tuple
STAR_SPD = ((14,15,44,45,74,75), YELLOW)

base_color = random.choice([RED, BLUE])
if base_color == RED:
    dark_color = (1,0,0)
    spin_color = WHITE
elif base_color == GREEN:
    dark_color = (0,1,0)
    spin_color = WHITE
else:
    dark_color = (0,0,1)
    spin_color = WHITE

ORB_SPD = [
            ((30, 89, 90, 120, 59, 60, 119, 149), base_color),
            ((31, 88, 91, 121, 58, 61, 118, 148), base_color),
            ((32, 87, 92, 122, 57, 62, 117, 147), base_color),
            ((33, 86, 93, 123, 56, 63, 116, 146), base_color),
            ((34, 85, 94, 124, 55, 64, 115, 145), base_color),
            ((35, 84, 95, 125, 54, 65, 114, 144), base_color),
            ((36, 83, 96, 126, 53, 66, 113, 143), base_color),
            ((37, 82, 97, 127, 52, 67, 112, 142), base_color),
            ((38, 81, 98, 128, 51, 68, 111, 141), base_color),
            ((39, 80, 99, 129, 50, 69, 110, 140), base_color),
            ((40, 79, 100, 130, 49, 70, 109, 139), base_color),
            ((41, 78, 101, 131, 48, 71, 108, 138), base_color),
            ((42, 77, 102, 132, 47, 72, 107, 137), base_color),
            ((43, 76, 103, 133, 46, 73, 106, 136), base_color),
            ((44, 75, 104, 134, 45, 74, 105, 135), base_color),
          ]
          
BASE_SPD = [(range (150,180), DARK_RED),
            (range (180,210), DARK_BLUE),]
            
EQUATOR_SPD = [(range(0,30), DARK_BLUE)]
      
# Constants used to index the tuples stored as Strand Range Definitions.
POINTS = 0
COLOR = 1


def add_strand_regions(definitions, regions, base_number):                                        
    for region_num, strand_range_def in enumerate(definitions):
        regions.append(led_strand.add_point_region(base_number+region_num, 
                                             "region"+str(base_number+region_num), 
                                             strand_range_def[POINTS], 
                                             strand_range_def[COLOR]))



# We will dynamically build lists of regions from the Strand Point Definitions
spin_regions = []
base_regions = []
equator_regions = []
    
try:
    # Create a Strand with all LEDs 
    led_strand = Strand(NUMBER_OF_LEDS)
    
    # Create a region with all LEDs that is DARK, ie all LEDs are off.
    # Use this to turn all LEDs off as needed.
    region_dark = led_strand.add_region(10, 
                                        "region10", 
                                        range(0,NUMBER_OF_LEDS), 
                                        DARK)
                                        

    add_strand_regions(ORB_SPD, spin_regions, 750)                                        
    add_strand_regions(BASE_SPD, base_regions, 800)                                        
    add_strand_regions(EQUATOR_SPD, equator_regions, 850)                                        

    for spin_region in spin_regions:
        an_led = spin_region.get_led_num(0)
        an_led.set_color(spin_color)
        an_led = spin_region.get_led_num(4)
        an_led.set_color(spin_color)
    
    for base_region in base_regions:
        for led_num in range(0,30,5):
            # There is an offset in the way the base leds are wrapped. Handle
            # that here.
            if base_region.name == 'region801':
                led_num += 1
            an_led = base_region.get_led_num(led_num)
            an_led.r = 64
            an_led.g = 64
            an_led.b = 64
            
    for equator_region in equator_regions:
        for led_num in range(0,30,5):
            an_led = equator_region.get_led_num(led_num)
            an_led.r = 64
            an_led.g = 64
            an_led.b = 64

    spin_direction = random.choice(['cw', 'ccw'])
    spin_control = 0
    while True:
        spin_control += 1
        for spin_region in spin_regions:
            led_strand.set_region(spin_region)
            if spin_control % 3 == 0:
                spin_region.rotate(spin_direction)

        for base_region in base_regions:
            led_strand.set_region(base_region)
            if spin_control % 5 == 0:
                base_region.rotate(spin_direction)    
                
        for equator_region in equator_regions:
            led_strand.set_region(equator_region)
            equator_region.rotate(spin_direction)    

        led_strand.write_leds()
        time.sleep(STEP_TIME)	
    
        
			
finally:
    # After a keyboard interrupt or anything else that shuts things down,
    # turn off the LED strand
    print("BYE!")
    led_strand.ledstrip.reset_leds()
