n=list(map(int,input("arr = ").strip().split(",")))
s=int(input("Sum = "))
f=0
for x in range(0,len(n)-1):
    		for y in range(x+1,len(n)):
        		if(n[x]+n[y]==s):
            			print(n[x],",",n[y])
            			f=1
if(f==0):
    	print("No Pairs found")
