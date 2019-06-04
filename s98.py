p,q=[int(j) for j in input().split()]
if p > q:
	great = p
else:
	great = q

while(True):
	if((great % p == 0) and (great % q == 0)):
		x = great
		break
	great += 1
print(x)