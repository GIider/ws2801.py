ws2801.py
=========

Python toolkit to manipulate a LED stripe running the ws2801 driver from a Raspberry Pi

Requirements
============

SPI needs to be enabled on your Raspberry (If you don't know how to just google it) and your LED stripe needs to be
hooked up to the Raspberry.

Project Structure
=================

The *client* folder holds files relevant for manipulating the LED stripe attached to your Raspberry from another
machine.
The *server* folder holds the files that should be put on your Raspberry to modify the state of the LEDs.