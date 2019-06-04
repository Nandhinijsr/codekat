p,q=[int(j) for j in input().split()]
if p > q:
    small = q
else:
    small = p
for j in range(1, small+1):
    if((p % j == 0) and (q % j == 0)):
        x = j
print(x)            
