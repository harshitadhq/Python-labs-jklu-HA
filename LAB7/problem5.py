s=input("Enter a string: ")
shift=int(input("Enter shift value: "))
res=""
i=0
while i<len(s):
    ch=s[i]
    if ch>='a' and ch<='z':
        res+=chr((ord(ch)-97+shift)%26+97)
    elif ch>='A' and ch<='Z':
        res+=chr((ord(ch)-65+shift)%26+65)
    else:
        res+=ch
    i+=1
print("Encrypted string:",res)