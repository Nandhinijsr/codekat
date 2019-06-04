p=input()
q=[]
for j in p:
	if j.isnumeric():
		q.append(j)
print("".join(q))