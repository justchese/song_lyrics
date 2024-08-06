#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 18:10:31 2024

@author: kchitran810
"""

import sys
from time import sleep

def print_lyrics():
    lyrics = [
        ("I want you to stay", 0.06, 3),
        ("'Til I'm in the grave", 0.06, 3),
        ("'Til I rot away, dead and buried", 0.09, 2),
        ("'Til I'm in the casket you carry", 0.09, 1),
        ("If you go, I'm going too, uh", 0.06, 3),
        ("'Cause it was always you, alright", 0.06, 2),
        ("And if I'm turning blue, please don't save me", 0.09, 0.6),
        ("Nothing left to lose without my baby", 0.09, 1.9),
        
        ("Birds of a feather, we should stick together, I know", 0.08, 0.5),
        ("I said I'd never think I wasn't better alone", 0.08, 0.5),
        ("Can't change the weather, might not be forever", 0.08, 1),
        ("But if it's forever", 0.08, 0.5),
        ("It's even better", 0.08, 0.5),
        
        ("And I don't know what I'm crying for", 0.1, 1.5),
        ("I don't think I could love you more", 0.1, 1),
        ("It might not be long, but baby, I", 0.10, 1),
        ("I'll love you 'til the day that I die", 0.10, 2),
        ("'Til the day that I die", 0.1, 2),
        ("'Til the light leaves my eyes", 0.1, 2),
        ("'Til the day that I die", 0.1, 3),
           
        ("I want you to see, hm", 0.06, 3),
        ("How you look to me, hm", 0.06, 3),
        ("You wouldn't believe if I told ya", 0.09, 1),
        ("You would keep the compliments I throw ya", 0.09, 1),
        ("But you're so full of shit, uh", 0.06, 3),
        ("Tell me it's a bit, oh", 0.06, 2),
        ("Say you don't see it, your mind's polluted", 0.09, 0.6),
        ("Say you wanna quit, don't be stupid", 0.09, 1.9),
        
        ("And I don't know what I'm crying for", 0.1, 1.5),
        ("I don't think I could love you more", 0.1, 1),
        ("Might not be long, but baby, I", 0.10, 1),
        ("Don't wanna say goodbye", 0.1, 2),
        
        ("Birds of a feather, we should stick together, I know", 0.08, 0.5),
        ("I said I'd never think I wasn't better alone", 0.08, 0.5),
        ("Can't change the weather, might not be forever", 0.08, 1),
        ("But if it's forever", 0.08, 0.5),
        ("It's even better", 0.08, 0.5),

        ("I knew you in another life", 0.1, 2),
        ("You had that same look in your eyes", 0.1, 1.5),
        ("I love you, don't act so surprised", 0.1, 2),
    ]

    for line, char_delay, line_delay in lyrics:
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        print()
        sleep(line_delay)

print_lyrics()
