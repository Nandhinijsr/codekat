p=input()
x=0
for j in p :
  if j.isnumeric()!=True :
    if j.isalpha()!=True :
      x=x+1
print(x)