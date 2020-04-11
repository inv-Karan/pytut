def name_function():
    '''
    DOCSTRING: Information about the function
    INPUT: no input...
    OUTPUT: Hello ..
    '''
    print('Hello')
    
def say_hello(name='NAME'):
    print('hello'+name) 
    return 'hello'+name
    result = say_hello('bro')
    print(result)

def add(n1,n2):
    return n1+n2
    result = add(20,30)
    print(result)

def dog_check(mystring):
    if 'dog' in mystring:
        return True
    elif 'dog' in mystring.lower():
        return mystring
        dog_check('My dog ran away')
        print(dog_check)
        dog_check('Dog is back')
        print(dog_check)

def pig_latin(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word
    print(pig_word)
    