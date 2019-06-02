n=int(input())
lst=list(map(int,input().split()))
result=[]
for i in range(n-1):
    for j in range(i+1,n):
        if lst[i]==lst[j]:
            result.append(lst[i])
            lst.remove(lst[i])
            n=n-1
            break
if not result:
    print("unique")
else:
    print(" ".join(str(x) for x in result))
    
