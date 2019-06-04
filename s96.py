p=input()
q=0
x=len(p)
for j in range(0,x-1):
	for k in range(j+1,x):
		if p[j]==p[k]:
			q+=1
if q==0:
	print("yes")
else:
	print("no")