import sys
import itertools


def shortest(cities, dest):
    travel_plans = itertools.permutations(cities, len(cities))
    return [calc_distance(travel_plan, dest) for travel_plan in travel_plans]


def calc_distance(travel_plan, dest):
    distance = 0
    for i in range(1, len(travel_plan)):
        distance += int(dest[travel_plan[i - 1]][travel_plan[i]])
    return distance


def main():

    lines = open(sys.argv[1], 'r').readlines()
    dest = {}
    cities = []

    for line in lines:
        cp, distance = line.strip('\n').split(' = ')
        city1, city2 = cp.split(' to ')

        if city1 not in dest:
            dest[city1] = {}
            cities.append(city1)

        if city2 not in dest:
            dest[city2] = {}
            cities.append(city2)

        dest[city1][city2] = distance
        dest[city2][city1] = distance

    traveling_distances = shortest(cities, dest)
    print(min(traveling_distances))
    print(max(traveling_distances))

if __name__ == '__main__':
    main()

