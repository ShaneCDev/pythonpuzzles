def valid_parentheses(input_string):
    character_stack = []
    for character in input_string:
        if character in ['(', '{', '[']:
            character_stack.append(character)
        elif character in [')', '}', ']']:
            com = character_stack.pop()
            if com == '[' and character == ']' or com == '(' and character == ')' or com == '{' and character == '}':
                #print('This is balanced')
                return True
            else:
                #print('This is not balanced') 
                return False
            
                
    
    


print(valid_parentheses('()'))
print(valid_parentheses("()[]"))
print(valid_parentheses('(]'))
print(valid_parentheses('([])'))
print(valid_parentheses('([)]'))
