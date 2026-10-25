print("N    N^2     N^3       Square Root")
print("-"*35)
n=1
while n<=15:
    n_sq=n*n
    n_cube=n*n*n
    guess=n/2.0
    if guess==0:
        guess=1.0
    iter_count=0
    while iter_count<20:
        guess=(guess+n/guess)/2
        iter_count+=1
    sqrt_val=guess
    print(f"{n:<5}{n_sq:<8}{n_cube:<10}{sqrt_val:<12.4f}")
    n+=1