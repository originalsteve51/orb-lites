import time


import apa

from region import Region
from strand import Strand

# Strand Start: Where in the LED strip is the first LED
SS = 0 

# Color definitions: RGB tuples
DARK    = (0,0,0)
WHITE   = (32,32,32)
RED     = (32,0,0)
GREEN   = (0,32,0)
BLUE    = (0,0,32)

# Strand range definitions
# Each is a tuple containing a range of LEDs and a color for the range
SRD = [(range(SS,      SS+15),    GREEN),
      (range(SS+15,    SS+30),    GREEN),
      (range(SS+30,    SS+45),    GREEN),
      (range(SS+45,    SS+60),    GREEN),
      (range(SS+60,    SS+75),    GREEN),
      (range(SS+75,    SS+90),    GREEN),
      (range(SS+92,    SS+107),   GREEN),
      (range(SS+107,   SS+122),   GREEN),
      (range(SS+126,   SS+141),   GREEN),
      (range(SS+141,   SS+156),   GREEN),
      (range(SS+156,   SS+171),   GREEN),
      (range(SS+171,   SS+186),   GREEN),
      
      # The last range definition is for the 60 LED spiral strip
      (range(SS+186,   SS+246),   WHITE) 
      ]
      
# Constants used to index the tuples stored as Strand Range Definitions.
RANGE = 0
COLOR = 1

# We will dynamically build list of regions from the Strand Range Definitions
regions = []
    
try:
    # Create a Strand with all LEDs 
    led_strand = Strand(240+6)
    
    # Create a region with all LEDs that is DARK, ie all LEDs are off.
    # Use this to turn all LEDs off as needed.
    region_dark = led_strand.add_region(10, 
                                        "region10", 
                                        range(0,240+6), 
                                        DARK)

    # Build the list of regions using the Strand Range Definitions                                         
    for region_num, strand_range_def in enumerate(SRD):
        regions.append(led_strand.add_region(region_num, 
                                             "region"+str(region_num), 
                                             strand_range_def[RANGE], 
                                             strand_range_def[COLOR]))
        
    state = 0
    while True:
        
        if state%3 == 1:
            # Load the Strand Range Definitions into the LED strand
            for a_region in regions:
                led_strand.set_region(a_region)
        else:
            # Load the completely dark definition into the LED strand
            led_strand.set_region(region_dark)
			    
        led_strand.write_leds()
        state += 1
        time.sleep(1.0)	
			
finally:
    # After a keyboard interrupt or anything else that shuts things down,
    # turn off the LED strand
    print("BYE!")
    led_strand.ledstrip.reset_leds()
