import re

excluded_letters = ['i', 'o', 'l']

requirements = [lambda p: not any(c in excluded_letters for c in p),
                lambda p: re.findall(r"([a-z])\1.*([a-z])\2", p),
                lambda p: find_straight(p)]

def find_straight(password):
    last_c = password[0]
    count = 1
    exists = False

    for c in password[1:]:
        if count == 3:
            exists = True
            break
        if c == chr(ord(last_c) + 1):
            count += 1
        else:
            count = 1
        last_c = c

    return exists


def next_pass(i, old_password, new_password):
    if old_password[::-1][i] == 'z':
        if abs(i) != len(old_password) - 1:
            return next_pass(i + 1, old_password, 'a' + new_password)
        else:
            return 'a' + 'a' + new_password
    else:
        return old_password[:(len(old_password) - 1) - i] + chr(ord(old_password[::-1][i]) + 1) + new_password


def check_pass(password):
    valid = False
    if all(req(password) for req in requirements):
        valid = True
    return valid




if __name__ == '__main__':
    old_pass = 'hepxcrrq'
    new_pass = next_pass(0, old_pass, "")
    while not check_pass(new_pass):
        new_pass = next_pass(0, new_pass, "")
    # Part 1

    print("\n" + new_pass + "\n")
    # Part 2
    new_pass = next_pass(0, new_pass, "")
    while not check_pass(new_pass):
        new_pass = next_pass(0, new_pass, "")
    print(new_pass)

