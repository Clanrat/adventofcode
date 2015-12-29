import sys


class Reindeer:
    def __init__(self, name,speed, stam, rest):

        self.name = name
        self.speed = speed
        self.stam = stam
        self.rest = rest
        self.resting = False
        self.run_time = 0
        self.rest_time = 0
        self.distance = 0
        self.points = 0

    def run(self):
        if not self.resting:
            self.run_time += 1
            self.distance += self.speed
            if self.run_time % self.stam == 0:
                self.resting = True
                self.run_time = 0
        else:
            self.rest_time += 1
            if self.rest_time % self.rest == 0:
                self.resting = False
                self.rest_time = 0


def check_lead(r):
    leading = []
    furthest = 0
    for c_r in r:
        if c_r.distance == furthest:
            leading.append(c_r)
        elif c_r.distance > furthest:
            leading = [c_r]
            furthest = c_r.distance

    for c_r in leading:
        c_r.points += 1


def main():
    inp = open(sys.argv[1], 'r').readlines()

    r = []
    for line in inp:
        line = line.split()

        curr_reind = line[0]
        stats = [int(s) for s in line if s.isnumeric()]
        r.append(Reindeer(curr_reind, stats[0], stats[1], stats[2]))

    for r_t in range(1, 2503 + 1):
        for c_r in r:
            c_r.run()
        check_lead(r)


    print(max([c_r.distance for c_r in r]))
    print(max([c_r.points for c_r in r]))

if __name__ == '__main__':
    main()
