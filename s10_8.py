x=int(input())
a=list(map(int,input().split()))
for j in range(0,x-1):
	if(a[j]!=j+1):
		print(j)
		break