n=int(input())
inp=list(map(int,input().split()))
result=[]
for i in range(n):
    if i==inp[i]:
        result.append(i)
if not result:
    print("-1")
else:
    print(" ".join(str(x) for x in sorted(result)))
          
