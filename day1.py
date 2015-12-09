import sys


f = open(sys.argv[1], 'r')
s = f.read()

floor = 0
i = 1
for c in s:
    if c == '(':
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(i)
    i += 1
print(floor)
