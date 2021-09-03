n=list(map(int,input().split(",")))
for x in n:
    x+=64
    print(chr(x),end="")
