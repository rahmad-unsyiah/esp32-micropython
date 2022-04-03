import time
from machine import UART

# Pakai UART 1, dimana TX pada G10 dan RX pada pim 9
uart = UART(1, baudrate=9600, tx=10, rx=9)
uart.init()

# Minta diukur
uart.write(b'\x55')
# Tunggu sebentar untuk diukur, 1ms cukup
time.sleep(0.1)
# Baca hasil pengukuran
hasil = uart.read(2)

# Konversi bacaan ke milimeter
hasil = hasil[1] + (hasil[0] << 8)

# Tampilkan hasil bacaan
print(hasil)
