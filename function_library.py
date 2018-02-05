#This is the function library.  This is imported by main.py

import time
import math
import random
from neopixel import *
from array import *
import argparse
import signal
import sys
import datetime

def signal_handler(signal, frame):
        colorWipe(strip, Color(0,0,0))
        sys.exit(0)

def opt_parse():
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', action='store_true', help='clear the display on exit')
        args = parser.parse_args()
        if args.c:
                signal.signal(signal.SIGINT, signal_handler)

#LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

#Define functions which animate LEDs in various ways.
def SetAll(strip, color):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)

def FadeRGB(strip):
    for i in range(0, 3):
        #Fade In.
        for j in range (0, 256):
            if i == 0:
                SetAll(strip, Color(j, 0, 0))
            elif i == 1:
                SetAll(strip, Color(0, j, 0))
            elif i == 2:
                SetAll(strip, Color(0, 0, j))
            strip.show()
        #Fade Out.
        for j in range (256, 0, -1):
            if i == 0:
                SetAll(strip, Color(j, 0, 0))
            elif i == 1:
                SetAll(strip, Color(0, j, 0))
            elif i == 2:
                SetAll(strip, Color(0, 0, j))
            strip.show()

def FadeInOut(strip, red, green, blue):
    #Fade In.
    for i in range (0, 256):
        r = int(math.floor((i / 256.0) * red))
        g = int(math.floor((i / 256.0) * green))
        b = int(math.floor((i / 256.0) * blue))
        SetAll(strip, Color(r, g, b))
        strip.show()
    #Fade Out.
    for i in range (256, 0, -1):
        r = int(math.floor((i / 256.0) * red))
        g = int(math.floor((i / 256.0) * green))
        b = int(math.floor((i / 256.0) * blue))
        SetAll(strip, Color(r, g, b))
        strip.show()

def Strobe(strip, red, green, blue, StrobeCount, FlashDelay, EndPause):
    for i in range (0, StrobeCount):
        SetAll(strip, Color(red, green, blue))
        strip.show()
        time.sleep(FlashDelay)
        SetAll(strip, Color(0, 0, 0))
        strip.show()
        time.sleep(FlashDelay)
    time.sleep(EndPause)

def Cylon(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay):
    for i in range (0, (LED_COUNT - EyeSize - 2)):
        SetAll(strip, Color(0, 0, 0))
        strip.setPixelColor(i, Color(int(math.floor(red / 10)), int(math.floor(green / 10)), int(math.floor(blue / 10))))
        for j in range(1, (EyeSize + 1)):
            strip.setPixelColor(i + j, Color(red, green, blue))
        strip.setPixelColor(i + EyeSize + 1, Color(int(math.floor(red / 10)), int(math.floor(green / 10)), int(math.floor(blue / 10))))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)
    for i in range ((LED_COUNT - EyeSize - 2), 0, -1):
        SetAll(strip, Color(0, 0, 0))
        strip.setPixelColor(i, Color(int(math.floor(red / 10)), int(math.floor(green / 10)), int(math.floor(blue / 10))))
        for j in range(1, (EyeSize + 1)):
            strip.setPixelColor(i + j, Color(red, green, blue))
        strip.setPixelColor(i + EyeSize + 1, Color(int(math.floor(red / 10)), int(math.floor(green / 10)), int(math.floor(blue / 10))))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)

def Twinkle(strip, red, green, blue, Count, SpeedDelay, OnlyOne):
    SetAll(strip, Color(0, 0, 0))
    for i in range (0, Count):
        strip.setPixelColor(random.randrange(0, LED_COUNT), Color(red, green, blue))
        strip.show()
        time.sleep(SpeedDelay)
        if OnlyOne:
            SetAll(strip, Color(0, 0, 0))
    time.sleep(SpeedDelay)

def TwinkleRandom(strip, Count, SpeedDelay, OnlyOne):
    SetAll(strip, Color(0, 0, 0))
    for i in range (0, Count):
        strip.setPixelColor(random.randrange(0, LED_COUNT), Color(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)))
        strip.show()
        time.sleep(SpeedDelay)
        if OnlyOne:
            SetAll(strip, Color(0, 0, 0))
    time.sleep(SpeedDelay)

def Sparkle(strip, red, green, blue, SpeedDelay):
    pixel=random.randrange(0, LED_COUNT)
    strip.setPixelColor(pixel, Color(red, green, blue))
    strip.show()
    time.sleep(SpeedDelay)
    strip.setPixelColor(pixel, Color(0, 0, 0))
    
def SnowSparkle(strip, red, green, blue, SparkleDelay, SpeedDelay):
    SetAll(strip, Color(red, green, blue))    
    pixel=random.randrange(0, LED_COUNT)
    strip.setPixelColor(pixel, Color(255, 255, 255))
    strip.show()
    time.sleep(SparkleDelay)
    strip.setPixelColor(pixel, Color(red, green, blue))
    strip.show()
    time.sleep(SpeedDelay)
    
def RunningLights(strip, red, green, blue, WaveDelay):
    Position=0
    for i in range (0, (LED_COUNT * 2)):
        Position = Position + 1
        for i in range (0, LED_COUNT):
            strip.setPixelColor(i, Color(int(math.floor(((math.sin(i+Position) * 127 + 128) / 255) * red)), int(math.floor(((math.sin(i+Position) * 127 + 128) / 255) * green)), int(math.floor(((math.sin(i+Position) * 127 + 128) / 255) * blue))))
        strip.show()
        time.sleep(WaveDelay)

def RunningLightsOther(strip, red, green, blue, WaveDelay):
    Position=0
    for i in range ((LED_COUNT * 2), 0, -1):
        Position = Position - 1
        for i in range (0, LED_COUNT):
            strip.setPixelColor(i, Color(int(math.floor(((math.sin(i+Position) * 127 + 128) / 255) * red)), int(math.floor(((math.sin(i+Position) * 127 + 128) / 255) * green)), int(math.floor(((math.sin(i+Position) * 127 + 128) / 255) * blue))))
        strip.show()
        time.sleep(WaveDelay)

def ColorWipe(strip, red, green, blue, SpeedDelay):
    for i in range (0, LED_COUNT):
        strip.setPixelColor(i, Color(red, green, blue))
        strip.show()
        time.sleep(SpeedDelay)

def ColorWipeReverse(strip, red, green, blue, SpeedDelay):
    for i in range (LED_COUNT, 0, -1):
        strip.setPixelColor(i, Color(red, green, blue))
        strip.show()
        time.sleep(SpeedDelay)

def Wheel(WheelPosition):
	#Generate rainbow colors across 0-255 positions.
	if WheelPosition < 85:
		return Color(WheelPosition * 3, 255 - WheelPosition * 3, 0)
	elif WheelPosition < 170:
		WheelPosition -= 85
		return Color(255 - WheelPosition * 3, 0, WheelPosition * 3)
	else:
		WheelPosition -= 170
		return Color(0, WheelPosition * 3, 255 - WheelPosition * 3)
	    
def Rainbow(strip, SpeedDelay):
    for i in range(0, 256):
	for j in range(0, LED_COUNT):
		strip.setPixelColor(j, Wheel((j + i) & 255))
	strip.show()
	time.sleep(SpeedDelay)

def RainbowCycle(strip, Iterations, SpeedDelay):
    for i in range (0, 256 * Iterations):
        for j in range (0, LED_COUNT):
            strip.setPixelColor(j, Wheel((int(j * 256 / LED_COUNT) + i) & 255))
	strip.show()
	time.sleep(SpeedDelay)
    
def ColorChase(strip, red, green, blue, SpeedDelay):
	for i in range(LED_COUNT):
		strip.setPixelColor(i, Color(red, green, blue))
		strip.show()
		time.sleep(SpeedDelay)
		strip.setPixelColor(i, Color(0, 0, 0))
		strip.show()

def ColorChaseReverse(strip, red, green, blue, SpeedDelay):
	for i in range(LED_COUNT, 0, -1):
		strip.setPixelColor(i, Color(red, green, blue))
		strip.show()
		time.sleep(SpeedDelay)
		strip.setPixelColor(i, Color(0, 0, 0))
		strip.show()

def TheaterChase(strip, red, green, blue, SpeedDelay, Iterations):
	for i in range(0, Iterations):
		for j in range(0, 3):
			for k in range(0, LED_COUNT, 3):
				strip.setPixelColor(k + j, Color(red, green, blue))
			strip.show()
			time.sleep(SpeedDelay)
			for k in range(0, LED_COUNT, 3):
				strip.setPixelColor(k + j, Color(0, 0, 0))

def TheaterChaseRainbow(strip, SpeedDelay):
	#Rainbow movie theater light style chaser animation.
	for i in range(256):
		for j in range(3):
			for k in range(0, strip.numPixels(), 3):
				strip.setPixelColor(k + j, Wheel((k + i) % 255))
			strip.show()
			time.sleep(SpeedDelay)
			for k in range(0, strip.numPixels(), 3):
				strip.setPixelColor(k + j, Color(0, 0, 0))

def MeteorRain(strip, red, green, blue, MeteorSize, MeteorTrailDecay, MeteorRandomDecay, SpeedDelay):
    SetAll(strip, Color(0, 0, 0))
    for i in range (0, LED_COUNT + LED_COUNT):
        # Fade brightness all LEDs one step
        for j in range (0, LED_COUNT):
            if ((not MeteorRandomDecay) or ((random.randint(0, 10)>5))):
                FadeToBlack(strip, j, MeteorTrailDecay)
        # Draw meteor
        for j in range (0, MeteorSize):
            if (((i - j) < LED_COUNT) and ((i - j) >= 0)):
                strip.setPixelColor(i - j, Color(red, green, blue))
        strip.show()
        time.sleep(SpeedDelay)

#Used by MeteorRain
def FadeToBlack(strip, Position, FadeValue):
    OldColor = strip.getPixelColor(Position)
    r = (OldColor & 0x00ff0000) >> 16
    g = (OldColor & 0x0000ff00) >> 8
    b = (OldColor & 0x000000ff)
    if (r<=10):
        r = 0;
    else:
        r = r - (r * FadeValue / 256)
    if (g<=10):
        g = 0;
    else:
        g = g - (g * FadeValue / 256)
    if (b<=10):
        b = 0;
    else:
        b = b - (b * FadeValue / 256)
    strip.setPixelColor(Position, Color(r, g, b))

def NewKitt(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay):
    RightToLeft(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)
    LeftToRight(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)
    OutsideToCenter(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)
    CenterToOutside(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)
    RightToLeft(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)
    LeftToRight(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)
    OutsideToCenter(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)
    CenterToOutside(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)

#Used by NewKitt
def CenterToOutside(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay):
    for i in range(int(math.floor((LED_COUNT-EyeSize)/2)), 0, -1):
        SetAll(strip, Color(0, 0, 0))
        strip.setPixelColor(i, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        for j in range(1, EyeSize + 1):
            strip.setPixelColor(i + j, Color(red, green, blue))
        strip.setPixelColor(i + EyeSize + 1, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        strip.setPixelColor(LED_COUNT - i, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        for j in range(1, EyeSize + 1):
            strip.setPixelColor(LED_COUNT - i - j, Color(red, green, blue))
        strip.setPixelColor(LED_COUNT - i - EyeSize - 1, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)

#Used by NewKitt
def OutsideToCenter(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay):
    for i in range(0, int(math.floor((LED_COUNT-EyeSize)/2))):
        SetAll(strip, Color(0, 0, 0))
        strip.setPixelColor(i, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        for j in range(1, EyeSize + 1):
            strip.setPixelColor(i + j, Color(red, green, blue))
        strip.setPixelColor(i + EyeSize + 1, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        strip.setPixelColor(LED_COUNT - i, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        for j in range(1, EyeSize + 1):
            strip.setPixelColor(LED_COUNT - i - j, Color(red, green, blue))
        strip.setPixelColor(LED_COUNT - i - EyeSize - 1, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)

#Used by NewKitt
def LeftToRight(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay):
    for i in range(0, LED_COUNT - EyeSize - 2):
        SetAll(strip, Color(0, 0, 0))
        strip.setPixelColor(i, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        for j in range(1, EyeSize+1):
            strip.setPixelColor(i + j, Color(red, green, blue))
        strip.setPixelColor(i + EyeSize + 1, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)

#Used by NewKitt
def RightToLeft(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay):
    for i in range(LED_COUNT - EyeSize - 2, 0, -1):
        SetAll(strip, Color(0, 0, 0))
        strip.setPixelColor(i, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        for j in range(1, EyeSize + 1):
            strip.setPixelColor(i + j, Color(red, green, blue))
        strip.setPixelColor(i + EyeSize + 1, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)

#The Heat array needs to be declaired globally.  You can put it in the main section (but not in the While loop), but not in the Fire function...
Heat = [0] * LED_COUNT
def Fire(strip, Heat, Cooling, Sparking, SpeedDelay):
    #Step 1.  Cool down every cell a little
    for i in range(0, LED_COUNT):
        CoolDown = random.randint(0, (int(math.floor((Cooling * 10) / LED_COUNT)) + 2))
        if (CoolDown > Heat[i]):
            Heat[i] = 0
        else:
            Heat[i] = Heat[i] - CoolDown
    #Step 2.  Heat from each cell drifts 'up' and diffuses a little
    for i in range((LED_COUNT - 1), 2, -1):
        Heat[i] = int(math.floor((Heat[i - 1] + Heat[i - 2] + Heat[i - 2]) / 3))
    #Step 3.  Randomly ignite new 'sparks' near the bottom
    if (random.randint(0, 255) < Sparking):
        y=random.randint(0, 7)
        #There are 2 different ways to do this part, the commented out line is the alternate
        Heat[y] = Heat[y] + random.randrange(160, 255)
        #Added check to original code so that the heat never exceeds 255
        if (Heat[y]>255): Heat[y]=255
        #Heat[y] = random.randrange(160, 255)
    #Step 4.  Convert heat to LED colors
    for i in range(0, LED_COUNT):
        SetPixelHeatColor(strip, i, Heat[i])
    #Step 5.  Display
    strip.show()
    time.sleep(SpeedDelay)

#Used by Fire
def SetPixelHeatColor(strip, Pixel, Temperature):
    #Scale 'heat' down from 0-255 to 0-191
    t192 = int(math.floor((Temperature / 255.0) * 191))
    #calculate ramp up from
    HeatRamp = t192 & 0x3F #0..63
    HeatRamp <<= 2 #scale up to 0..252
    #figure out which third of the spectrum we're in:
    if (t192 > 0x80):
        strip.setPixelColor(Pixel, Color(255, 255, HeatRamp))
    elif(t192 > 0x40):
        strip.setPixelColor(Pixel, Color(255, HeatRamp, 0))
    else:
        strip.setPixelColor(Pixel, Color(HeatRamp, 0, 0))

#Used by BouncingBalls and BouncingBallsRGB
def GetMillis():
    return (time.time() * 1000)

def BouncingBalls(strip, red, green, blue, BallCount):
    Gravity = -9.81
    StartHeight = 1
    Height = [0] * BallCount
    ImpactVelocityStart = math.sqrt(-2 * Gravity * StartHeight)
    ImpactVelocity = [0] * BallCount
    TimeSinceLastBounce = [0] * BallCount
    Position = [0] * BallCount
    ClockTimeSinceLastBounce = [0] * BallCount
    Dampening = [0] * BallCount
    for i in range(0, BallCount):
        ClockTimeSinceLastBounce[i] = GetMillis()
        Height[i] = StartHeight
        Position[i] = 0
        ImpactVelocity[i] = ImpactVelocityStart
        TimeSinceLastBounce[i] = 0
        Dampening[i] = 0.90 - (i / math.pow(BallCount,2))
    for i in range(0, BallCount):
        TimeSinceLastBounce[i] = GetMillis() - ClockTimeSinceLastBounce[i]
        Height[i] = 0.5 * Gravity * math.pow((TimeSinceLastBounce[i] / 1000), 2.0) + ImpactVelocity[i] * (TimeSinceLastBounce[i] / 1000)
        if (Height[i] < 0):
            Height[i] = 0
            ImpactVelocity[i] = Dampening[i] * ImpactVelocity[i]
            ClockTimeSinceLastBounce[i] = GetMillis()
            if (ImpactVelocity[i] < 0.01):
                ImpactVelocity[i] = ImpactVelocityStart
        Position[i] = int(math.floor((Height[i] * (LED_COUNT - 1)) / StartHeight))
    for i in range(0, BallCount):
        strip.setPixelColor(Position[i], Color(red, green, blue))
    strip.show()
    SetAll(strip, Color(0, 0, 0))

def BouncingBallsRGB(strip, BallCount, BallColors):
    Gravity = -9.81
    StartHeight = 1
    Height = [0] * BallCount
    ImpactVelocityStart = math.sqrt(-2 * Gravity * StartHeight)
    ImpactVelocity = [0] * BallCount
    TimeSinceLastBounce = [0] * BallCount
    Position = [0] * BallCount
    ClockTimeSinceLastBounce = [0] * BallCount
    Dampening = [0] * BallCount
    for i in range(0, BallCount):
        ClockTimeSinceLastBounce[i] = GetMillis()
        Height[i] = StartHeight
        Position[i] = 0
        ImpactVelocity[i] = ImpactVelocityStart
        TimeSinceLastBounce[i] = 0
        Dampening[i] = 0.90 - (i / math.pow(BallCount,2))
    for i in range(0, BallCount):
        TimeSinceLastBounce[i] = GetMillis() - ClockTimeSinceLastBounce[i]
        Height[i] = 0.5 * Gravity * math.pow((TimeSinceLastBounce[i] / 1000), 2.0) + ImpactVelocity[i] * (TimeSinceLastBounce[i] / 1000)
        if (Height[i] < 0):
            Height[i] = 0
            ImpactVelocity[i] = Dampening[i] * ImpactVelocity[i]
            ClockTimeSinceLastBounce[i] = GetMillis()
            if (ImpactVelocity[i] < 0.01):
                ImpactVelocity[i] = ImpactVelocityStart
        Position[i] = int(math.floor((Height[i] * (LED_COUNT - 1)) / StartHeight))
    for i in range(0, BallCount):
        strip.setPixelColor(Position[i], Color(BallColors[i][i], BallColors[i][1], BallColors[i][2]))
    strip.show()
    SetAll(strip, Color(0, 0, 0))

def HalloweenEyes(strip, red, green, blue, EyeWidth, EyeSpace, Fade, Steps, FadeDelay, EndPause):
    StartPoint = random.randint(0, LED_COUNT - (2 * EyeWidth) - EyeSpace)
    Start2ndEye = StartPoint + EyeWidth + EyeSpace
    for i in range(0, EyeWidth):
        strip.setPixelColor(StartPoint + i, Color(red, green, blue))
        strip.setPixelColor(Start2ndEye + i, Color(red, green, blue))
    strip.show()
    if (Fade):
        for i in range(Steps, -1, -1):
            r = i * int(math.floor(red / Steps))
            g = i * int(math.floor(green / Steps))
            b = i * int(math.floor(blue / Steps))
            for j in range(0, EyeWidth):
                strip.setPixelColor(StartPoint, Color(r, g, b))
                strip.setPixelColor(Start2ndEye, Color(r, g, b))
            strip.show()
            time.sleep(FadeDelay)
    SetAll(strip, Color(0, 0, 0))
    time.sleep(EndPause)

#Morse Code dictionary
MORSE_CODE_DICT = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}
def MorseCode(strip, red, green, blue, Message, DotLength):
    Message = Message.upper()
    MessageArray=list(Message)
    cipher = ''
	#Fill cipher with converted MessageArray values
    for i in range(0, len(MessageArray)):
        if MessageArray[i] != ' ':
            if i < (len(MessageArray)-1):
                if MessageArray[i+1] == ' ':
                    cipher += MORSE_CODE_DICT[MessageArray[i]]
                else:
                    cipher += MORSE_CODE_DICT[MessageArray[i]] + ' '
            else:
                cipher += MORSE_CODE_DICT[MessageArray[i]]
        else:
            cipher += '='
    """
	Dot length = Dot length x 1
    Dash length = Dot length x 3
    Pause between elements = Dot length x 1
    Pause between characters = Dot length x 3
    Pause between words = Dot length x 7
	"""
    for element in cipher:
        if element == '.':
            SetAll(strip, Color(red, green, blue))
            strip.show()
            time.sleep(DotLength)
            #Include Pause between elements
            SetAll(strip, Color(0, 0, 0))
            strip.show()
            time.sleep(DotLength)
        elif element == '-':
            SetAll(strip, Color(red, green, blue))
            strip.show()
            time.sleep(DotLength * 3)
            #Include Pause between elements
            SetAll(strip, Color(0, 0, 0))
            strip.show()
            time.sleep(DotLength)
        elif element == ' ':
            #Since we have already included an element Pause, only pause between characters for 2 dot lengths
            SetAll(strip, Color(0, 0, 0))
            strip.show()
            time.sleep(DotLength * 2)
        elif element == '=':
            #Since we have already included an element Pause, only pause between words for 6 dot lengths
            SetAll(strip, Color(0, 0, 0))
            strip.show()
            time.sleep(DotLength * 6)
    #Give word pause at end of message. Since we have already included an element Pause, only pause between words for 6 dot lengths
    SetAll(strip, Color(0, 0, 0))
    strip.show()
    time.sleep(DotLength * 6)

def Clock1(strip):
    #This function is geared towards my 60 LED strip; you'll need to modify it if you have something else.
    #Get the current Time
    CurrentTime=datetime.datetime.now()
    Hours = int(CurrentTime.hour)
    Minutes = int(CurrentTime.minute)
    Seconds = int(CurrentTime.second)
    Microseconds = int(CurrentTime.microsecond) #range=1,000,000
    #Convert from 24h to 12h
    if (Hours>12):
        AMPM="PM"
        Hours=Hours-12
    else:
        AMPM="AM"
    #Output    = LED   - Notes
    #Hours     = 0-11  - Divided into 4 red, 4 green, and 4 blue for easier counting
    #AMPM      = 12    - AM = solid white, PM = blinking white
    #Seperator = 13
    #Minutes   = 14-43 - 30 pixels - blinks the last pixel if it is the first half of the 2 minutes, solid for the 2nd half of the 2 minutes
    #Seperator = 44
    #Seconds   = 45-59 - 15 pixels - each pixel represents 4 seconds, the last pixel increases brightness for each second
    SetAll(strip, Color(0, 0, 0))
    #Hours
    for i in range(1,4+1):
        if (i>Hours):
            strip.setPixelColor(i-1, Color(0, 0, 0))
        else:
            strip.setPixelColor(i-1, Color(255, 0, 0))
    for i in range(5,8+1):
        if (i>Hours):
            strip.setPixelColor(i-1, Color(0, 0, 0))
        else:
            strip.setPixelColor(i-1, Color(0, 255, 0))
    for i in range(9,12+1):
        if (i>Hours):
            strip.setPixelColor(i-1, Color(0, 0, 0))
        else:
            strip.setPixelColor(i-1, Color(0, 0, 255))
    #AMPM
    if (AMPM=='AM'):
        strip.setPixelColor(12, Color(255, 255, 255))
    else:
        #Blink the PM
        if (Microseconds<500000):
            strip.setPixelColor(12, Color(0, 0, 0))
        else:
            strip.setPixelColor(12, Color(255, 255, 255))
    #Seperator
    strip.setPixelColor(13, Color(128, 0, 255))
    #Minutes
    for i in range(0,30):
        if Minutes>((i*2)+1):
            strip.setPixelColor(i+14, Color(255, 255, 0))
        elif Minutes==(i*2) or Minutes==((i*2)+1):
            if Minutes==(i*2):
                if (Microseconds<500000):
                    strip.setPixelColor(12, Color(0, 0, 0))
                else:
                    strip.setPixelColor(i+14, Color(255, 255, 0))
            else:
                strip.setPixelColor(i+14, Color(255, 255, 0))
        else:
            strip.setPixelColor(i+14, Color(0, 0, 0))
    #Seperator
    strip.setPixelColor(44, Color(128, 0, 255))
    #Seconds
    for i in range(0,15):
        if Seconds>((i*4)+3):
            strip.setPixelColor(i+45, Color(0, 255, 255))
        elif (i*4) <= Seconds <= ((i*4)+3):
            if Seconds==((i*4)+0):
                strip.setPixelColor(i+45, Color(0, 51, 51))
            elif Seconds==((i*4)+1):
                strip.setPixelColor(i+45, Color(0, 102, 102))
            elif Seconds==((i*4)+2):
                strip.setPixelColor(i+45, Color(0, 153, 153))
            else:
                strip.setPixelColor(i+45, Color(0, 204, 204))
        else:
            strip.setPixelColor(i+45, Color(0, 0, 0))
    #Show Results
    strip.show()

def Clock2(strip, IncludeHours):
    #This function is geared towards my 60 LED strip; you'll need to modify it if you have something else.
    #Based on this: https://www.youtube.com/watch?v=YTbRFqJvVOE
    #Get the current Time
    CurrentTime=datetime.datetime.now()
    Hours = int(CurrentTime.hour)
    Minutes = int(CurrentTime.minute)
    Seconds = int(CurrentTime.second)
    #Convert from 24h to 12h
    if (Hours>12):
        AMPM="PM"
        Hours=Hours-12
    else:
        AMPM="AM"
    #Output
    SetAll(strip, Color(0, 0, 0))
    if IncludeHours:
        for i in range (0, 60):
            if i%5==0:
                strip.setPixelColor(i, Color(64, 64, 64))
    HourPosition = Hours * 5
    if HourPosition==60:
        HourPosition=0
    strip.setPixelColor(HourPosition, Color(255, 0, 0))
    strip.setPixelColor(Minutes, Color(0, 255, 0))
    strip.setPixelColor(Seconds, Color(0, 0, 255))
    #Intersections
    if Minutes==Seconds:
        strip.setPixelColor(Seconds, Color(0, 255, 255))
    if Seconds==HourPosition:
        strip.setPixelColor(Seconds, Color(255, 0, 255))
    if Minutes==HourPosition:
        strip.setPixelColor(Seconds, Color(255, 255, 0))
    if Seconds==HourPosition and Minutes==HourPosition:
        strip.setPixelColor(Seconds, Color(255, 255, 255))
    strip.show()
    
def FillDownRandom(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
    SetAll(strip, Color(0, 0, 0))
    #Fill down with random colors
    for i in range(0, LED_COUNT):
        r=random.randint(0, 255)
        g=random.randint(0, 255)
        b=random.randint(0, 255)
        for j in range(0,LED_COUNT-i):
            strip.setPixelColor(j, Color(r, g, b))
            if j>0:
                strip.setPixelColor(j-1, Color(0, 0, 0))
            strip.show()
            time.sleep(SpeedDelay)
        time.sleep(DisplayDelay)
    time.sleep(PauseDelay)
    #"Flush" results
    for i in range(LED_COUNT-1, -1, -1):
        for j in range(LED_COUNT-1, 0, -1):
            OldColor = strip.getPixelColor(j-1)
            strip.setPixelColor(j, OldColor)
        strip.setPixelColor(i-LED_COUNT+1, Color(0, 0, 0))
        strip.show()
        time.sleep(FlushDelay)
    time.sleep(PauseDelay)

def RandomColors(strip, SpeedDelay):
    SetAll(strip, Color(0, 0, 0))
    while True:
        for i in range(0, LED_COUNT):
            r=random.randint(0, 255)
            g=random.randint(0, 255)
            b=random.randint(0, 255)
            strip.setPixelColor(i, Color(r, g, b))
        strip.show()
        time.sleep(SpeedDelay)

"""
Done
"""
