# Author: Frak Al-Nuaimy 
# email: frakman@hotmail.com

from PIL import ImageGrab
import time
import os
from colour import Color

#//////////////////////////////////////////////////////////////////////////////////////////////////////////
# GLOBAL DEFINES
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#HEIGHT         = 1920   #now using image.size[1] dynamically
#WIDTH          = 1200   #now using image.size[0] dynamically
LOOP_INTERVAL  = 3    # how often we calculate screen colour (in seconds)
DURATION       = 3    # how long it takes bulb to switch colours (in seconds)
DECIMATE       = 10   # skip every DECIMATE number of pixels to speed up calculation
#get your unit-unique token from http://developer.lifx.com/ and use it here
TOKEN          = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" 
BULB_NAME      = "all"  # you can use any label you've assigned your bulb here
#//////////////////////////////////////////////////////////////////////////////////////////////////////////


# run loop
while True:
	#init constants
	red   = 0
	green = 0
	blue  = 0
	
	time.sleep(LOOP_INTERVAL) #wake up ever so often and perform this ...
	#//////////////////////////////////////////////////////////////////////////////////////////////////////////
	# CALCULATE AVERAGE SCREEN COLOUR
	#//////////////////////////////////////////////////////////////////////////////////////////////////////////
	image = ImageGrab.grab()  # take a screenshot
	#print image.size
	
	for y in range(0, image.size[1], DECIMATE):  #loop over the height
		for x in range(0, image.size[0], DECIMATE):  #loop over the width
			#print "\n coordinates   x:%d y:%d \n" % (x,y)
			color = image.getpixel((x, y))  #grab a pixel
			# calculate sum of each component (RGB)
			red = red + color[0]
			green = green + color[1]
			blue = blue + color[2]
			#print red + " " +  green + " " + blue
			#print "\n totals   red:%s green:%s blue:%s\n" % (red,green,blue)
			#print color
	#print(time.clock())
	red = (( red / ( (image.size[1]/DECIMATE) * (image.size[0]/DECIMATE) ) ) )/255.0
	green = ((green / ( (image.size[1]/DECIMATE) * (image.size[0]/DECIMATE) ) ) )/255.0
	blue = ((blue / ( (image.size[1]/DECIMATE) * (image.size[0]/DECIMATE) ) ) )/255.0
	c= Color(rgb=(red, green, blue))  
	print c
	
	print "\n average   red:%s green:%s blue:%s" % (red,green,blue)
	#print "\n average   hue:%f saturation:%f luminance:%f" % (c.hue,c.saturation,c.luminance)
	print "\n average  (hex) "+  (c.hex)
	#//////////////////////////////////////////////////////////////////////////////////////////////////////////

	#//////////////////////////////////////////////////////////////////////////////////////////////////////////
	# PROGRAM LIFX BULB WITH COLOUR 
	#//////////////////////////////////////////////////////////////////////////////////////////////////////////
	cmd = " c:\\curl\\curl.exe -u \""+TOKEN+":\" -X PUT -d \"color=" + str(c.hex) + "\" -d \"duration=" +str(DURATION)+ "\" \"https://api.lifx.com/v1beta1/lights/label:"+BULB_NAME+"/color\"" 
	print cmd
	os.system(cmd)
	

