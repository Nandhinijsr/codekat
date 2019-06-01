p=list(map(str,input()))
q=0
r=0
for k in range(0,len(p)):
    if p[k].isdigit()==True:
        q=q+1
    elif p[k].isalpha()==True:
        r=r+1
if r>0 and q>0:
    print("Yes")
else: print("No")