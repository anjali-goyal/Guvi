n=int(input())
lst=list(map(int,input().split()))
rst=sorted(lst,reverse=True)
if rst[0]==0:
    print("0")
else:
    print("".join(str(x) for x in rst))
