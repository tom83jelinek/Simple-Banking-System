text = input().lower()
vowels = 'aeiouy'

for character in text:
    if character in vowels:
        print('vowel')
    elif not character.isalpha():
        break
    else:
        print('consonant')
