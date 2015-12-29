import sys
import re


class Ingredient:
    def __init__(self, nam, cap, dur, fla, tex, cal):
        self.nam = nam
        self.cap = cap
        self.dur = dur
        self.fla = fla
        self.tex = tex
        self.cal = cal


def gen_recipies(n, m):
    if n == 1:
        yield (m, )
    else:
        for i in range(0, m + 1):
            for j in gen_recipies(n - 1, m - i):
                yield (i, ) + j


def calc_val(ing, rec):


    cap = 0
    dur = 0
    fla = 0
    tex = 0
    cal = 0

    for i in range(0, len(rec)):
        cap += ing[i].cap * rec[i]
        dur += ing[i].dur * rec[i]
        fla += ing[i].fla * rec[i]
        tex += ing[i].tex * rec[i]
        cal += ing[i].cal * rec[i]

    return cap * dur * fla * tex if (not any(i < 0 for i in [cap, dur, fla, tex])) and cal == 500 else 0

def main():
    inp = open(sys.argv[1], 'r').readlines()
    ingred = []
    for line in inp:
        vals = re.findall(r'-?\d+', line)
        vals = [int(v) for v in vals]
        name = line.replace(',', '').split()[0]

        ingred.append(Ingredient(name, vals[0], vals[1], vals[2], vals[3], vals[4]))
    recp = list(gen_recipies(len(ingred), 100))
    scores = [calc_val(ingred, rec) for rec in recp]
    print(max(scores))
if __name__ == '__main__':
    main()
    62842880