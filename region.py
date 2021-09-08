# Region - A Strand has 0 or more Regions. The LEDs on the Strand are mapped to Regions.
# Regions use 0 or more LEDs from the Strand they are associated with.
# Region has a map keyed 0..n that maps to the n LEDs assigned to it in the associated Strand.
import random
from led import LED

class Region(object):
	def __init__(self, region_name, strand_range, rgb):
		self.name = region_name
		self.map = {}
		self.leds = []
		self.state = 0
		idx = 0
		for n in strand_range:
			self.map[idx] = n
			self.leds.append(LED(idx, n, rgb[0], rgb[1], rgb[2], 200))
			idx = idx + 1
			
	def __iter__(self):
		self.idx = 0
		return self
		
	def __next__(self):
		if self.idx < len(self.leds):
			led = self.leds[self.idx]
			self.idx = self.idx + 1
			return led
		else:
			raise StopIteration
	
	def split(self, leds, size):
		split_leds = []
		while len(leds) > size:
			piece = leds[:size]
			split_leds.append(piece)
			leds   = leds[size:]
		split_leds.append(leds)
		return split_leds
			
	# get both the absolute strand number of an led and the corresponding LED object
	def get_led_num(self, idx):
		print(self.name, idx, len(self.leds))
		return self.leds[idx]
		
	def get_last_led(self):
		return self.leds[len(self.leds)-1]
		
	def push_down_leds(self, other_region, smear=False):
		this_region_size = len(self.leds)
		other_region_size = len(other_region.leds)
		
		split_size = max(this_region_size, other_region_size)
		
		# combine the regions
		self.leds.extend(other_region.leds)
		
		# get the first led and make it last
		self.leds.append(self.leds[0])
		
		# remove the first, which is now last
		if not smear:
			del self.leds[0]
		
		split_leds = self.split(self.leds, split_size)
		
		if this_region_size == split_size:
			self.leds = split_leds[0]
			other_region.leds = split_leds[1]
		else:
			self.leds = split_leds[1]
			other_region.leds = split_leds[0]
			
		self.renumber(self)
		self.renumber(other_region)
			
	def renumber(self, region):
		for map_idx, map_target in region.map.items():
			region.leds[map_idx].region_idx = map_idx
			region.leds[map_idx].id_num = map_target
						
				
	def get_info(self):
		info = ""
		for map_idx, map_target in self.map.items():
			info = info + "\n" + str(map_idx) + ", " + str(map_target) + \
					", led: " + self.get_led_num(map_idx).get_info()
		return "\n" + "Region name: " + self.name  + info

	# set the led by its region index using an rgb tuple
	def set_led_num(self, idx, rgb, rgb_bright=200):
		led = self.leds[idx]
		led.r = rgb[0]
		led.g = rgb[1]
		led.b = rgb[2]		
		led.brightness = rgb_bright
	
	def add_strip(self, rgb_tuple, count):
		for idx in range(count):
			self.set_led_num(idx, rgb_tuple)
	
	
		
	def set(self, led, rgb, rgb_bright=255):
		led = self.leds[led.region_idx]
		led.r = rgb[0]
		led.g = rgb[1]
		led.b = rgb[2]
		led.brightness = rgb_bright		
		
	DEFAULT_COLORS = [ (65,0,0), (65,65,0), (0,0,65), (0,65,65), (0,0,0), (0,0,0),
	                   (0,0,0), (0,0,0), (0,0,0), (0,0,0),] 	
		
	def randomize(self, color_profile=DEFAULT_COLORS):
		colors = color_profile
		for an_led in self.leds:
			self.set(an_led, random.choice(colors))