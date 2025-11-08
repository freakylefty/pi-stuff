#!/usr/bin/env python3
import sys
import tts

# Text to Speech
def say_text(msg):
    print("Saying " + msg)
    tts.say(msg)

if len(sys.argv) < 2:
    print("Usage: python3 main.py <text>")
else:
    say_text(sys.argv[1])
