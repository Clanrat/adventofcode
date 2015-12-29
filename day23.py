import sys


def get_instructions():
    instr = []
    inp = open(sys.argv[1], 'r').readlines()
    for line in inp:
        line = line.replace(',', '')
        line = line.strip('\n')
        line = line.split(' ')
        instr.append(line)
    return instr


regs = dict(
    a=0,
    b=0
)

avail_com = dict(
    hlf=lambda *args: (int(args[0] / 2), args[1] + 1),
    tpl=lambda *args: (args[0] * 3, args[1] + 1),
    inc=lambda *args: (args[0] + 1, args[1] + 1),
    jmp=lambda *args: (None, args[0] + args[1]),
    jie=lambda *args: (None, args[1] + args[2] if args[0] % 2 == 0 else args[1] + 1),
    jio=lambda *args: (None, args[1] + args[2] if args[0] == 1 else args[1] + 1)
)

i = 0
instructions = get_instructions()
while len(instructions) > i >= 0:
    c_i = instructions[i]
    com = avail_com[c_i[0]]
    if c_i[1] in regs:
        reg_val, i = com(regs[c_i[1]], i, int(c_i[2]) if len(c_i) > 2 else None)
        regs[c_i[1]] = reg_val if reg_val is not None else regs[c_i[1]]

    else:
        _, i = com(i, int(c_i[1]))

print(regs['a'])
print(regs['b'])
