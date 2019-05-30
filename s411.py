x=int(input())
p=[1,1]
if x<=len(p):
    print(*p[:x])
else:
    for j in range(2,x):
        r=p[j-1]+p[j-2]
        p.append(r)
    print(*p)