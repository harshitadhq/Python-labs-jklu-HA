#READ PROBLEM IN PDF:
x=int(input())
y=int(input())
n=int(input())
count=0
for i in range(x,y+1):
    if i%n!=0:
        print(i,end=" ")
        count+=1
print()
print("Numbers of working posts:",count)

