x=int(input())
p=input().split(' ')
q= [int(k) for k in p]
q.sort()
for k in range (x):
    print(q[k],end=" ")