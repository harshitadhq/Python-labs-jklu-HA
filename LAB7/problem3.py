text=input("Enter a sentence: ")
word=input("Enter a word: ")
print("Using inbuilt count():",text.count(word))
count=0
n=len(text)
w=len(word)
i=0
while i<=n-w:
    match=True
    j=0
    while j<w:
        if text[i+j]!=word[j]:
            match=False
        j+=1
    if match:
        count+=1
    i+=1
print("Without inbuilt functions count:",count)