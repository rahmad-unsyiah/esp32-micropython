from machine import Pin

# LED tersambung ke Pin 0.
led = Pin(0, Pin.OUT)
# Matikan LED
led.off()			

# S1 (A1) tersambung ke Pin 2.
button = Pin(2, Pin.IN)

# Infinite loop
while True:
    # Loop selaman S1 ditekan
    while button.value() == 1:
        # Hidupkan LED
        led.on()

    # S1 tidak ditekan matikan LED
    led.off()	
