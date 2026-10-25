#Write a program that interprets the Body Mass Index (BMI) based on a user’s weight and height.
height=int(input("Enter height in meters:"))
weight=int(input("Enter weight in kilograms:"))
bmi=weight/height**2
if bmi<18.5:
    print("Underweight")
elif bmi<25:
    print("Normal weight")
elif bmi<30:
    print("Slightly Overweight")
else:
    print("Obese")