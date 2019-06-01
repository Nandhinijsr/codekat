p,q=[int(r) for r in input().split()]
s=list(map(int,input().split()))
t=0
for j in range(p):
	if(s[j]==q):
		t+=1
print(t)