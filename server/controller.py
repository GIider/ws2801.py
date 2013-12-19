# -*- coding: utf-8 -*-
"""The main file to interact with the LED stripe"""
import array

import fcntl

__all__ = ['get_color', 'LedStripe']

NUL = chr(0)
SPI_IOC_WR_MAX_SPEED_HZ = 0x40046b04


def get_color(r, g, b):
    """Bitshift the red, green and blue components around to get the proper bits that represent that color"""
    return ((r & 0xFF) << 16) | ((g & 0xFF) << 8) | (b & 0xFF)


#noinspection PyTypeChecker
class LedStripe(object):
    """The LedStripe object that is used to interact"""

    def __init__(self, amount_of_leds):
        self.amount_of_leds = amount_of_leds
        self._leds = [0] * amount_of_leds

    # I am not really sure what this does yet :-)
    def set_speed(self, speed=400000):
        """Makes things faster, I guess?"""
        with open('/dev/spidev0.0', 'wb') as spidev:
            fcntl.ioctl(spidev, SPI_IOC_WR_MAX_SPEED_HZ, array.array('L', [speed]))

    def update(self):
        """Write the current state of the led stripe to the hardware"""
        with open('/dev/spidev0.0', 'wb') as spidev:
            for index, pixel in enumerate(self._leds):
                _bytes = chr((pixel >> 16) & 0xFF) + chr((pixel >> 8) & 0xFF) + chr(pixel & 0xFF)
                spidev.write(_bytes)

    def set_pixel_color(self, index, color):
        """Change the color of a single pixel"""
        self._leds[index] = color

    def set_all_pixels(self, hex_string):
        """Change the color of all pixels in the stripe

        Expects a hex string with the colors you want to display. Every LED has 6 digits, respectively 2 for each
        color component.

        Example: Turning the first LED red, the next one green and the third blue: FF000000FF000000FF
        """
        pixels_available = self.amount_of_leds

        hex_string = hex_string.ljust(pixels_available * 6, '0')
        for index in range(pixels_available):
            red = hex_string[index * 6: index * 6 + 2]
            green = hex_string[index * 6 + 2: index * 6 + 4]
            blue = hex_string[index * 6 + 4: index * 6 + 6]

            color = get_color(int(red, 16), int(green, 16), int(blue, 16))
            self.set_pixel_color(index, color)

    def turn_all_off(self):
        """Turn off all LEDs"""
        with open("/dev/spidev0.0", "wb") as spidev:
            darkness = (NUL + NUL + NUL) * self.amount_of_leds
            spidev.write(darkness)


if __name__ == '__main__':
    led_stripe = LedStripe(100)
    led_stripe.turn_all_off()