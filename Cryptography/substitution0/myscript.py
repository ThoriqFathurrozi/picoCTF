#!/usr/bin/env python3

from curses.ascii import islower, isupper
import string
from turtle import position

from certifi import contents

with open("message.txt") as flip:
    contents = flip .read()

uppercase_key = "VOUHMJLTESZCDKWIXNQYFAPGBR"
lowercase_key = uppercase_key.lower()

flag = []

for char in contents:
    if char.isupper():
        position = uppercase_key.index(char)
        flag.append(string.ascii_uppercase[position])
    elif char.islower():
        position = lowercase_key.index(char)
        flag.append(string.ascii_lowercase[position])
    else:
        flag.append(char)

flag = "".join(flag)
print(flag.split()[-1])
