n=int(input())
x=n
s=0
while x!=0:
    a=x%10
    s=a+s*10
    x=x//10
if s==n:
    print("Yes")
else:
    print("No")
