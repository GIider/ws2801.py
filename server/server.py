# -*- coding: utf-8 -*-
"""Small socket server to interact with the led stripe from a remote client

This should be called with the amount of leds in the stripe as argument. It will then start up a server
that listens for UDP packets on port 26667, expecting them to hold a hex string to pass to the LED stripe.
"""
import sys

try:
    import SocketServer as socketserver
except ImportError:
    import socketserver

from controller import LedStripe

__all__ = ['HexLedStripeUDPHandler']


class HexLedStripeUDPHandler(socketserver.BaseRequestHandler):
    """A server that accepts hex strings to change the local LED stripe"""
    __slots__ = 'stripe'

    def handle(self):
        data = self.request[0].strip()

        stripe = self.server.stripe

        stripe.set_all_pixels(data)
        stripe.update()


if __name__ == "__main__":
    HOST, PORT = "", 26667

    num_leds = int(sys.argv[1])

    server = socketserver.UDPServer((HOST, PORT), HexLedStripeUDPHandler)
    server.stripe = LedStripe(num_leds)

    print('Now serving on port %d' % PORT)
    server.serve_forever()
