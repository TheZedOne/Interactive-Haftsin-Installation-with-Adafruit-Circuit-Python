import time
import board
import array
import math
import digitalio
import adafruit_mpr121
import busio
import neopixel

pixel_pin = board.A3
num_pixels = 7
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1)
i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
purple = (76, 0, 153)
orange = (255, 128, 0)
black = (0, 0, 0)

while True:
    for i in range(12):
        if mpr121[i].value:
            print("Input {} touched!".format(i))
            if i == 0:
                pixels[0] = purple
                time.sleep(1)
                pixels[0] = black
            if i == 1:
                pixels[1] = purple
                time.sleep(1)
                pixels[1] = black
            if i == 5:
                pixels[2] = purple
                time.sleep(1)
                pixels[2] = black
            if i == 3:
                pixels[3] = purple
                time.sleep(1)
                pixels[3] = black
            if i == 9:
                pixels[4] = purple
                time.sleep(1)
                pixels[4] = black
            if i == 11:
                pixels[5] = purple
                time.sleep(1)
                pixels[5] = black
            if i == 7:
                pixels[6] = purple
                time.sleep(1)
                pixels[6] = black

    time.sleep(0.25)# Write your code here :-)


