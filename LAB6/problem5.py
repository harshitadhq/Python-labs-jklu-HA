N=int(input("Enter number of students N (2-100): "))
dist=int(input("Enter distance 1: "))
max_dist=dist
runner_up=-1
i=2
while i<=N:
    dist=int(input(f"Enter distance {i}: "))
    if dist>max_dist:
        runner_up=max_dist
        max_dist=dist
    elif dist>runner_up and dist<max_dist:
        runner_up=dist
    i+=1
print("Winning distance:",max_dist)
print("Runner-up distance:",runner_up)