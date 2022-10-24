# adc_ws2812_v2.py: reads the analogue value from the slider potentiometer
# connected to the ADC on pin 36 marked A0 on the ESP32 CPU board
# Depending on the value read from the slider, one of the LEDs on the
# RGB LED shield is selected. Prints slice number
# This version also lights the corresponding LED in green
# Copyright U. Raich 2022
# The program is part of the African School of Physics 2022

from machine import Pin, ADC
from neopixel import NeoPixel
from time import sleep_ms
NEOPIXEL_PIN = 26
ADC_PIN = 36
slider = ADC(Pin(ADC_PIN),atten=ADC.ATTN_11DB)  # create ADC object on ADC pin 36
neopixel = NeoPixel(Pin(NEOPIXEL_PIN),7)

# calculate the LED number depending on the slider value
def getLED(slider_val):
    s12 = slider_val
    # 4095 would start a new slice
    if s12 > 4094:
        s12 -= 1
    s12_div = s12 //585
    led = (s12_div + 1) % 7
    return s12,s12_div,led

green = (0,31,0)
dark = (0,0,0)

s12,s12_div,led = getLED(slider.read()) # read the slider and calculate the LED number
lastLED = led
# write the led found
print("s12: ", s12, "s12_div: ",s12_div,"led: ",led)
neopixel[led] = green
neopixel.write()

while True:
    s12,s12_div,led = getLED(slider.read())
    if led != lastLED:
        print("s12: ", s12, "s12_div: ",s12_div,"led: ",led)
        neopixel[lastLED] = dark
        neopixel.write() # switch of the previously lit LED
        neopixel[led] = green
        neopixel.write() # switch on the new led
        lastLED = led        
    sleep_ms(100)



