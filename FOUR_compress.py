s=input()
c=1
ans=""
i=0
while(i<len(s)):
    c=1
    f=0
    ans+=s[i]
    if s[i].isspace():
            i+=c
            continue
    for j in range(i+1,len(s)):

            if s[j].isspace():
                break
            if s[i]==s[j]:
                f=1
                c+=1

    if(f==1):
            ans+=str(c)
            f=0
    i+=c
print(ans)
