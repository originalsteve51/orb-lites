# Strand
import time

import apa

from region import Region
from point_region import PointRegion

class Strand:
	
	# Region collection
	regions = {}
	
	def __init__(self, num_leds, one_color="no", immediate_write=False):
		self.ledstrip = apa.Apa(num_leds)
		self.num_leds = num_leds

	def add_region(self, region_num, name, region_range, rgb):
		r = Region(name, region_range, rgb)
		self.regions[region_num] = r
		return r

    # !!!
	def add_point_region(self, region_num, name, region_points, rgb):
		r = PointRegion(name, region_points, rgb)
		self.regions[region_num] = r
		return r

	def write_leds(self):
		self.ledstrip.write_leds()
		
	def advance_region(self, from_region, to_region):
		# push down region2
		to_region.push_down_leds(from_region)
		
	def smear_region(self, from_region, to_region):
		to_region.push_down_leds(from_region, True)
		
				
	def set_region(self, region):
		for led in region:
			self.ledstrip.led_set(led.id_num, led.brightness, led.b, led.g, led.r)
			#print('setting led', led.get_info())
				
		
	def get_info(self):
		info = ""
		for r_idx in range(0, len(self.regions)):
			info = info + "\n" + self.regions[r_idx].get_info()
		return info
	
	def randomize_region(self, region):
		region.randomize()
