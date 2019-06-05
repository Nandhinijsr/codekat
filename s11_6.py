p,q=[int(j) for j in input().split()]
x=list(map(int,input().split()))
z=[]
for k in range(len(x)):
    if(x[k]%2)!=0:
        z.append(x[k])
print(z[q-1])