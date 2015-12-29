import re
import sys
import json


inp = open(sys.argv[1], 'r').read()
# p1
print(sum(map(int, re.findall(r'-?[0-9]+', inp))))

# p2


def json_hook(obj):
    if "red" in obj.values():
        return {}
    else:
        return obj

red_rem = str(json.loads(inp, object_hook=json_hook))
print(sum(map(int, re.findall(r'-?[0-9]+', red_rem))))

