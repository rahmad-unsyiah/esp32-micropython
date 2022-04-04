# SPI

Tampilkan angka pada 7-Segment.


### Perangkat

1. ESP32
2. [Multifunction Shield](https://github.com/coderfls/Arduino_MultiFunctionShield)


### Koneksi

1. GND ESP32 ke GND Shield
2. 5V ESP32 ke 5V Shield
3. G4 ESP32 ke 4 (CS 7-Segment) shield
4. G16 ESP32 ke 7 (SPI Clock) shield
5. G17 ESP32 ke 8 (SPI MOSI) shield

Note:
* CS aktif low. 
* G5 ESP32 ditetapkan sebagai SPI MISO tetapi tidak dipakai.

### Referensi

* Halaman 27 di hackatronics-arduino-multi-function-shield.pdf
