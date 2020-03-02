# https://github.com/jcarbaugh/python-roku
import time

from roku import Roku

roku = Roku('192.168.1.214')

roku.poweroff()