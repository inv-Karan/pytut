def old_macdonald(name):
    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]

    return first_letter.upper()+inbetween.lower()+fourth_letter.upper()+rest

def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]

    return first_half.capitalize()+second_half.capitalize()
#############################################################################
def master_yoda(text):
    wordlist = text.split()
    reverse_word_list = wordlist[::-1]

    return ''.join(reverse_word_list)
#############################################################################
def almost_there(n):
    
    return (abs(100-n)<=10) or (abs(200-n)<=10)