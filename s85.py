p=input()
q=[]
for j in p:
    q.append(j)
r=len(q)
s=r//2
if(r%2!=0):
    q[s]="*"
else:
    q[s]="*"
    q[s-1]="*"
print("".join(q))