first,second=map(int,input().split())
for i in range(first+1,second):
    if i%2==0:
        continue
    else:
        print(i,end=" ")
