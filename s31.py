N,A,D=[int(y) for y in input().split()]
p=q=a
for j in range(N-1):
    p=p+D
    q=q+p
print(q)