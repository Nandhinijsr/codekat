p,q=list(map(int,input().split()))
r=list(map(int,input().split()))
s=False
for j in r:
    if j==q:
        s=True
        break
if s:
    print("yes")
else:
    print("no")