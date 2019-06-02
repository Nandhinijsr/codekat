p=str(input())
q=0
for j in range(0,len(p)):
	if(p[j]!='0')and(p[j]!='1'):
		q+=1
if(q>0):
	print("no")
else:
	print("yes")