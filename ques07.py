txt = input()
change = 0

for i in range(len(txt)//2):
    if txt[i] != txt[-(i+1)]:
        change += 1
print('Changes needed:',change)
