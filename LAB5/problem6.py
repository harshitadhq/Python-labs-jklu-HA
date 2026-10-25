n=int(input())
if n<=0:
    print("Invalid input")
else:
    term=1
    count=1
    while count<=n:
        print(term,end=" ")
        term=term*2
        count+=1
