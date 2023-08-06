import string

s = input()
alphabet = string.ascii_lowercase
l = sorted([e for e in alphabet if e not in s])

if len(l) == 0:
    print("None")
else:
    print(l[0])
