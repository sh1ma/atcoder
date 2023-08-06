n, m = map(int, input().split())
l = [tuple(map(int, input().split())) for _ in range(m)]
ls = [i[0] for i in l]
rs = [i[1] for i in l]
lsmax = max(ls)
rsmin = min(rs)

r = [i for i in range(1, n + 1) if i >= lsmax and i <= rsmin]
print(len(r))
