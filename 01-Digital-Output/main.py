from machine import Pin
import time

 # Jadikan pin G0 sebagai output.
 # Tersambung ke LED D1 dari shield melalui pin 13.
 # Jika G0 ON maka LED akan hidup, jika OFF maka LED akan mati.
led = Pin(0, Pin.OUT)

# Hidupkan LED selama 0.5 detik dan matikan selama 0.5 detik.
# Ulangi selama-lamanya (infinite loop).
while True:
	# Hidupkan LED
	led.on()

	# Tunggu 0.5 detik
	time.sleep_ms(500)

	# Matikan LED
	led.off()

	# Tunggu 0.5 detik
	time.sleep_ms(500)
