Num=int(input())
sum=0
temp=Num
while(temp>0):
	c=temp%10
	sum+=c**3
	temp//=10
if(Num==sum):
	print("yes")
else :
	print("no")