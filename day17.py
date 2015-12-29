import sys
import itertools



containers = []
for line in open(sys.argv[1], 'r').readlines():
    containers.append(int(line))

count = 0
min_no_cont = len(containers)
n = 0
for i in range(1, len(containers)):
    for comb in itertools.combinations(containers, i):
        if sum(comb) == 150:
            count += 1
            if len(comb) == min_no_cont:
                n += 1
            elif len(comb) < min_no_cont:
                min_no_cont = len(comb)
                n = 1
print(count)
print(n)

