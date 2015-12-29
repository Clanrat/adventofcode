import sys
from itertools import groupby


def change(string):
    new_string = []
    for c, i in groupby(string):
        new_string.append(str(len(list(i))))
        new_string.append(c)
    return "".join(new_string)



string = open(sys.argv[1], 'r').read()
for i in range(0,50):
    string = change(string)

print(len(string))
