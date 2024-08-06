#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 18:04:49 2024

@author: kchitran810
"""

import sys
from time import sleep

def print_lyrics():
    lyrics = [
        
        ("Notice me", 0.12, 3),
        ("Take my hand", 0.12, 3),
        ("Why are we", 0.12, 3),
        ("Strangers when", 0.12, 2),
        ("Our love is strong?", 0.12, 2),
        ("Why carry on without me?", 0.12, 1),
        ("And every time I try to fly I fall", 0.1, 1),
        ("Without my wings", 0.12, 0.7),
        ("I feel so small", 0.10, 1),
        ("I guess I need you baby", 0.10, 0.7),
        ("And every time I see you in my dreams", 0.10, 0.8),
        ("I see your face", 0.1, 0.8),
        ("It's haunting me", 0.1, 0.8),
        ("I guess I need you baby", 0.1, 11),
        ("I make-believe", 0.12, 2),
        ("That you are here", 0.12, 2),
        ("It's the only way", 0.12, 2),
        ("That I see clear", 0.12, 2),
        ("What have I done?", 0.12, 2),
        ("You seem to move on easy", 0.12, 2.5),
        ("And every time I try to fly I fall", 0.1, 1),
        ("Without my wings", 0.12, 0.7),
        ("I feel so small", 0.10, 1),
        ("I guess I need you baby", 0.10, 0.7),
        ("And every time I see you in my dreams", 0.10, 0.8),
        ("I see your face", 0.1, 0.8),
        ("You're haunting me", 0.1, 0.8),
        ("I guess I need you baby", 0.1, 2.3),
        ("I may have made it rain", 0.12, 1.8),
        ("Please forgive me", 0.10, 1.5),
        ("My weakness caused you pain", 0.12, 1.3),
        ("And this song's my sorry", 0.12, 23),
        ("At night I pray", 0.12, 1.8),
        ("That soon your face will fade away", 0.12, 0.8),
        ("And every time I try to fly I fall", 0.1, 0.5),
        ("Without my wings", 0.12, 0.5),
        ("I feel so small", 0.10, 1),
        ("I guess I need you baby", 0.1, 0.9),
        ("And every time I see you in my dreams", 0.12, 0.5),
        ("I see your face", 0.1, 0.5),
        ("You're haunting me", 0.1, 0.5),
        ("I guess I need you baby", 0.1, 0.8)
    ]

    for line, char_delay, line_delay in lyrics:
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        print()
        sleep(line_delay)

print_lyrics()