number=list()
r,s = input().split()
s = int(s)
r = int(r)
sum = 0
number=input().split()
for count in range(0,s):
    sum = sum + int(number[count])
print (sum)