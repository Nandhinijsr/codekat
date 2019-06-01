p=int(input())
q=0
r=list(map(int,input().split()))
for j in range(p):
    q=q+r[j]
print(q//p)