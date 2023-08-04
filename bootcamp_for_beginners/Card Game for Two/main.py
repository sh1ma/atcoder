# coding: utf-8

_ = input()
s = list(map(int, input().split()))

r = sorted(s, reverse=True)

alice = r[0::2]
bob = r[1::2]

print(sum(alice) - sum(bob))
