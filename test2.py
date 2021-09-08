import time

import apa

from region import Region
from strand import Strand


		

if __name__ == "__main__":
	
	test_orange = (255, 25, 0)
	
	all_off = (0,0,0)
	white = test_orange # (255,255,255)
	red = test_orange # (255,0,0)
	green = test_orange # (0,255,0)
	blue = test_orange # (0,0,255)

	try:
		
		led_strand = Strand(240)

		region0 = led_strand.add_region(0, "region0", range(60,90), all_off)
		region1 = led_strand.add_region(1, "region1", range(90,120), all_off)
		region2 = led_strand.add_region(2, "region2", range(120,150), all_off)
		region3 = led_strand.add_region(3, "region3", range(150,180), all_off)
		
		region100 = led_strand.add_region(100, "region100", range(60,90), red)
		region101 = led_strand.add_region(101, "region101", range(90,120), white)
		region102 = led_strand.add_region(102, "region102", range(120,150), blue)
		region103 = led_strand.add_region(103, "region103", range(150,180), all_off)
		
		region200 = led_strand.add_region(200, "region200", range(60,90), all_off)
		region201 = led_strand.add_region(201, "region201", range(90,120), red)
		region202 = led_strand.add_region(202, "region202", range(120,150), white)
		region203 = led_strand.add_region(203, "region203", range(150,180), blue)

		region300 = led_strand.add_region(300, "region300", range(60,90), blue)
		region301 = led_strand.add_region(301, "region301", range(90,120), all_off)
		region302 = led_strand.add_region(302, "region302", range(120,150), red)
		region303 = led_strand.add_region(303, "region303", range(150,180), white)
		
		region400 = led_strand.add_region(400, "region400", range(60,90), white)
		region401 = led_strand.add_region(401, "region401", range(90,120), blue)
		region402 = led_strand.add_region(402, "region402", range(120,150), all_off)
		region403 = led_strand.add_region(403, "region403", range(150,180), red)
		
		region1000 = led_strand.add_region(1000, "region1000", range(60,75), all_off)
		region1001 = led_strand.add_region(1001, "region1001", range(89,74,-1), all_off)
		region1002 = led_strand.add_region(1002, "region1002", range(90,105), all_off)
		region1003 = led_strand.add_region(1003, "region1003", range(119,104,-1), all_off)
		region1004 = led_strand.add_region(1004, "region1004", range(120,135), all_off)
		region1005 = led_strand.add_region(1005, "region1005", range(149,134,-1), all_off)
		region1006 = led_strand.add_region(1006, "region1006", range(150,165), all_off)
		region1007 = led_strand.add_region(1007, "region1007", range(179,164,-1), all_off)
		
		region1000.add_strip(red, 6)
		region1001.add_strip(white, 6)
		region1002.add_strip(blue, 6)
		region1003.add_strip(white, 6)
		region1004.add_strip(blue, 6)
		region1005.add_strip(red, 6)
		region1006.add_strip(red, 6)
		region1007.add_strip(white, 6)

		region2000 = led_strand.add_region(2000, "region2000", range(60,75), red)
		region2001 = led_strand.add_region(2001, "region2001", range(89,74,-1), red)
		region2002 = led_strand.add_region(2002, "region2002", range(90,105), red)
		region2003 = led_strand.add_region(2003, "region2003", range(119,104,-1), red)
		region2004 = led_strand.add_region(2004, "region2004", range(120,135), red)
		region2005 = led_strand.add_region(2005, "region2005", range(149,134,-1), red)
		region2006 = led_strand.add_region(2006, "region2006", range(150,165), red)
		region2007 = led_strand.add_region(2007, "region2007", range(179,164,-1), red)

		region2000.add_strip(white, 10)
		region2001.add_strip(white, 10)
		region2002.add_strip(white, 10)
		region2003.add_strip(white, 10)
		region2004.add_strip(white, 10)
		region2005.add_strip(white, 10)
		region2006.add_strip(white, 10)
		region2007.add_strip(white, 10)

		region2000.add_strip(blue, 8)
		region2001.add_strip(blue, 8)
		region2002.add_strip(blue, 8)
		region2003.add_strip(blue, 8)
		region2004.add_strip(blue, 8)
		region2005.add_strip(blue, 8)
		region2006.add_strip(blue, 8)
		region2007.add_strip(blue, 8)

		region0.add_strip(red, 2)
		region1.add_strip(white, 2)
		region2.add_strip(blue, 2)
		region3.add_strip(red, 2)
		
		region_equator = led_strand.add_region(999, "region_equator", range(30,60), all_off)
		region_dark_equator = led_strand.add_region(999, "region_equator", range(30,60), all_off)
		
		max_travel_strip = 30
		strip_end = max_travel_strip
		
		while strip_end > 6:
			region_equator.add_strip(white, strip_end)
			region_equator.add_strip(blue, strip_end - 2)
			region_equator.add_strip(red, strip_end - 4)
			region_equator.add_strip(all_off, strip_end - 6)
			
			strip_end = strip_end -12

		while True:
			
			loop_counter = 0
			while True and loop_counter < 150:
				led_strand.set_region(region2000)
				led_strand.set_region(region2001)
				led_strand.set_region(region2002)
				led_strand.set_region(region2003)
				led_strand.set_region(region2004)
				led_strand.set_region(region2005)
				led_strand.set_region(region2006)
				led_strand.set_region(region2007)
				
				led_strand.write_leds()
				
				led_strand.advance_region(region2000, region2000)
				led_strand.advance_region(region2001, region2001)
				led_strand.advance_region(region2002, region2002)
				led_strand.advance_region(region2003, region2003)
				led_strand.advance_region(region2004, region2004)
				led_strand.advance_region(region2005, region2005)
				led_strand.advance_region(region2006, region2006)
				led_strand.advance_region(region2007, region2007)
				
				time.sleep(0.0)			
				loop_counter = loop_counter + 1
			
			loop_counter = 0
			while True and loop_counter < 150:
				led_strand.set_region(region1000)
				led_strand.set_region(region1001)
				led_strand.set_region(region1002)
				led_strand.set_region(region1003)
				led_strand.set_region(region1004)
				led_strand.set_region(region1005)
				led_strand.set_region(region1006)
				led_strand.set_region(region1007)
							
				led_strand.write_leds()
				
				led_strand.advance_region(region1000, region1000)
				led_strand.advance_region(region1001, region1001)
				led_strand.advance_region(region1002, region1002)
				led_strand.advance_region(region1003, region1003)
				led_strand.advance_region(region1004, region1004)
				led_strand.advance_region(region1005, region1005)
				led_strand.advance_region(region1006, region1006)
				led_strand.advance_region(region1007, region1007)
				
				time.sleep(0.0)			
				loop_counter = loop_counter + 1
			
			loop_counter = 0
			while True and loop_counter < 250:
				
				led_strand.set_region(region0)
				led_strand.set_region(region1)
				led_strand.set_region(region2)
				led_strand.set_region(region3)
				
				led_strand.set_region(region_equator)
				
				led_strand.write_leds()
				led_strand.advance_region(region0, region0)
				led_strand.advance_region(region1, region1)			
				led_strand.advance_region(region2, region2)			
				led_strand.advance_region(region3, region3)			
				
				led_strand.advance_region(region_equator,region_equator)				
				time.sleep(0.0)	
				loop_counter = loop_counter + 1
				
			loop_counter = 0
			delay = 1
			led_strand.set_region(region_dark_equator)
			while True and loop_counter < 55:
				
				led_strand.set_region(region100)
				led_strand.set_region(region101)
				led_strand.set_region(region102)
				led_strand.set_region(region103)
				led_strand.write_leds()
				time.sleep(delay)
				led_strand.set_region(region200)
				led_strand.set_region(region201)
				led_strand.set_region(region202)
				led_strand.set_region(region203)
				led_strand.write_leds()
				time.sleep(delay)
				led_strand.set_region(region300)
				led_strand.set_region(region301)
				led_strand.set_region(region302)
				led_strand.set_region(region303)
				led_strand.write_leds()
				time.sleep(delay)
				led_strand.set_region(region400)
				led_strand.set_region(region401)
				led_strand.set_region(region402)
				led_strand.set_region(region403)
				led_strand.write_leds()
				time.sleep(delay)
				loop_counter = loop_counter + 1
				delay = delay * .8
	finally:
		print("BYE!")
		led_strand.ledstrip.reset_leds()
