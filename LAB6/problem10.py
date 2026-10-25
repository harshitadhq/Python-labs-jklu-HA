N=int(input("Enter an odd positive integer N: "))
i=1
while i<=N:
    if i<=(N//2)+1:
        spaces=(N//2)+1-i
        stars=2*i-1
    else:
        spaces=i-((N//2)+1)
        stars=2*(N-i)+1
    line=(" "*spaces)+("*"*stars)
    print(line)
    i+=1