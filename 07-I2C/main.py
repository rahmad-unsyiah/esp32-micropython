from machine import Pin
from machine import SoftI2C
import time

# Pakai Pin G21 utk SDA
sda_pin = Pin(21)
# Pakai Pin G22 utk SCL
scl_pin = Pin(22)
# Buat konseksi I2C
i2c = SoftI2C(sda=sda_pin, scl=scl_pin)

# Berbagai konfigurasi
# 
# Atur kecepatan data yang dikeluarkan ke hanya 100Hz (0x2C) 
i2c.writeto_mem(0x53, 0x2C, b'\x0A')
# Ubah mode ke mengukur percepatan (0x2D)
i2c.writeto_mem(0x53, 0x2D, b'\x08')
# Matikan semua interrupt (0x2E)
i2c.writeto_mem(0x53, 0x2E, b'\x00')
# Ubah pembacaan ke max resolusi hanya 2g (0x31)
i2c.writeto_mem(0x53, 0x31, b'\x00')
# Tunggu sebentar untuk konfigurasi berubah, untuk jaga-jaga
time.sleep(0.1)

# Ambil data dari sensor (0x32), langsung 6 byte (X, Y, dan Z)
buff = i2c.readfrom_mem(0x53, 0x32, 6)

# Porsi X di byte 0 dan 1. Note: Format Litte-Endian.
x = (int(buff[1]) << 8) | buff[0]
if x > 32767:
    x -= 65536

# Porsi Y di byte 2 dan 3. Note: Format Litte-Endian.
y = (int(buff[3]) << 8) | buff[2]
if y > 32767:
    y -= 65536

# Porsi Z di byte 4 dan 5. Note: Format Litte-Endian.
z = (int(buff[5]) << 8) | buff[4]
if z > 32767:
    z -= 65536

# Note: 1 bit = 0.004*G. Dimana G adalah percepatan gravitas bumi (9.80665) 
x = x * 0.004 * 9.80665
y = y * 0.004 * 9.80665
z = z * 0.004 * 9.80665
