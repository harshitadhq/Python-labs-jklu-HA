s=input("Enter a sentence: ")
res=""
i=0
while i<len(s):
    ch=s[i]
    found=False
    j=0
    while j<len(res):
        if res[j]==ch:
            found=True
        j+=1
    if not found:
        res+=ch
    i+=1
print("Without duplicates:",res)