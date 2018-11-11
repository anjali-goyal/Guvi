no=list(map(int,input().split()))
if no[0]>no[1]:
    if no[0]>no[2]:
        print(no[0])
    else:
        print(no[2])
else:
    if no[1]>no[2]:
        print(no[1])
    else:
        print(no[2])
