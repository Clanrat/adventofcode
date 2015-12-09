import sys


def move(c, x, y):
    if c == '^':
        y -= 1
    elif c == 'v':
        y += 1
    elif c == '>':
        x += 1
    elif c == '<':
        x -= 1

    return x, y

f = open(sys.argv[1], 'r')
lines = f.read()

x_santa = 0
y_santa = 0

x_robo = 0
y_robo = 0

presents = set()
presents.add((0, 0))

part2 = True
santa = True
for c in lines:
    if (santa and part2) or not part2:
        x_santa, y_santa = move(c, x_santa, y_santa)
        presents.add((x_santa, y_santa))

    else:
        x_robo, y_robo = move(c, x_robo, y_robo)
        presents.add((x_robo, y_robo))

    santa = not santa

print(len(presents))
