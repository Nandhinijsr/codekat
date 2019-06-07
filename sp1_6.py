t1,t2=list(map(str,input().split()))
u=len(set(t1))
v=len(set(t2))
if u==v:
	print("yes")
else:
	print("no")
