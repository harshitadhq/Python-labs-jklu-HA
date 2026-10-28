txt = input('Enter a sentence: ')
count = 0

for ch in txt:
    if ch == ' ':
        if count != 0:
            print(count,end=' ')
        count = 0
        continue
    count += 1
    
if count != 0:
    print(count,end=' ')
