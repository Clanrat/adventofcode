import itertools
import math

weps = dict(Dagger=[8, 4, 0],
            Shortsword=[10, 5, 0],
            Warhammer=[25, 6, 0],
            Longsword=[40, 7, 0],
            Greataxe=[74, 8, 0])

arms = dict(none=[0, 0, 0],
            Leather=[13, 0, 1],
            Chainmail=[31, 0, 2],
            Splintmail=[53, 0, 3],
            Bandedmail=[75, 0, 4],
            Platedmail=[102, 0, 5])

rins = dict(none=[0, 0, 0],
            d1=[25, 1, 0],
            d2=[50, 2, 0],
            d3=[100, 3, 0],
            a1=[20, 0, 1],
            a2=[40, 0, 2],
            a3=[80, 0, 3])

bhp = 103
bdam = 9
barm = 2

rtk = lambda hp, dam, ar: hp / (dam - ar) if dam > ar else hp
costs_l = []
costs_d = []
for wep, w_s in weps.items():
    for arm, a_s in arms.items():
        for r1, r1_s in rins.items():
            for r2, r2_s in rins.items():
                if r1 != r2 or r2 == 'none':
                    t_c = w_s[0] + a_s[0] + r1_s[0] + r2_s[0]
                    t_d = w_s[1] + a_s[1] + r1_s[1] + r2_s[1]
                    t_a = w_s[2] + a_s[2] + r1_s[2] + r2_s[2]

                    rounds_to_kill = math.ceil(rtk(bhp, t_d, barm))
                    rounds_to_die = math.ceil(rtk(100, bdam, t_a))

                    if rounds_to_die >= rounds_to_kill:
                        costs_l.append(t_c)
                    if rounds_to_die < rounds_to_kill:
                        costs_d.append(t_c)
print(min(costs_l))
print(max(costs_d))
