p,q=input().split()
p=int(p)
q=int(q)
for j in range(p,q+1):
	if(j>1):
		for n in range(2,j):
			if(j%n==0):
				break
		else:
			print(j,end=" ")
		