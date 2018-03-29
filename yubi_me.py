#!/usr/bin/env python3

import string
import keyboard
from random import randrange

LETTERS = [c for c in string.ascii_lowercase]
NUMBERS = [str(n) for n in range(10)]
CHARS = LETTERS + NUMBERS
CHARS_LENGTH = len(CHARS)

CONFIG = {
    'min_len' : 40,
    'max_len' : 45,
    'has_upper' : False
}

def yubi():
    return _yubi_from_input(CHARS, CONFIG['min_len'], CONFIG['max_len'])

def yubi_letters():
    return _yubi_from_input(LETTERS, CONFIG['min_len'], CONFIG['max_len'])

def _yubi_from_input(src, min_length, max_length):
    yubi_str = ''
    length = randrange(min_length, max_length+1)
    src_length = len(src)
    for _ in range(length):
        char_index = randrange(0, src_length)
        yubi_str += src[char_index]
    return yubi_str

keyboard.add_hotkey('command+\\', lambda: keyboard.write(yubi_letters()))
while True:
    pass
