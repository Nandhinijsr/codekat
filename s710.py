x=int(input())
for j in range(0,1000):
    if 2**j==x:
        break
j=j+1
print(2**j)