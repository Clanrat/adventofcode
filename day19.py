import sys
import re
import random


rep_skeleton = lambda x, y: (lambda z: y if z == x else z)
op = []
rev_op = {}
inp = open(sys.argv[1], 'r').readlines()


def synthesize(mol_str, rev_op):
    st = 0
    old_mol = ''
    keys = list(rev_op.keys())
    random.shuffle(keys)
    while old_mol != mol_str:
        old_mol = mol_str
        for key in keys:
            while key in mol_str:
                st += mol_str.count(key)
                mol_str = mol_str.replace(key, rev_op[key])

    return st if mol_str == 'e' else 0


for line in inp:
    try:
        l, r = line.strip('\n').split(' => ')

        rev_op[r] = l

        op.append(rep_skeleton(l, r))
    except ValueError:
        if line != '\n':
            molstr = line.strip()
            molecule = re.findall(r'[A-Z][^A-Z]*', line)


unique_molecules = set()

for o in op:
    for i, atom in enumerate(molecule):
        if atom != o(atom):
            molecule[i] = o(atom)
            unique_molecules.add(''.join(molecule))
            molecule[i] = atom


print(len(unique_molecules))

steps = 0
while steps == 0:
    steps = synthesize(molstr, rev_op)
print(steps)

