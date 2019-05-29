x=input()
for j in x:
    if j not in ['1','2','3','4','5','6','7','8','9','0',"."]:
        print("No")
        break
else:
    print("Yes")