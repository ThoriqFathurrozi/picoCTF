from curses.ascii import islower
import string

with open("message.txt") as flip:
    contents = flip.read()

flag = []

for char in contents:
    x = char.lower()
