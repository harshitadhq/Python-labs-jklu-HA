#READ IN QUESTIONS' PDF.
initial_water=int(input("Enter the initial amount of water in liters: "))
days=int(input("Enter the number of days:"))
if initial_water<0 or days<0:
    print("Invalid input!")
else:
    final_water=200+(initial_water-200)*0.95**days
    print("The final amount of water in the tank after",days,"days is:",final_water,"liters.")
    