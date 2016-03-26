# -*- coding: utf-8-*-
import random
import re
import subprocess

WORDS = ["MUSIC", "PLAY", "BONKERS", "EIGHTEEN", "CD1", "CD2", "CD3", "ENBEEAR"]

PRIORITY = 9

def play(mic, name, path):
    mic.say("Playing %s" % name)
    path = path.replace(" ", "\\ ")
    cmd = ['/bin/bash', '-c', 'mplayer %s/*' % path]
    subprocess.Popen(cmd)

def searchsub(pattern, text):
    return bool(re.search(r'\b%s\b' % pattern, text, re.IGNORECASE))

def handle(text, mic, profile):
    tokens = text.split(' ')
    if bool(re.search(r'\bstop\b', text, re.IGNORECASE)):
        print "jjd27: stopping music\n"
        cmd = ['/usr/bin/killall', 'mplayer']
        subprocess.call(cmd)
    else:
        print "TEXT is %s\n" % text
        if searchsub('bonkers', text):
            play(mic, "Bonkers 18 CD1", "/mnt/campi-music/Bonkers 18 - The Original Hardcore/CD1 - Sharkey/")
        elif searchsub('enbeear', text):
            play(mic, "NBR CD3", "/mnt/campi-music/Natural Born Ravers 5/CD3 - Gammer")
        else:
            mic.say("Pardon?")

def isValid(text):
    return searchsub('music', text) or searchsub('play', text)
