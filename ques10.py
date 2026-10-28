s = input()

count = 1
maximum = 1
ch = s[0]

for i in range(1,len(s)):
    if s[i] == s[i-1]:
        count += 1 
    else:
        count = 1

    if count > maximum:
        maximum  = count
        ch = s[i]

print(ch,maximum)
