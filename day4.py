import hashlib

key = "bgvyzdsv"
p2 = False

number = 1


s_w = '00000'
if p2:
    s_w = '000000'


while True:
    if hashlib.md5(bytes(key + str(number), 'utf-8')).hexdigest().startswith(s_w):
        print(number)
        break
    number += 1
