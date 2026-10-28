txt = input()
ch = input()

count = 0
positions = []

for i in range(len(txt)):
    if txt[i] == ch:
        count = count + 1
        positions.append(str(i))

print("Count:",count)

if count == 0:
    print("Positions: -1")
else:
    print(f'Positions: {" ".join(positions)}')
