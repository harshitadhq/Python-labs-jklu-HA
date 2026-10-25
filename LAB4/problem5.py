n=int(input())
t=input()
if n<20:
    if t=='day':
        fair=33.58+37.89*n
    elif t=='night':
        fair=33.58+43.17*n
elif n<100:
    fair=4.32*n
else:
    fair=2.88*n
print("Total fair:",fair)
