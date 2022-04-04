# I2C

Ambil datap percepatan dari ADXL-345.


### Perangkat

1. ESP32
2. [Multifunction Shield](https://github.com/coderfls/Arduino_MultiFunctionShield)


### Koneksi

1. GND ESP32 ke GND ADXL345
2. 3.3V ESP32 ke VCC ADXL345
3. G21 ESP32 ke SDA ADXL345
4. G22 ESP32 ke SCL ADXL345


### Referensi

* Halaman 23 dari datasheet (REGISTER MAP)
* Halaman 27 dari datasheet (Register 0x32 to Register 0x37) 
* https://github.com/DFRobot/micropython-dflib/blob/master/ADXL345/user_lib/ADXL345.py
* https://github.com/adafruit/Adafruit_CircuitPython_ADXL34x/blob/main/adafruit_adxl34x.py
