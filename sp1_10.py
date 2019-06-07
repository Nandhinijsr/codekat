s,t=input().split()
w=len(s)
x=0
for j in range(0,w,1):
	if s[j]!=t[j]:
		x=x+1
if x==1:
	print("yes")
else:
	print("no")
	