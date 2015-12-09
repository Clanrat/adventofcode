import re
import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()
print(len([s for s in lines if (re.search(r'(\w)\1+', s) and re.search(r'([aeiou](?i).*){3,}', s) and not
            re.search(r'ab|cd|pq|xy', s))]))
print(len([s for s in lines if (re.search(r'(\w\w).*\1+', s) and re.search(r'(\w).\1+', s))]))
