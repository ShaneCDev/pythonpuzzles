def reverse_words_not_characters(phrase):
    list_words = []
    rev_list_words = []
    words = phrase.split()
    
    for word in words:
        list_words.append(word)

    i = len(list_words)

    while i != 0:
        x = i-1
        rev_list_words.append(list_words[x])
        i -= 1
    
    print('The reverse output is: ' + ' '.join(rev_list_words))




user_phrase = input('Please enter a phrase: ')
reverse_words_not_characters(user_phrase)
