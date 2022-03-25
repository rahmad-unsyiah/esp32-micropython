from machine import Pin
from machine import PWM
import time

# Jadikan Pin G0 sebagai PWM.
# Sementara jadikan 100% ON (atau 0% OFF)
led = PWM(Pin(0), duty_u16=65535)

# Infinite Loop
while True:
    # Dari gelap ke terang maksimum.
    # % OFF berkurang menuju 0% per 10 mikrodetik
    for duty_cycle in range(65535, 0, -1):
        led.duty_u16(duty_cycle)
        time.sleep_us(10)
    
    # Dari terang maksimum ke gelap.
    # % OFF bertambah menuju 100% (65535) per 10 mikrodetik
    for duty_cycle in range(0, 65535):
        led.duty_u16(duty_cycle)
        time.sleep_us(10)
