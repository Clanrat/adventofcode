import sys
import re

f = open(sys.argv[1], 'r')
lines = f.readlines()
print(sum([len(line) - (len(line.decode('unicode_escape')) - 2) for line in
           [bytes(line.rstrip('\n'), 'utf8') for line in lines]]))
print(sum([len(re.escape(line)) - (len(line) - 2) for line in [bytes(line.rstrip('\n'), 'utf8') for line in lines]]))
