# -*- coding: utf-8 -*-
"""Small UDP client to set the colors of a remote LED stripe"""
import socket

__all__ = ['RemoteLedStripe']


class RemoteLedStripe(object):
    """A client to pass hex strings to a LED Stripe UDP server"""

    def __init__(self, host, port=26667):
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_hex_string(self, hex_string):
        """Send a hex string to the server to change the colors on the stripe"""
        self.socket.sendto(('%s\n' % hex_string).encode('ascii'), (self.host, self.port))