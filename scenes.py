from phue import Bridge
b = Bridge('192.168.1.73')

# Get a dictionary with individual light numbers as the key (1,2,3,etc.)
lights = b.get_light_objects('id')

# Get a dictionary with the each light's name as the key (Kitchen, Bedroom, etc.)
light_names = b.get_light_objects('name')

# Get a flat list of the light objects
light_list = b.get_light_objects('list')

# Will turn on all lights in system
def all_on():
	b.set_light(lights,'on',True)

# Will turn off all lights in system
def all_off():
	b.set_light(lights,'on',False)

# Example to set a single light with easily visible settings
def nightlight():
	if b.get_light(1,'on') is False:
		lights[1].on = True
		lights[1].brightness = 0
		lights[1].hue = 0
		lights[1].saturation = 255
	else:
		lights[1].on = False

# Example to set all lights to the same setting.
def eveninglight():
	evening = {u'on': True, u'hue': 46256, u'colormode': u'ct', u'effect': u'none', u'alert': u'none', u'xy': [0.179, 0.0626], u'reachable': True, u'bri': 127, u'sat': 251, u'ct': 244}
	b.set_light(lights, evening)

# Creating a scene
def deepsea():
	deepsea = {u'on': True, u'hue': 65496, u'colormode': u'xy', u'effect': u'none', u'alert': u'none', u'xy': [0.6727, 0.3216], u'reachable': True, u'bri': 183, u'sat': 253, u'ct': 500}
	b.set_light([2,3], deepsea)