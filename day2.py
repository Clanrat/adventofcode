import sys

f = open(sys.argv[1], 'r')

lines = f.readlines()
wra_paper = 0
ribbon = 0
for line in lines:
    dim = line.split('x')
    dim = [int(x) for x in dim]
    dim.sort()
    wra_paper += 2 * dim[0] * dim[1] + 2 * dim[1] * dim[2] + 2 * dim[2] * dim[0] + dim[0] * dim[1]
    ribbon += 2 * dim[0] + 2 * dim[1] + dim[0] * dim[1] * dim[2]

print(wra_paper)
print(ribbon)
