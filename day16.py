import sys
import re

aunt_sue = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

encabulator = {
    'trees': lambda x, y: x > y,
    'cats': lambda x, y: x > y,
    'pomeranians': lambda x, y: x < y,
    'goldfish': lambda x, y: x < y
}


def match_aunt(aunt):
    matches = []
    for key in aunt:
        if aunt[key] == aunt_sue[key] and key not in encabulator:
            matches.append(True)
        elif key in encabulator:
            if encabulator[key](aunt[key], aunt_sue[key]):
                matches.append(True)

    return matches


inp = open(sys.argv[1], 'r').readlines()
best_match = 0
best_match_index = 0

for i, line in enumerate(inp):
    sue = {}
    line = re.split(r"Sue \d: |:|, ", line.strip('\n'))
    line.pop(0)
    for j in range(0, len(line), 2):
        sue[line[j].strip()] = int(line[j + 1].strip())
    aunt_len = len(match_aunt(sue))
    if aunt_len > best_match:
        best_match = aunt_len
        best_match_index = i

print(best_match_index + 1)


