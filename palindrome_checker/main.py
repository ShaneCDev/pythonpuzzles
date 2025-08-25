def palindrome_checker(word):
    chars = []
    rev_list = []
    
    for char in word:
        chars.append(char)
    
    index = len(chars)


    while index != 0:
        x = index - 1
        rev_list.append(chars[x])
        index -= 1
    
    print('New list: ' + ''.join(rev_list))
    comparison = ''.join(rev_list)

    if word == comparison:
        print('Input word: ' + word)
        print('Reverse of input: ' + comparison)
        print('This word is a palindrome!')
    else:
        print('Input word: ' + word)
        print('Reverse of input: ' + comparison)
        print('This word is not a palindrome')



user_input = input('Enter a word: ')
palindrome_checker(user_input)
