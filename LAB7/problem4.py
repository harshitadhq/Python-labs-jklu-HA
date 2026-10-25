s=input("Enter a string: ").lower()
alphabet="abcdefghijklmnopqrstuvwxyz"
is_pangram=True
i=0
while i<len(alphabet):
    found=False
    j=0
    while j<len(s):
        if s[j]==alphabet[i]:
            found=True
        j+=1
    if not found:
        is_pangram=False
    i+=1
if is_pangram:
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")