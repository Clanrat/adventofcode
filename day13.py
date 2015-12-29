import sys
import itertools


def seating_arrangements(people, pref):
    seating = itertools.permutations(people, len(people))
    return [happiness(s, pref) for s in seating]


def happiness(people, pref):
    happy = 0
    for pos, person in enumerate(people):
        if pos == 0:
            change = pref[person][people[pos + 1]] + pref[person][people[-1]]
        elif pos == len(people) - 1:
            change = pref[person][people[pos - 1]] + pref[person][people[0]]
        else:
            change = pref[person][people[pos + 1]] + pref[person][people[pos - 1]]
        happy += change
    return happy


def main():
    people = []
    pref = {}

    inp = open(sys.argv[1], 'r').readlines()
    for line in inp:
        line = line.strip('.').split()
        p1 = line[0]
        p2 = line[-1].strip('.')
        change = sum([int(c) for c in line if c.isnumeric()])

        if p1 not in pref:
            people.append(p1)
            pref[p1] = {}
        if not "gain" in line:
            change *= -1

        pref[p1][p2] = change

    print(pref)

    # part 1
    print(max(seating_arrangements(people, pref)))

    # part 2
    people.append('me')
    pref['me'] = {}
    for p in people:
        if p != 'me':
            pref['me'][p] = 0
            pref[p]['me'] = 0

    print(max(seating_arrangements(people, pref)))

if __name__ == '__main__':
    main()