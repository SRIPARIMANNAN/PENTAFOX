import random
s=input()
s.lower()
n=random.randint(0,len(s)-1)
print(s[n].upper()+s[::-1])
