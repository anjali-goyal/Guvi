l=list(map(int,input().split()))
n=l[0]
k=l[1]
arr=[]
s=0
for i in range(n):
    arr.append(int(input()))
for i in range(k):
    s=s+arr[k]
print(s)

