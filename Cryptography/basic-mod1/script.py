
import string

u = string.ascii_uppercase
x = string.digits


a = [202, 137, 390, 235, 114, 369, 198, 110, 350, 396, 390,
     383, 225, 258, 38, 291, 75, 324, 401, 142, 288, 397, ]

flag = []

for i in a:
    b = i % 37

    if b in range(26):
        flag.append(u[b])
    elif b in range(26, 36):
        flag.append(x[b-26])
    else:
        flag.append("_")

print("picoCTF{"+"".join(flag)+"}")
