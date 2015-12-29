import random


def mm(p, b):
    p['mana'] -= 53
    b['hp'] -= 4


def drain(p, b):
    p['mana'] -= 73
    p['hp'] += 2
    b['hp'] -= 2


def shield(p):
    p['mana'] -= 113
    p['a'] = 6


def poison(p, b):
    p['mana'] -= 173
    b['dot'] = 6


def recharge(p):
    p['mana'] -= 229
    p['r'] += 5


def dot(b):
    b['hp'] -= 3 if b['dot'] > 0 else 0
    b['dot'] -= 1 if b['dot'] > 0 else 0


def stat(p):
    tot_a = 7 if p['a'] > 0 else 0
    p['a'] -= 1 if p['a'] > 0 else 0
    p['mana'] += 101 if p['r'] > 0 else 0
    p['r'] -= 1 if p['r'] > 0 else 0
    return tot_a


def select_spell(sp, p, b):
    av_s = []
    for s, ef in sp.items():
        if ef[0] <= p['mana'] and not (s == 'Poison' and b['dot'] > 0) and not (s == 'Shield' and p['a'] > 0):
            av_s.append(s)

    return random.choice(av_s) if len(av_s) > 0 else 'none'


def combat(pl, bo, hard_mode=False):
    spent_mana = 0
    p_turn = True
    spells = dict(
        MM=[53, lambda p, b: mm(p, b)],
        Drain=[73, lambda p, b: drain(p, b)],
        Shield=[113, lambda p, b: shield(p)],
        Poison=[173, lambda p, b: poison(p, b)],
        Recharge=[229, lambda p, b: recharge(p)])

    while pl['hp'] > 0 and bo['hp'] > 0:
        dot(bo)
        arm = stat(pl)
        if bo['hp'] <= 0:
            break

        if p_turn:
            # Player turn
            if hard_mode:
                pl['hp'] -= 1

            if pl['hp'] <= 0:
                break

            spell = select_spell(spells, pl, bo)
            if spell in spells:
                spent_mana += spells[spell][0]
                spells[spell][1](pl, bo)

        else:
            # Boss turn
            pl['hp'] -= bo['dam'] - arm if arm < bo['dam'] else 1

        p_turn = not p_turn
    return spent_mana if pl['hp'] > 0 else 0


victories = []
sim_c = 0
while len(victories) < 1000:

    player = dict(hp=50, mana=500, a=0, r=0)
    boss = dict(hp=55, dam=8, dot=0)
    encounter = combat(player, boss, False)
    if encounter > 0:
        victories.append(encounter)
    sim_c += 1

print(min(victories))
print(sim_c)