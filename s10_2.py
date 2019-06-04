p=int(input())
q=list(map(int,input().split()))
x=0
for j in range(len(q)):
	x+=q[j]
print(x)