h=int(input("Enter number of holidays:"))
if h<0 or h>365:
    print("Invalid Input!")
else:
    workdays=365-h
    playtime=(workdays*63)+(h*127)
    norm=30000
    diff=abs(norm-playtime)
    hours=diff//60
    minutes=diff%60
    if playtime<=norm:
        print("Tom sleeps well")
        print(f"{hours} hours and {minutes} minutes less for play.")
    else:
        print("Tom will run away")
        print(f'{hours} hours and {minutes} minutes more for play.')
        