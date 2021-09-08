import time
import random
import apa

from point_region import PointRegion
from strand import Strand

# Strand Start: Where in the LED strip is the first LED
SS = 0 

NUMBER_OF_LEDS = 186

STEP_TIME = 0.08
PAUSE_TIME = 1.5

# Color definitions: RGB tuples
DARK    = (0,1,0)
WHITE   = (32,32,32)
RED     = (32,0,0)
GREEN   = (0,32,0)
BLUE    = (0,0,32)
DARK_GREEN = (0,20,0)
DARK_BLUE = (0,0,10)
DARK_RED = (10,0,0)
YELLOW = (255,255,0)
LIGHT_YELLOW = (10,10,0)
PURPLE = (32,0,32)
DARK_PURPLE = (10,0,32)
BLUE_GREEN = (0,10,10)

# Strand point definitions
# Each is a tuple containing a tuple of LED numbers and a color for the tuple
STAR_SPD = ((14,15,44,45,74,75), YELLOW)

base_color = random.choice([RED,GREEN,BLUE])
if base_color == RED:
    dark_color = (1,0,0)
elif base_color == GREEN:
    dark_color = (0,1,0)
else:
    dark_color = (0,0,1)

TOP_SPD = [ ((13,16,43,46,73,76), base_color),
            ((12,17,42,47,72,77), base_color),
            ((11,18,41,48,71,78), base_color),
            ((10,19,40,49,70,79), base_color),
            (( 9,20,39,50,69,80), base_color),
            (( 8,21,38,51,68,81), base_color),
            (( 7,22,37,52,67,82), base_color),
        ]
        
MID_SPD = [ (( 6,23,36,53,66,83), dark_color),
            (( 5,24,35,54,65,84), base_color),
            (( 4,25,34,55,64,85), base_color),
            (( 3,26,33,56,63,86), base_color),
            (( 2,27,32,57,62,87), base_color),
            (( 1,28,31,58,61,88), base_color),
            (( 0,29,30,59,60,89), base_color),
      ]

BOT_SPD = [ ((100,109,129,139,162,171), base_color),
            ((99 ,110,128,140,161,172), base_color),
            ((98 ,111,127,141,159,173), base_color),
            ((97 ,112,126,142,158,174), base_color),
            ((96 ,113,125,143,157,175), base_color),
            ((95 ,114,124,144,156,176), base_color),
            ((94 ,115,123,145,155,177), base_color),
            ((93 ,116,122,146,154,178), base_color),
            ((92 ,117,121,147,153,179), WHITE),
            ((91 ,118,120,148,152,180), WHITE),
            ]

      
# Constants used to index the tuples stored as Strand Range Definitions.
POINTS = 0
COLOR = 1

# We will dynamically build list of regions from the Strand Range Definitions
top_branch_regions = []
mid_branch_regions = []
bot_branch_regions = []
    
try:
    # Create a Strand with all LEDs 
    led_strand = Strand(NUMBER_OF_LEDS)
    
    # Create a region with all LEDs that is DARK, ie all LEDs are off.
    # Use this to turn all LEDs off as needed.
    region_dark = led_strand.add_region(10, 
                                        "region10", 
                                        range(0,NUMBER_OF_LEDS), 
                                        dark_color)
                                        
    star_region = led_strand.add_point_region(0, 
                                             "region0", 
                                             STAR_SPD[POINTS], 
                                             STAR_SPD[COLOR])


    # Build the lists of regions using the Strand Range Definitions                                         
    for region_num, strand_range_def in enumerate(TOP_SPD):
        top_branch_regions.append(led_strand.add_point_region(25+region_num, 
                                             "region"+str(25+region_num), 
                                             strand_range_def[POINTS], 
                                             strand_range_def[COLOR]))
                                             
    for region_num, strand_range_def in enumerate(MID_SPD):
        mid_branch_regions.append(led_strand.add_point_region(50+region_num, 
                                             "region"+str(50+region_num), 
                                             strand_range_def[POINTS], 
                                             strand_range_def[COLOR]))

    for region_num, strand_range_def in enumerate(BOT_SPD):
        bot_branch_regions.append(led_strand.add_point_region(75+region_num, 
                                             "region"+str(75+region_num), 
                                             strand_range_def[POINTS], 
                                             strand_range_def[COLOR]))
            
    while True:
        # Light the star at the top of the tree
        led_strand.set_region(star_region)
        led_strand.write_leds()
        time.sleep(STEP_TIME)	
        
        # Light the branches in a cascading fashion, one region at a time
        for idx in range(0,len(top_branch_regions)):
            led_strand.set_region(top_branch_regions[idx])    
            led_strand.set_region(mid_branch_regions[idx])    
            led_strand.set_region(bot_branch_regions[idx])    
            
            led_strand.write_leds()
            time.sleep(STEP_TIME)
            
        # The bottom branches are longer, so they have more LEDs to light.
        # Light them next.
        for idx in range(len(top_branch_regions),len(bot_branch_regions)):
            led_strand.set_region(bot_branch_regions[idx])    
            
            led_strand.write_leds()
            time.sleep(STEP_TIME)
            	
        time.sleep(PAUSE_TIME)
        led_strand.set_region(region_dark)    
        led_strand.write_leds()
        time.sleep(STEP_TIME)	
        
			
finally:
    # After a keyboard interrupt or anything else that shuts things down,
    # turn off the LED strand
    print("BYE!")
    led_strand.ledstrip.reset_leds()
