from machine import Pin
from machine import PWM
from machine import ADC

# Jadikan Pin 0 sebagai PWM. 
# Matikan LED, 100% OFF
led = PWM(Pin(0), duty_u16=65535)

# VR (A0) tersambung ke Pin 34.
vr_pin = Pin(34)

# Karena VR adalah analog maka harus disambungkan ke ADC terlebih dahulu agar bisa dibaca.
# Note: Tidak semua pin ESP32 ada ADC.
vr = ADC(vr_pin)
# Atur atenuasi sesuai range voltase yang akan dibaca.
# Atenuasi 11db untuk 150mV s/d 2450mv.
vr.atten(ADC.ATTN_11DB)

# Infinite loop
while True:
    # Akan hasilkan bacaan dari 0 s/d 65535, bisa langsung dijadikan duty cycle.
    duty_cycle = vr.read_u16()
    led.duty_u16(duty_cycle)
