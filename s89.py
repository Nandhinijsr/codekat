p,q=input().split()
p=int(p)
q=int(q)
x=p*q
r=x**0.5
if r**2==x:
	print("yes")
else:
	print("no")