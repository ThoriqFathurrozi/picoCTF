from email import message
import string
from numpy import number
from pygame import NUMEVENTS

from sympy import content

u = string.ascii_uppercase
x = string.digits


with open("message.txt") as flip:
    content = flip.read()
    number = [int(val) for val in content.split()]

    print(number)

    flag = []
    mn = []

    for i in number:
        m = pow(i, -1, 41)
        mn.append(m)
        if m in range(1, 27):
            flag.append(u[m-1])
        elif m in range(27, 37):
            flag.append(x[m-27])
        else:
            flag.append("_")

print(mn)
print("picoCTF{%s}" % "".join(flag))
