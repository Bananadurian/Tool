#! /usr/bin/env python
from utils import get_device_state
from utils import screen_record

get_device_state()
time = ''
while not time:
    time = input('please enter recording time(s):')
screen_record(time)
if __name__=='__main__':
    input('Enter Pass')
