import time

import apa

from region import Region
from strand import Strand

SS = 0 # Strand Start

SR = [range(0,30), 
      range(30,60), 
      range(60,90), 
      range(90,120),
      range(120,150) 
      ]

if __name__ == "__main__":
	
	all_off = (0,0,0)
	white = (255,255,255)
	red = (255,0,0)
	green = (0,255,0)
	blue = (0,0,255)

	try:
		
		led_strand = Strand(150)

		region0 = led_strand.add_region(0, "region0", SR[0], green)
		region1 = led_strand.add_region(1, "region1", SR[1], green)
		region2 = led_strand.add_region(2, "region2", SR[2], green)
		region3 = led_strand.add_region(3, "region3", SR[3], all_off)
		region4 = led_strand.add_region(4, "region4", SR[4], all_off)

		three_state = 0
		while True:
			three_state = three_state + 1
			led_strand.set_region(region0)
			led_strand.set_region(region1)
			led_strand.set_region(region2)
			led_strand.set_region(region3)
			led_strand.set_region(region4)
			
			#led_strand.advance_region(region2, region0)
			#led_strand.advance_region(region3, region1)
			led_strand.write_leds()
			time.sleep(0.1)	
					
	finally:
		print("BYE!")
		led_strand.ledstrip.reset_leds()
