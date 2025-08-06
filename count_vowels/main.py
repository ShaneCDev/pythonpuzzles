def count_vowels(phrase):
    vowel_count = []

    for char in phrase:
        if char in ['a', 'e', 'i', 'o', 'u']:
            vowel_count.append(char)
    
    print('The amount of vowels counted is: ' + str(len(vowel_count)) + ' - ' + ' '.join(vowel_count))


user_input = input('Enter a phrase: ')
user_input = user_input.lower()
count_vowels(user_input)
