# @author : Salih Eren Değirmenci
# 12.05.2020
#Basic python console app for cooler device that can be controlled remotely. Device has a user authentication, and operatable database. Currently there is no device connected to it so temperature data created randomly.

from Handler import *

hndlr = Handler()

hndlr.DeviceMenu()
