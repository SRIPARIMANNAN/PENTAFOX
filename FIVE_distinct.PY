s=input()
ss=input()
l=list(ss)
ans=""
for x in range(0,len(s)):
    if s[x] not in l:
        ans+=s[x]
l=list(s)
for x in range(0,len(ss)):
    if ss[x] not in l:
        ans+=ss[x]

print(ans)
