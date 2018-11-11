c=input('')[0].lower()
if c>='a' and c<='z':
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
