# coding: utf-8
# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

w = int(device.getProperty("display.width"))
h = int(device.getProperty("display.height"))

print('width: ',w,' height:',h)

start = int(device.getProperty("clock.millis"))
count = 0
while True:
	current = int(device.getProperty("clock.millis"))
	if(current - start <= 5000):
		device.touch(int(w/2), int(h*0.9), MonkeyDevice.DOWN_AND_UP)
		count += 1
	else:
		break
		
print('touch count: ',count)

device.touch(int(w*0.83), int(h*0.28), MonkeyDevice.DOWN_AND_UP)