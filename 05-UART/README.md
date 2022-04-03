# Analogi Input

Atur terang LED memakai potensiometer.


### Perangkat

1. ESP32
2. [US-100 Ultrasonic Distance Sensor](https://www.adafruit.com/product/4019)


### Koneksi

1. GND ESP32 ke kedua GND
2. 5V ESP32 ke VCC
3. G10 ESP32 ke TX
4. G9 ESP32 ke RX
5. Jumper di US-100 terpasang

Note: 
* Biasanya TX ESP32 disambung ke RX dan RX ESP32 disambung ke TX.
* US-100 kebalikannya, TX ESP32 disambung ke TX dan RX ESP32 disambung ke RX.
* Jika jumper tidak terpasang maka akan bekerjsa sebagai HC-SR04


### Referensi

* https://github.com/adafruit/Adafruit_CircuitPython_US100
