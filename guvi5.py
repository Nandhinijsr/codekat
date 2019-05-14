a=input()
if(a.isalpha() and len(a)==1):
  if(a=='a' or a=='e' or a=='i' or a=='o'or a=='u'):
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
