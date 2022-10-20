# adc_ws2812.py: reads the analogue value from the slider potentiometer
# connected to the ADC on pin 36 marked A0 on the ESP32 CPU board
# Depending on the value read from the slider, one of the LEDs on the
# RGB LED shield is lit. The color changes from blue (lowest ADC value) to
# white (highest ADC value). The first LED to be lit (lowest value) is the top
# one. The following ones follow in clockwise direction. The LED for the highest
# value is the middle one.
# Copyright U. Raich 2022
# The program is part of the African School of Physics 2022

from machine import Pin, ADC
from neopixel import NeoPixel
from time import sleep_ms
NEOPIXEL_PIN = 26
ADC_PIN = 36
slider = ADC(Pin(ADC_PIN),atten=ADC.ATTN_11DB)  # create ADC object on ADC pin 36
neopixel = NeoPixel(Pin(NEOPIXEL_PIN),7)
colors = [(0x1f, 0x1f, 0x1f), # white
          (0x00, 0x00, 0x1f), # blue
          (0x00, 0x1f, 0x1f), # cyan
          (0x00, 0x1f, 0x00), # green
          (0x1f, 0x1f, 0x00), # yellow
          (0x1f, 0x00, 0x1f), # magenta
          (0x1f, 0x00, 0x00)] # red

dark = (0,0,0)

while True:
    s12 = slider.read()
    if s12 > 4094:
        s12 -= 1  
    s12_div = s12 // 585
       # 4095 would start a new slice
    led = (s12_div + 1) % 7
    
    print("s12: ", s12, "s12_div: ",s12_div,"led: ",led)
    # light the LED with the corresponding color

    neopixel[led] = colors[led]
    neopixel.write()
    sleep_ms(500)
    neopixel[led] = dark
    neopixel.write()

