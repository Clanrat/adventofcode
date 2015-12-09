import sys
import re
lines = open(sys.argv[1], 'r').readlines()
#lines = ['turn on 0,0 through 999,999', 'turn off 0,0 through 999,999']
# Part 1
grid = [[False for x in range(0, 1000)] for x in range(0, 1000)]
b_grid = [[0 for x in range(0, 1000)] for x in range(0, 1000)]
total_brightness = 0
for line in lines:
    ranges = [int(x) for x in re.findall(r'\d+', line)]

    for i in range(ranges[0], ranges[2] + 1):
        for j in range(ranges[1], ranges[3] + 1):
            if 'on' in line:
                grid[i][j] = True
                b_grid[i][j] += 1
                total_brightness += 1
            if 'off' in line:
                grid[i][j] = False
                total_brightness -= 1 if b_grid[i][j] != 0 else 0
                b_grid[i][j] -= 1 if b_grid[i][j] != 0 else 0
            if 'toggle' in line:
                grid[i][j] = not grid[i][j]
                b_grid[i][j] += 2
                total_brightness += 2


light_count = 0
for i in range(0, 1000):
    light_count += grid[i].count(True)

print(light_count)
print(total_brightness)

