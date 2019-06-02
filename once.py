n=int(input())
inp=list(map(int,input().split()))
count=[]
for i in range(max(inp)+1):
    count.append(0)
for i in inp:
    count[i]=count[i]+1
for i in range(len(count)):
    if  count[i]==1:
        print(i)
        break
        
