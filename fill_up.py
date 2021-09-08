import time
import random
import apa

from point_region import PointRegion
from strand import Strand

# Strand Start: Where in the LED strip is the first LED
SS = 0 

NUMBER_OF_LEDS = 186

STEP_TIME = 0.0
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

base_color = random.choice([DARK])

SPIN_MID_SPD = [ 
            ((76,16,43,73,13,46), base_color),
            ((77,17,42,72,12,47), base_color),
            ((78,18,41,71,11,48), base_color),
            ((79,19,40,70,10,49), base_color),
            ((80,20,39,69,9,50), base_color),
            ((81,21,38,68,8,51), base_color),
            ((82,22,37,67,7,52), base_color),
            ((83,23,36,66,6,53), base_color),
            ((84,24,35,65,5,54), base_color),
            ((85,25,34,64,4,55), base_color),
            ((86,26,33,63,3,56), base_color),
            ((87,27,32,62,2,57), base_color),
            ((88,28,31,61,1,58), base_color),
            ((89,29,30,60,0,59), base_color),
        ]

SPIN_BOT_SPD = [ 
            ((140, 100, 171, 129, 109, 161), base_color),
            ((141, 99,  172, 128, 110, 160), base_color),
            ((142, 98, 173, 127, 111, 159), base_color),
            ((143, 97, 174, 126, 112, 158), base_color),
            ((144, 96, 175, 125, 113, 157), base_color),
            ((145, 95, 176, 124, 114, 156), base_color),
            ((146, 94, 177, 123, 115, 155), base_color),
            ((147, 93, 178, 122, 116, 154), base_color),
            ((148, 92, 179, 121, 117, 153), base_color),
            
            ]
            
ALL_SPD = SPIN_MID_SPD + SPIN_BOT_SPD
      
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
spin_branch_regions = []
    
try:
    # Create a Strand with all LEDs 
    led_strand = Strand(NUMBER_OF_LEDS)
    
    # Create a region with all LEDs that is DARK, ie all LEDs are off.
    # Use this to turn all LEDs off as needed.
    region_dark = led_strand.add_region(10, 
                                        "region10", 
                                        range(0,NUMBER_OF_LEDS), 
                                        DARK)
                                        
    star_region = led_strand.add_point_region(0, 
                                             "region0", 
                                             STAR_SPD[POINTS], 
                                             STAR_SPD[COLOR])

    led_strand.set_region(star_region)

    add_strand_regions(ALL_SPD, spin_branch_regions, 400)                                        

    for spin_region in spin_branch_regions:
        an_led = spin_region.get_led_num(0)
        an_led.r = 64
        an_led.g = 64
        an_led.b = 64
        an_led = spin_region.get_led_num(1)
        an_led.r = 64
        an_led.g = 0
        an_led.b = 0
        an_led = spin_region.get_led_num(2)
        an_led.r = 0
        an_led.g = 64
        an_led.b = 0
        an_led = spin_region.get_led_num(3)
        an_led.r = 0
        an_led.g = 0
        an_led.b = 64
        an_led = spin_region.get_led_num(4)
        an_led.r = 0
        an_led.g = 64
        an_led.b = 64
        an_led = spin_region.get_led_num(5)
        an_led.r = 64
        an_led.g = 0
        an_led.b = 64

    while True:

        for spin_region in spin_branch_regions:
            for idx in range(1):
                led_strand.set_region(spin_region)
                led_strand.write_leds()
                #spin_region.rotate("cw")    
                time.sleep(STEP_TIME)
            spin_region.rotate("cw")    
            	
                
        
        
			
finally:
    # After a keyboard interrupt or anything else that shuts things down,
    # turn off the LED strand
    print("BYE!")
    led_strand.ledstrip.reset_leds()
