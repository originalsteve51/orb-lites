import time

import apa

from region import Region
from strand import Strand

SS = 0 # Strand Start

SR = [range(SS,17), 
      range(SS+17,SS+17+22), 
      range(SS+17+22,SS+17+22+17), 
      range(SS+17+22+17,SS+17+22+17+17), 
      range(SS+17+22+17+17,SS+17+22+17+17+18),
      range(SS+17+22+17+17+18,SS+17+22+17+17+18+17),
      range(SS+17+22+17+17+18+17,SS+17+22+17+17+18+17+17),
      range(SS+17+22+17+17+18+17+17,SS+17+22+17+17+18+17+17+25)]

if __name__ == "__main__":
	
	all_off = (0,0,0)
	white = (255,255,255)
	red = (255,0,0)
	green = (0,255,0)
	blue = (0,0,255)

	try:
		
		led_strand = Strand(180)

		region0 = led_strand.add_region(0, "region0", SR[0], red)
		region1 = led_strand.add_region(1, "region1", SR[1], red)
		region2 = led_strand.add_region(2, "region2", SR[2], white)
		region3 = led_strand.add_region(3, "region3", SR[3], white)
		region4 = led_strand.add_region(4, "region4", SR[4], blue)
		region5 = led_strand.add_region(5, "region5", SR[5], blue)
		region6 = led_strand.add_region(6, "region6", SR[6], red)
		region7 = led_strand.add_region(7, "region7", SR[7], red)

		region100 = led_strand.add_region(100, "region100", range(30,47), white)
		region101 = led_strand.add_region(101, "region101", range(47,69), white)
		region102 = led_strand.add_region(102, "region102", range(69,86), red)
		region103 = led_strand.add_region(103, "region103", range(86,103), red)
		region104 = led_strand.add_region(104, "region104", range(103,121), blue)
		region105 = led_strand.add_region(105, "region105", range(121,138), blue)
		region106 = led_strand.add_region(106, "region106", range(138,155), white)
		region107 = led_strand.add_region(107, "region107", range(155,180), white)

		region200 = led_strand.add_region(200, "region200", range(30,47), blue)
		region201 = led_strand.add_region(201, "region201", range(47,69), blue)
		region202 = led_strand.add_region(202, "region202", range(69,86), white)
		region203 = led_strand.add_region(203, "region203", range(86,103), white)
		region204 = led_strand.add_region(204, "region204", range(103,121), red)
		region205 = led_strand.add_region(205, "region205", range(121,138), red)
		region206 = led_strand.add_region(206, "region206", range(138,155), blue)
		region207 = led_strand.add_region(207, "region207", range(155,180), blue)

		region_clear = led_strand.add_region(999, "region_clear", range(30,180), all_off)
		
		three_state = 0
		while True:
			three_state = three_state + 1
			if three_state % 3 == 0:				
				led_strand.set_region(region0)
				led_strand.set_region(region1)
				led_strand.set_region(region2)
				led_strand.set_region(region3)
				led_strand.set_region(region4)
				led_strand.set_region(region5)
				led_strand.set_region(region6)
				led_strand.set_region(region7)
			elif three_state % 3 == 1:
				led_strand.set_region(region100)
				led_strand.set_region(region101)
				led_strand.set_region(region102)
				led_strand.set_region(region103)
				led_strand.set_region(region104)
				led_strand.set_region(region105)
				led_strand.set_region(region106)
				led_strand.set_region(region107)
			else:
				led_strand.set_region(region200)
				led_strand.set_region(region201)
				led_strand.set_region(region202)
				led_strand.set_region(region203)
				led_strand.set_region(region204)
				led_strand.set_region(region205)
				led_strand.set_region(region206)
				led_strand.set_region(region207)

			led_strand.advance_region(region1, region0)
			led_strand.advance_region(region3, region2)
				
				
			led_strand.write_leds()
			time.sleep(0.1)	
					
	finally:
		print("BYE!")
		led_strand.ledstrip.reset_leds()
