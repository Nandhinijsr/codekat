p,q=[int(y) for y in input().split()]
for i in range(p,q):
    t = 0
    z = i
    while z > 0:
        c = z % 10
        t += c ** 3
        z //= 10

    if i == t:
        print(i)