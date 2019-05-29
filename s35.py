x=int(input())
p=input().split(' ')
q=[int(j) for j in p]
q.sort()
x=int(x/2)
print(q[x])