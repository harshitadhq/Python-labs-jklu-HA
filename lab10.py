
#ans1
numbers = list(map(int, input().split()))
V = int(input())

t = tuple(numbers)

print("Tuple:", t)
print("Length:", len(t))
print("Count of", V, ":", t.count(V))
print("First index of", V, ":", t.index(V))


#ans2
def count_vowels(s):
    count = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            count += 1
    return count

text = input()
print("Vowels:", count_vowels(text))


#ans3
votes = input().split()

count = {}
order = []

for name in votes:
    if name in count:
        count[name] += 1
    else:
        count[name] = 1
        order.append(name)

for name in order:
    print(name, ":", count[name])

winner = order[0]
for name in order:
    if count[name] > count[winner]:
        winner = name

print("Winner:", winner)



#ans4
word = input()

freq = {}
for ch in word:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)



#ans5
def simple_interest(p, r, t=1):
    return p * r * t / 100

p = float(input())
r = float(input())

print("1 year:", simple_interest(p, r))
print("3 years:", simple_interest(p, r, 3))


#ans6
def get_grade(marks):
    if marks >= 80:
        return 'A'
    elif marks >= 60:
        return 'B'
    elif marks >= 40:
        return 'C'
    else:
        return 'F'

n = int(input())

grade_count = {}
order = []

for i in range(n):
    line = input().split()
    name = line[0]
    marks = int(line[1])

    grade = get_grade(marks)
    print(name, ":", grade)

    if grade in grade_count:
        grade_count[grade] += 1
    else:
        grade_count[grade] = 1
        order.append(grade)

print("Grade count:")
result = {}
for g in order:
    result[g] = grade_count[g]
print(result)



#ans7
numbers = tuple(map(int, input().split()))

evens = ()
for num in numbers:
    if num % 2 == 0:
        evens = evens + (num,)

print(evens)



#ans8
n = int(input())

capitals = {}
for i in range(n):
    line = input().split()
    country = line[0]
    capital = line[1]
    capitals[country] = capital

query = input()
if query in capitals:
    print(capitals[query])
else:
    print("Not found")



#ans9
n = int(input())

stock = {}
order = []

for i in range(n):
    line = input().split()
    item = line[0]
    qty = int(line[1])
    stock[item] = qty
    order.append(item)

q = int(input())

for i in range(q):
    line = input().split()
    action = line[0]
    item = line[1]
    qty = int(line[2])

    if action == "SELL":
        if qty > stock[item]:
            print("Insufficient stock:", item)
        else:
            stock[item] -= qty
    elif action == "ADD":
        if item in stock:
            stock[item] += qty
        else:
            stock[item] = qty
            order.append(item)

for item in order:
    print(item, stock[item])


#ans10
def stats(nums):
    smallest = nums[0]
    largest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    average = sum(nums) / len(nums)
    return (smallest, largest, average)

numbers = list(map(int, input().split()))
print(stats(numbers))

