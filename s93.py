p,q,r=[j for j in input().split()]
if(q=="%"):
	print(int(p)%int(r))
else:
	print(int(int(p)/int(r)))