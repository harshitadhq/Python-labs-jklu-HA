s = input()
uniq = ''

for char in s:
    if char not in uniq:
        uniq += char
print(uniq)
