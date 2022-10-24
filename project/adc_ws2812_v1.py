# adc_ws2812_v1.py: reads the analogue value from the slider potentiometer
# connected to the ADC on pin 36 marked A0 on the ESP32 CPU board
# Depending on the value read from the slider, one of the LEDs on the
# RGB LED shield is selected. Prints slice number
# Copyright U. Raich 2022
# The program is part of the African School of Physics 2022

from machine import Pin, ADC
from time import sleep_ms
ADC_PIN = 36
slider = ADC(Pin(ADC_PIN),atten=ADC.ATTN_11DB)  # create ADC object on ADC pin 36

while True:
    s12 = slider.read()
    if s12 > 4094:
        s12 -= 1  
    s12_div = s12 // 585
       # 4095 would start a new slice
    led = (s12_div + 1) % 7
    print("s12: ", s12, "s12_div: ",s12_div,"led: ",led)
    sleep_ms(100)



