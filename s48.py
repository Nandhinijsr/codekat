p,q=input().split()
p=int(p)
q=int(q)
p=p^q
q=q^p
p=p^q
print(p,q)