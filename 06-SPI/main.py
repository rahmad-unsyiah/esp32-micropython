from machine import Pin, SoftSPI

# Kode untuk tampilan angka pada 7-segment
SEVEN_SEGMENT_MAP = [0xC0,  # Angka 0
                     0xF9,  # Angka 1
                     0xA4,  # Angka 2
                     0xB0,  # Angka 3
                     0x99,  # Angka 4
                     0x92,  # Angka 5
                     0x82,  # Angka 6
                     0xF8,  # Angka 7
                     0X80,  # Angka 8
                     0X90]  # Angka 9
# Penentuan digit mana dari 7-segment
SEVEN_SEGMENT_DIGIT = [0xF1,    # Digit 1
                       0xF2,    # Digit 2
                       0xF4,    # Digit 3
                       0xF8]    # Digit 4


# Pin untuk informasikan shield akan kirim data 7-Segment, harus 0
cs = Pin(4, Pin.OUT)

# Komunikasi ke 7-Segment memakai SPI. Harus ada: CLOCK, MOSI, dan MISO.
# 
# Pin untuk clock untuk SPI.
spi_clock = Pin(16, Pin.OUT)
# Pin untuk pengiriman data dari Master ke Slave via SPI (MOSI).
spi_mosi = Pin(17, Pin.OUT)
# Pin untuk pengiriman data dari Slave ke Master via SPI (MISO).
spi_miso = Pin(5, Pin.IN)


def tampilkanSevenSegment(digit_ke, angka):
    # Buffer untuk kirim data
    # Byte pertama untuk tampilan 7-segment
    # Byte kedua untuk pilih 7-segment yang mana
    buf = bytearray(2)
    buf[0] = SEVEN_SEGMENT_MAP[angka]
    buf[1] = SEVEN_SEGMENT_DIGIT[digit_ke]

    # Inisiasi SPI
    spi = SoftSPI(sck=spi_clock, mosi=spi_mosi, miso=spi_miso)

    # Kirim data ke 7-segment memakai SPI
    cs.off()     # Infokan dulu akan kirim data
    spi.write(buf)          # Kirim data
    cs.on()      # Infokan pengiriman telah selesai

    # Deinisiasi SPI
    spi.deinit()

tampilkanSevenSegment(digit_ke=3, angka=6)
