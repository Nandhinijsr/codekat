p,q=[int(j) for j in input().split()]
s=list(map(int,input().split()))
s.sort()
print(s[q-1])