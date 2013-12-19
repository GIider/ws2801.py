# -*- coding: utf-8 -*-
import socket


class RemoteLedStripe(object):
    def __init__(self, host, port=26667):
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_hex_string(self, hex_string):
        """Send a hex string to the server to change the colors on the stripe"""
        self.socket.sendto(bytes(hex_string + "\n", "utf-8"), (self.host, self.port))