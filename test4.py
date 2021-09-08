import time

import apa

from region import Region
from strand import Strand

# Strand Start: Where in the LED strip is the first LED
SS = 0 

NUMBER_OF_LEDS = 186

# Color definitions: RGB tuples
DARK    = (0,0,0)
WHITE   = (32,32,32)
RED     = (32,0,0)
GREEN   = (0,32,0)
BLUE    = (0,0,32)
DARK_GREEN = (0,10,0)
DARK_BLUE = (0,0,10)
DARK_RED = (10,0,0)
YELLOW = (255,255,0)
LIGHT_YELLOW = (10,10,0)
PURPLE = (32,0,32)
DARK_PURPLE = (10,0,32)
BLUE_GREEN = (0,10,10)

# Strand range definitions
# Each is a tuple containing a range of LEDs and a color for the range
SRD = [(range(SS,      SS+15),    GREEN),
      (range(SS+15,    SS+30),    DARK_GREEN),
      (range(SS+30,    SS+45),    GREEN),
      (range(SS+45,    SS+60),    DARK_GREEN),
      (range(SS+60,    SS+75),    GREEN),
      (range(SS+75,    SS+90),    DARK_GREEN),
      (range(SS+90,    SS+105),   GREEN),
      (range(SS+105,   SS+120),   DARK_GREEN),
      (range(SS+120,   SS+135),   GREEN),
      (range(SS+141,   SS+156),   DARK_GREEN),
      (range(SS+156,   SS+171),   GREEN),
      (range(SS+171,   SS+186),   DARK_GREEN),
      ]


SRD_PARTIAL = [(range(SS+101, SS+108), DARK), #upper trunk
               (range(SS+130, SS+139), DARK), #upper trunk
               (range(SS+162, SS+171), DARK), #upper trunk
               ]
               
SRD_FLICKER = [(range(SS+71, SS+78), RED), #top branch
               (range(SS+41, SS+48), RED), #top branch
               (range(SS+11, SS+18), RED), #top branch
               
               (range(SS+2, SS+5), RED),   #middle branch side 1
               (range(SS+25, SS+28), RED), #middle branch side 2
               
               (range(SS+32, SS+35), RED), #middle branch side 1
               (range(SS+55, SS+58), RED), #middle branch side 2
               
               (range(SS+62, SS+65), RED), #middle branch side 1
               (range(SS+85, SS+88), RED), #middle branch side 2
               
               (range(SS+94, SS+98), RED), #lower branch side 1
               (range(SS+110, SS+114), RED), #lower branch side 2
               
               (range(SS+125, SS+128), RED), #lower branch side 1
               (range(SS+141, SS+145), RED), #lower branch side 2
               
               (range(SS+157, SS+161), RED), #lower branch side 1
               (range(SS+171, SS+175), RED), #lower branch side 2
               ]


SPECIAL_RD = [(range(SS+7,  SS+10), WHITE),
              (range(SS+19, SS+22), WHITE),
              (range(SS+37, SS+40), WHITE),
              (range(SS+49, SS+52), WHITE),
              (range(SS+67, SS+70), WHITE),
              (range(SS+79, SS+82), WHITE),
              (range(SS+90, SS+93), WHITE),              
              (range(SS+116, SS+119), WHITE),              
              (range(SS+120, SS+123), WHITE),              
              (range(SS+146, SS+149), WHITE),              
              (range(SS+152, SS+155), WHITE),
              (range(SS+179, SS+182), WHITE),
                             
              (range(SS+150,SS+152), DARK),
              (range(SS+183,SS+186), DARK),
              ]
    

FIXED_RD = [(range(SS+14, SS+16), YELLOW), 
            (range(SS+44, SS+46), YELLOW),
            (range(SS+74, SS+76), YELLOW)]
      
# Constants used to index the tuples stored as Strand Range Definitions.
RANGE = 0
COLOR = 1

TOP_REGION_NAMES = ['region0', 'region1', 'region2', 'region3', 'region4', 'region5']
BOTTOM_REGION_NAMES = ['region6', 'region7', 'region8', 'region9', 'region10', 'region11', 'region12']

# We will dynamically build list of regions from the Strand Range Definitions
branch_regions = []
white_tip_regions = []
fixed_branch_colors = []
partial_regions = []
flicker_regions = []
    
try:
    # Create a Strand with all LEDs 
    led_strand = Strand(NUMBER_OF_LEDS)
    
    # Create a region with all LEDs that is DARK, ie all LEDs are off.
    # Use this to turn all LEDs off as needed.
    region_dark = led_strand.add_region(10, 
                                        "region10", 
                                        range(0,NUMBER_OF_LEDS), 
                                        DARK)

    # Build the lists of regions using the Strand Range Definitions                                         
    for region_num, strand_range_def in enumerate(SRD):
        branch_regions.append(led_strand.add_region(region_num, 
                                             "region"+str(region_num), 
                                             strand_range_def[RANGE], 
                                             strand_range_def[COLOR]))
                                             
    for region_num, strand_range_def in enumerate(SPECIAL_RD):                                         
        white_tip_regions.append(led_strand.add_region(100 + region_num,
                                                 'region10'+str(region_num),
                                                 strand_range_def[RANGE],
                                                 strand_range_def[COLOR]))
        
    for region_num, strand_range_def in enumerate(FIXED_RD):                                         
        fixed_branch_colors.append(led_strand.add_region(200 + region_num,
                                                 'region20'+str(region_num),
                                                 strand_range_def[RANGE],
                                                 strand_range_def[COLOR]))

    for region_num, strand_range_def in enumerate(SRD_PARTIAL):
        partial_regions.append(led_strand.add_region(300+region_num, 
                                             "region30"+str(region_num), 
                                             strand_range_def[RANGE], 
                                             strand_range_def[COLOR]))

    for region_num, strand_range_def in enumerate(SRD_FLICKER):
        flicker_regions.append(led_strand.add_region(400+region_num, 
                                             "region40"+str(region_num), 
                                             strand_range_def[RANGE], 
                                             strand_range_def[COLOR]))

    state = 0

    branch_region_names = TOP_REGION_NAMES+BOTTOM_REGION_NAMES

    for a_region in branch_regions:
        if a_region.name in branch_region_names:
            led_strand.set_region(a_region)
    for white_tips in white_tip_regions:
        led_strand.set_region(white_tips)
    for fixed_colors in fixed_branch_colors:
        led_strand.set_region(fixed_colors)
    for flickers in flicker_regions:
        led_strand.set_region(flickers)
        
    while True:
        for a_region in branch_regions:
            if a_region.name in branch_region_names:
                led_strand.set_region(a_region)
        for partial_region in partial_regions:
            led_strand.set_region(partial_region)
        for flicker_region in flicker_regions:
            flicker_region.randomize([
                                DARK_RED,
                                DARK_BLUE,
                                LIGHT_YELLOW,
                                DARK_RED,
                                DARK_BLUE,
                                DARK_PURPLE,
                                BLUE_GREEN
                                ])
            led_strand.set_region(flicker_region)
        for white_tips in white_tip_regions:
            led_strand.set_region(white_tips)
        for fixed_colors in fixed_branch_colors:
            led_strand.set_region(fixed_colors)
            
        """    
        led_strand.advance_region(regions[0], regions[1])
        led_strand.advance_region(regions[2], regions[3])
        led_strand.advance_region(regions[4], regions[5])
        
        led_strand.advance_region(regions[6], regions[7])
        led_strand.advance_region(regions[8], regions[9])
        led_strand.advance_region(regions[10], regions[11])

        if state%10 == 1:
            led_strand.randomize_region(regions[11])
        """
        """
        if state%3 == 1:
            # Load the Strand Range Definitions into the LED strand
        elif state%3 == 2:
            led_strand.advance_region(regions[0], regions[1])
        else:
            # Load the completely dark definition into the LED strand
            led_strand.set_region(region_dark)
        """        
        
        led_strand.write_leds()
        state += 1
        time.sleep(0.5)	
			
finally:
    # After a keyboard interrupt or anything else that shuts things down,
    # turn off the LED strand
    print("BYE!")
    led_strand.ledstrip.reset_leds()
