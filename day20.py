inp = 33100000
highest = 0
house = [0 for i in range(0, int(inp/10))]
for i in range(1, len(house)):
    for j in range(i, len(house)):
        house[j] += i * 10


for i, presents in enumerate(house):
    if presents >= inp:
        print(i)
        break