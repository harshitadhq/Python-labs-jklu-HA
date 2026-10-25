N=int(input("Enter number of lines N: "))
i=1
while i<=N:
    spaces=N-i
    j=1
    line=""
    while j<=i:
        if j==1:
            line+=str(i)
        else:
            line+=" "+str(i)
        j+=1
    print((" "*spaces)+line)
    i+=1