txt = input()
new = ''

for i in range(len(txt)):
  if i%2 == 0:
    new += txt[i].upper()
  else:
    new += txt[i]

print(new)
