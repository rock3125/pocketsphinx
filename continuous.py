#!/usr/bin/env python

from pocketsphinx import LiveSpeech

for phrase in LiveSpeech():
    print(phrase)

