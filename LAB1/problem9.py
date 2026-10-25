#Write a program to SHOW THE GIVEN NUMBER OF SECONDS INTO HOURS MINUTES AND SECONDS FORMAT.
total_seconds=int(input("Enter seconds:"))
if total_seconds<0 or total_seconds>86400:
    print("Invalid input!")
else:
    hours=total_seconds//3600
    remaining=total_seconds%3600
    minutes=remaining//60
    seconds=remaining%60
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")


