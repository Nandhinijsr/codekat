p=int(input())
q=[]
for j in range(1,n+1):
    if(p%j==0):
        q.append(j)
print(*q)