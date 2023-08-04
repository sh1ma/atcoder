h = int(input())


def attack(n):
    if n == 1:
        return 1
    return attack(n // 2) * 2 + 1


print(attack(h))
