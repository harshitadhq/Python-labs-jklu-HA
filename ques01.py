txt = input('Enter a sentence: ').lower()
vowel = 0
consonant = 0
digits = 0
spaces = 0
others = 0

for ch in txt:
    if ch.isalpha():
        if ch in 'aeiou':
            vowel += 1
        else:
            consonant += 1
    elif ch.isdigit():
        digits += 1
    elif ch == ' ':
        spaces += 1
    else:
        others += 1

print('Vowels:',vowel)
print('Consonants:',consonant)
print('Digits:',digits)
print('Spaces:',spaces)
print('Others:',others)
