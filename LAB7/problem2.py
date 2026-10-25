s=input("Enter a sentence: ")
length=0
i=len(s)-1
while i>=0 and s[i]==" ":
    i-=1
while i>=0 and s[i]!=" ":
    length+=1
    i-=1
print("Length of last word:",length)