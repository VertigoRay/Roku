# https://github.com/jcarbaugh/python-roku
import numpy
import sys
import time

from roku import Roku

roku = Roku('192.168.1.214')
delay = .200
youtube_search_alpha = [
    ['A','B','C','D','E','F','G','{backspace}'],
    ['H','I','J','K','L','M','N','{num}'],
    ['O','P','Q','R','S','T','U'],
    ['V','W','X','Y','Z','-',"'"],
    [' ','{clear}','{search}'],
]
youtube_search_num = [
    ['1','2','3','&','#','(',')','{backspace}'],
    ['4','5','6','@','!','?',':','{alpha}'],
    ['7','8','9','0','.','_','"'],
    [' ','{clear}','{search}'],
]

def youtube_search_character(char):
    loc = next(((i, alpha.index(char))
        for i, alpha in enumerate(youtube_search_alpha)
        if char in alpha),
        None)
    
    if loc is None:
        loc = next(((i, num.index(char))
            for i, num in enumerate(youtube_search_num)
            if char in num),
            None)

        if loc is not None:
            loc = loc + youtube_search_character('{num}')
    
    return loc

def youtube_search(query):
    for char in list(query.upper()):
        print('char: %s' % char)
        loc = youtube_search_character(char)

        if (len(loc) > 2):
            print('numx: %s' % loc[3])
            print('numy: %s' % loc[2])

            for i in range(0, loc[3]):
                roku.right()
                time.sleep(delay)
            for i in range(0, loc[2]):
                roku.down()
                time.sleep(delay)
            roku.select()
            time.sleep(delay)

            for i in range(0, loc[3]):
                roku.left()
                time.sleep(delay)
            for i in range(0, loc[2]):
                roku.up()
                time.sleep(delay)

        print('x: %s' % loc[1])
        print('y: %s' % loc[0])

        for i in range(0, loc[1]):
            roku.right()
            time.sleep(delay)
        for i in range(0, loc[0]):
            roku.down()
            time.sleep(delay)
        roku.select()
        time.sleep(delay)

        for i in range(0, loc[1]):
            roku.left()
            time.sleep(delay)
        for i in range(0, loc[0]):
            roku.up()
            time.sleep(delay)

        if (len(loc) > 2):
            print('numx: %s' % loc[3])
            print('numy: %s' % loc[2])

            for i in range(0, loc[3]):
                roku.right()
                time.sleep(delay)
            for i in range(0, loc[2]):
                roku.down()
                time.sleep(delay)
            roku.select()
            time.sleep(delay)

            for i in range(0, loc[3]):
                roku.left()
                time.sleep(delay)
            for i in range(0, loc[2]):
                roku.up()
                time.sleep(delay)

roku.poweron()
time.sleep(3)

roku['YouTube'].launch()

for i in range(0, 100):
    roku.volume_down()

for i in range(0, 15):
    roku.volume_up()

time.sleep(10)

# Navigating YouTube App to search
roku.left()
time.sleep(delay)
roku.up()
time.sleep(delay)
roku.right()
time.sleep(delay)
roku.right()
time.sleep(delay)

if len(sys.argv) > 1:
    youtube_search(sys.argv[1])
else:
    youtube_search('fireplace jazz live')

# Typing done; select first video
for i in range(0, 5):
    roku.down()
    time.sleep(delay)
roku.select()