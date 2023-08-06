a, b = map(int, input().split())
s = input().split("-")

if len(s) == 2:
    if len(s[0]) == a and b == len(s[1]):
        print("Yes")
    else:
        print("No")
else:
    print("No")
