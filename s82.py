p = input()
x=0
for q in p:
    if(q=='A' or q=='a' or q=='E' or q =='e' or q=='I'or q=='i' or q=='O' or q=='o' or q=='U' or q=='u'):
        x=1
if(x==1):
    print("yes")
else:
    print("no")