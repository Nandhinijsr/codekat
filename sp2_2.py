s,t=map(int,input().split())
z=list(map(int,input().split()))
for j in range(0,t):
    z=[z[-1]]+z[:-1]
print(*z,end=' ')