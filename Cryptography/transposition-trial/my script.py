
with open("message.txt") as flip:
    contents = flip.read()

flag = []

for i in range(0, len(contents), 3):
    block = contents[i:i+3]
    a, b, c = block
    flag.append(c + a + b)

print("".join(flag))
