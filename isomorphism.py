str1=input()
str2=input()
for i in range(len(str1)):
    if str1.count(str1[i])!=str2.count(str2[i]):
        print("no")
        break
else:
    print("yes")
