import sys

neighbours = [
    [2, 3],
    [3]]

rules = [lambda x, y: any([x == i for i in y]),
         ]


def check_neighbour(i, j, grid):
    count = 0
    up_down = [i - 1, i, i + 1]
    left_right = [j - 1, j, j + 1]
    for k in up_down:
        for m in left_right:
            if not (k == i and m == j) and (k >= 0 and m >= 0):
                try:
                    if grid[k][m] == '#':
                        count += 1
                except IndexError:
                    pass
    return count


def update_grid(x_list, y_list, grid, always_on=None):
    for j, i in enumerate(x_list):
        if grid[i][y_list[j]] == '#':
            grid[i][y_list[j]] = '.'
        else:
            grid[i][y_list[j]] = '#'

    if always_on is not None:
        for co in always_on:
            grid[co[0]][co[1]] = '#'
    return grid


def animate(grid, always_on=None):
    x_changes = []
    y_changes = []
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            count = check_neighbour(i, j, grid)
            if (grid[i][j] == '#' and not rules[0](count, neighbours[0])) or (
                    grid[i][j] == '.' and rules[0](count, neighbours[1])):
                x_changes.append(i)
                y_changes.append(j)

    return update_grid(x_changes, y_changes, grid, always_on)


def count_lights(grid):
    count = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == '#':
                count += 1
    return count


def print_grid(grid):
    for i in range(0, len(grid)):
        print(grid[i])


def main():

    lines = open(sys.argv[1], 'r').readlines()
    grid = [['' for _ in range(0, len(lines[0].strip('\n')))] for _ in range(0, len(lines))]
    for i, line in enumerate(lines):
        for j, c in enumerate(line.strip('\n')):
            grid[i][j] = c

    always_on = [[0, 0],
                 [0, len(grid[0]) - 1],
                 [len(grid) - 1, 0],
                 [len(grid) - 1, len(grid[0]) - 1]]

    new_grid = animate(grid, always_on)
    for i in range(1, 100):
        new_grid = animate(grid, always_on)

    print_grid(new_grid)
    print(count_lights(new_grid))

if __name__ == '__main__':
    main()
