from phue import Bridge
b = Bridge('YOUR.IP.ADDRESS.HERE')

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

# Will turn light 1 on or off
def example():
	if b.get_light(1,'on') is False:
		b.set_light(1, 'on', True)
	else:
		b.set_light(1, 'on', False)

# Example to set a single light with easily visible settings. The
def nightlight():
	if b.get_light(1,'on') is False:
		lights[1].on = True
		lights[1].brightness = 0
		lights[1].hue = 0
		lights[1].saturation = 255
	else:
		lights[1].on = False

# Example to set all lights to the same setting.
# evening is defined by running a b.get_light(1)['state'] command in terminal while the 'evening light' preset is running on light 1, then copying the result and pasting it below.
def eveninglight():
	evening = {u'on': True, u'hue': 46256, u'colormode': u'ct', u'effect': u'none', u'alert': u'none', u'xy': [0.179, 0.0626], u'reachable': True, u'bri': 127, u'sat': 251, u'ct': 244}
	b.set_light(lights, evening)

# Creating a scene where lights 2 and 3 have the same setting and light 1 is unaffected
def deepsea():
	deepsea = {u'on': True, u'hue': 65496, u'colormode': u'xy', u'effect': u'none', u'alert': u'none', u'xy': [0.6727, 0.3216], u'reachable': True, u'bri': 183, u'sat': 253, u'ct': 500}
	b.set_light([2,3], deepsea)

# Creating a scene where all three lights are involved and have different settings
# Each light's settings were discovered by activating the "Taj" preset in the Hue app then running a b.get_light(LIGHTNUMBER)['state'] command in terminal for all three lights, then pasting the results below
def taj():
	b.set_light(1, {u'on': True, u'hue': 58985, u'colormode': u'xy', u'effect': u'none', u'alert': u'none', u'xy': [0.3889, 0.3652], u'reachable': True, u'bri': 166, u'sat': 19, u'ct': 262})
	b.set_light(2, {u'on': True, u'hue': 64206, u'colormode': u'xy', u'effect': u'none', u'alert': u'none', u'xy': [0.3936, 0.3729], u'reachable': True, u'bri': 181, u'sat': 13, u'ct': 267})
	b.set_light(3, {u'on': True, u'hue': 57049, u'colormode': u'xy', u'effect': u'none', u'alert': u'none', u'xy': [0.3859, 0.3601], u'reachable': True, u'bri': 196, u'sat': 23, u'ct': 256})