h=input()
i=list(h)
i[::2],i[1::2]=i[1::2],i[::2]
print(''.join(i))
