# Analogi Input

Atur terang LED memakai potensiometer.


### Perangkat

1. ESP32
2. [Multifunction Shield](https://github.com/coderfls/Arduino_MultiFunctionShield)


### Koneksi

1. GND ESP32 ke GND Shield
2. 5V ESP32 ke 5V Shield
3. G0 ESP32 ke 13 shield
4. G1 ESP32 ke A0 shield

Note: 
* ADC ESP32 menerima masukan berupa voltase.
* Atur atenuasi ADC berdasarkan range voltase yang akan masu:

    * 0db untuk 100mV - 950mV
    * 2.5db untuk 100mV - 1250mV
    * 6dB  untuk 150mV  - 1750mV
    * 11dB untuk 150mV - 2450mV
