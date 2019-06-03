x=int(input())
if x > 1: 
	for j in range(2, x//2): 
	       if (x % j) == 0: 
	           print("yes") 
	           break
	else: 
	       print("no") 
else: 
	print("yes") 