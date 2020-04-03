#!/usr/bin/env python
#
# This is the library for Grove Base Hat which used to connect grove sensors for raspberry pi.
# We use python module smbus2 instead of smbus.
#
'''
## License

The MIT License (MIT)

Grove Base Hat for the Raspberry Pi, used to connect grove sensors.
Copyright (C) 2018  Seeed Technology Co.,Ltd. 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
import spidev
from grove.gpio import GPIO
rev_to_bus = {
    1 : [0,0],
    2 : [0,0],
    3 : [0,0],
    'NPi_i_MX6ULL' : [2,0]
}
class SPI:
    instance = None
    bus = None
    device = None
    def __init__(self):
        rev = GPIO.RPI_REVISION
        self.bus = rev_to_bus[rev][0]
        self.device = rev_to_bus[rev][1]
        if not self.instance:
            self.instance = spidev.SpiDev()
    def __getattr__(self, name):
        return getattr(self.instance, name)
def main():
    # https://github.com/doceme/py-spidev
    spi = SPI()
    spi.open(spi.bus, spi.device)
    spi.max_speed_hz = 5000
    spi.mode = 0b01
    to_send = [0x01, 0x02, 0x03]
    spi.xfer(to_send)
    spi.close()
if __name__ == "__main__":
    main()