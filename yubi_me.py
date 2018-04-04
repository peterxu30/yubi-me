#!/usr/bin/env python3

import string, keyboard, platform
from random import randrange

LETTERS = [c for c in string.ascii_lowercase]

CONFIG = {
    'min_len' : 40,
    'max_len' : 45
}


def yubi():
    return _yubi_from_input(LETTERS, CONFIG['min_len'], CONFIG['max_len'])

def _yubi_from_input(src, min_length, max_length):
    yubi_str = ''
    length = randrange(min_length, max_length+1)
    src_length = len(src)
    for _ in range(length):
        char_index = randrange(0, src_length)
        yubi_str += src[char_index]
    return yubi_str


_hotkey = 'alt+\\'
if platform.system() == 'Darwin':
    _hotkey = 'windows+\\'

keyboard.add_hotkey(_hotkey, lambda: keyboard.write(yubi()))

if __name__ == '__main__':
    closeInput = input("Press " + _hotkey + " to hit 'em with the Yubi." + "\nPress ENTER to exit")
    print("Closing...")
