import sys
import re


def run_circuit(c):
    return follow_wire('a', c)


def follow_wire(wire, c):
    """
    Follow the wire recursively until the values for the connections can be resolved then move up until all wires
    are evaluated
    :param wire:
    :param c:
    :return:
    """
    if all([w.isnumeric() for w in c[wire]['wires']]):  # All connections are numbers
        c[wire]['val'] = do_command(c[wire]['com'], [int(v) for v in c[wire]['wires']])
        return c
    if all(c[w]['val'] != -1 for w in c[wire]['wires'] if
           not w.isnumeric()):  # All connections have been evaluated or are numbers
        c[wire]['val'] = do_command(c[wire]['com'],
                                    [c[v]['val'] if (not v.isnumeric()) else int(v) for v in c[wire]['wires']])
        return c
    else:  # One or more of the connections haven't been evaluated
        for w in c[wire]['wires']:  # Evaluate unevaluated wires
            if not w.isnumeric() and c[w]['val'] == -1:
                c = follow_wire(w, c)

    return follow_wire(wire, c)  # Follow the last wire


def do_command(com, d):
    operators = {'AND': lambda x, y: x & y,
                 'OR': lambda x, y: x | y,
                 'RSHIFT': lambda x, y: x >> y,
                 'LSHIFT': lambda x, y: x << y,
                 'NOT': lambda x: ~x}

    if com == 'NOT':
        val = operators[com](d[0])
    elif com in operators:
        val = operators[com](d[0], d[1])
    else:
        val = d[0]

    return val & 0xffff


def get_circuit(**kwargs):
    """
    Create the circuit and evaluate it
    :param kwargs:
    :return:
    """

    f = open(sys.argv[1], 'r')
    lines = f.readlines()
    circuit = {}
    for line in lines:
        command = ''.join(re.findall(r'AND|OR|RSHIFT|LSHIFT|NOT', line))
        vals = re.findall(r'\d+|\w+', line)
        if command:
            vals.remove(command)

        if vals[-1] not in circuit:
            circuit[vals[-1]] = {'com': command, 'wires': [v for v in vals[0:(len(vals) - 1)] if v != command],
                                 'val': -1}
    if 'p2' in kwargs:  # Replace the value for b if it's for p2
        circuit['b']['wires'][0] = str(kwargs['p2'])
    circuit = run_circuit(circuit)
    return circuit['a']['val']


if __name__ == '__main__':
    p1_val = get_circuit()
    p2_val = get_circuit(p2=p1_val)
    print('Part 1: {}'.format(p1_val))
    print('Part 2: {}'.format(p2_val))
