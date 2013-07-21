huekey
======

Control Philips Hue lights with BetterTouchTool (or any script launcher)

Using huekey requires that you already have [phue](https://github.com/studioimaginaire/phue) installed on your system. Please go to their repository and follow the instructions there to install.

To install huekey from git you can either download the zip or execute the following command in terminal after navigating to the directory where you want huekey to live.
```
	git clone https://github.com/bradykent/huekey
```
There are two main components to huekey: the scenes.py file and the command scripts.

##Scenes.py
You will define all of the scenes you want to be able to trigger in this file. I've provided some examples to get started, but you'll have to individually code the lights if you want to create particular scenes.
If you're uncomfortable with sending individual commands to control the lights, I'd recommend getting the status of your system when you have it set to your liking and using that response to control the lights.

Before you begin, make sure to edit the scenes.py file, line 2, to add your bridge's IP address.

For example, if I like the settings on lights 2 and 3 and want to turn that into a scene, I would execute the following commands in Terminal:
```
	python
	from phue import bridge
	b = Bridge('Your.IP.Address.Here') #phue will attempt to establish a connection with the bridge here. If this is the first time running it, you'll need to press the button on the bridge
	b.get_light(2)['state'] #copy the response from this command and add it to the scenes.py file using a text editor.
	b.get_light(3)['state'] #copy the response from this command and add it to the scenes.py file using a text editor.
```
Now the preset for lights 2 and 3 has been discovered and added to the scenes.py file. Now I need to take the scenes and turn them into something BetterTouchTool (BTT) can see.

##Command scripts
Open up a command script (we'll use example.command, but alloff.command and nightlight.command have also been provided) in a text editor. These files are pretty basic but should help keep scene activation run quickly.
The command files contain the following three lines (we'll use the example file):
```
	#!/usr/bin/env python  # <--This will tell terminal that the following lines should be executed in python.
	from scenes import example  # <--This imports the example scene from the scenes.py file.
	example() # <--This runs the example scene and changes the lights.
```
After you change the above lines to work, save the file with a name that you'll remember.

**IMPORTANT:** The command scripts need to be in the same folder as the scenes.py file to work. They also need to be executable (Either via the Terminal by running: chmod +x file.command or by Get Info in Finder)

##BetterTouchTool
Now for the final step. Open BTT and create your actions, pointing the triggers to "Open Application / File / Script" and then selecting the script you want to run. Then test it and it should work!

If you want terminal to close automatically after running the script, go to Terminal preferences->settings->shell and change "When the shell exits:" to "Close if the shell exited cleanly"
