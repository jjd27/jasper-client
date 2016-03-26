# -*- coding: utf-8-*-
import random
import re
import subprocess

WORDS = ["RADIO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SOLENT", "STOP"]

PRIORITY = 10

def searchsub(pattern, text):
    return bool(re.search(r'\b%s\b' % pattern, text, re.IGNORECASE))

def stopAll():
    print "jjd27: stopping radio\n"
    cmd = ['/usr/bin/killall', 'mplayer']
    subprocess.call(cmd)

def play(mic, station):
    stopAll()
    mic.say("Playing radio %s" % station)
    cmd = ['/home/pi/bbcradio.sh', station]
    subprocess.Popen(cmd)
    print "Invoked"

def handle(text, mic, profile):
    tokens = text.split(' ')
    if searchsub('stop', text):
        stopAll()
    else:
        print "TEXT is %s\n" % text
        if searchsub('one', text):
            play(mic, '1')
        elif searchsub('two', text):
            play(mic, '2')
        elif searchsub('three', text):
            play(mic, '3')
        elif searchsub('four', text):
            play(mic, '4')
        elif searchsub('five', text):
            play(mic, '5')
        elif searchsub('solent', text):
            play(mic, 'solent')

def isValid(text):
    return searchsub('radio', text)
