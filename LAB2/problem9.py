#A store sells widgets at 25 cents each for small orders or at 20 cents each for orders of 100 or more. Write a program that requests the number of widgets ordered and displays the total cost.
items=int(input("Enter number of widgets:"))
if items<100:
    cost=items*0.25
    print("Total cost:",cost)
elif items>=100:
    cost=items*0.20
    print("Total cost:",cost)
