num=int(input())
n=(int)(num/2)
if num==1 or num==2 or num==3:
    print("yes")
else:
    for i in range(2,n+1):
        if num%i==0:
            break
    if i==n:
        print("yes")
    else:
        print("no")
            
