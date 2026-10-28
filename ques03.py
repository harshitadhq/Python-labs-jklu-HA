pas = input()

if len(pas) < 8:
    print("weak")
else:
    upper = 0
    lower = 0
    digit = 0
    special = 0

    for char in pas:
        if char.isupper():
            upper = 1
        elif char.islower():
            lower = 1
        elif char.isdigit():
            digit = 1
        elif char != ' ':
            special = 1

    total = upper+lower+digit+special

    if total == 4:
        print('STRONG')
    elif total == 2 or total == 3:
        print("MODERATE")
    else:
        print("WEAK")
