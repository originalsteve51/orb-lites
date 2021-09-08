# LED

class LED:
	def __init__(self, region_idx, id_num, r, g, b, brightness, color=""):
		self.region_idx = region_idx
		self.id_num = id_num
		self.r = r
		self.g = g
		self.b = b
		self.brightness = brightness
		self.color = color

	def set_brightness(self, setting):
		self.brightness = setting
		    
	def set_color(self, color):
	    self.r = color[0]
	    self.g = color[1]
	    self.b = color[2]
	    

	def get_info(self):
		return " region_idx: " + str(self.region_idx) + \
			" id: " + str(self.id_num) + \
			" r: " + str(self.r) + \
			" g: "+ str(self.g) + \
			" b: "+ str(self.b) + \
			" brightness: "+ str(self.brightness)+ \
			" color code: '"+ self.color + "'"

