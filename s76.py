p=int(input())
q=1
for j in range(2,p+1):
    if p%j==0:
        q=q+1
if q==2:
    print("yes")
else:
    print("no")