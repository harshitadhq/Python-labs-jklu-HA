N=int(input("Enter number of lines N: "))
current_num=1
i=1
while i<=N:
    j=1
    line=""
    while j<=i:
        line+=str(current_num)+" "
        current_num+=1
        j+=1
    print(line)
    i+=1