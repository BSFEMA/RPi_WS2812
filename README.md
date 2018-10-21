# RPi_WS2812 #

## NeoPixel library extended example ##
 
 Author: BSFEMA

 I followed this example to hook my Raspberry Pi 3 to a strip of WS2812B (60 LED per meter):
     https://dordnung.de/raspberrypi-ledstrip/ws2812
     
 I started with the example code provided from the "WS281X Library":
     https://github.com/jgarff/rpi_ws281x
     
 and added the various functions from this Arduino tutorial
     https://www.tweaking4all.com/hardware/arduino/adruino-led-strip-effects/
 as well as some of my own things.

 Here is an example video of the various functions:
     https://www.youtube.com/watch?v=NI3_y6l6Bto

 My Raspberry Pi setup is just the 'Raspbian Stretch With Desktop':
     https://www.raspberrypi.org/downloads/raspbian/
     
 I ran `sudo apt-get install xrdp` so I could remote into it to from my computer edit the python files and run it from a terminal.
 I also enabled SSH.

 To run it, I start a terminal, navigate to the folder with the files, and use the command: `sudo python main.py`

 Note:  This was my first Raspberry Pi + GPIO project, my first time with Python, and my first contribution to GitHub.
