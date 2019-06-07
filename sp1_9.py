s,t=map(int,input().split())
u = list()
for j in range(s,t+1):
	y=0
	for k in range(1,j+1):
		if j%k==0:
			y+=1
	if y==2:
		u.append(j)
print(len(U))