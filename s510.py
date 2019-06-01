def isPowerOfTwo (p): 
      return (p and (not(p & (p - 1))) ) 
q=int(input())
if(isPowerOfTwo(q)): 
    print('yes') 
else: 
    print('no') 