s = input()

if len(s) == 10:
    if (s[:2] == "RJ" and s[2:4].isdigit() and s[4:6].isupper() and s[6:10].isdigit()):
        print("True")
    else:
        print("False")
else:
        print("False")
