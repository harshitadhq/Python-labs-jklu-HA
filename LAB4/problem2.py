#Write a program that reads input data from the console - a password (one line of random text)  and checks if the input matches the phrase "s3cr3t!P@ssw0rd". If it matches, print "Welcome", otherwise print "Wrong password!".
a=input("Enter Password:")
password="s3cr3t!p@ssw0rd"
if a==password:
    print("Welcome")
else:
    print("Wrong password")
    
