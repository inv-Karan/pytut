def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)
#############################################
def animal_crackers(text):
    wordlist = text.split()
    print(wordlist)
    first = wordlist[0]
    second = wordlist[1]

    return first[0] == second[0]

def animal_crackers(text):
    wordlist = text.split()

    return wordlist[0][0] == wordlist[1][0]

def animal_crackers(text):
    wordlist = text.lower().split()
    print(wordlist)
    return wordlist[0][0] == wordlist[1][0]

    wordlist = text.upper().split()
    print(wordlist)
    return wordlist[0][0] == wordlist[1][0]
#############################################
def make_twenty(n1, n2):
    if n1+n2 == 20:
        return True
    elif n1 == 20:
        return True
    elif n2 == 20:
        return True
    else:
        return False

def make_twenty(n1, n2):
    if n1+n2 == 20 or n1 == 20 or n2 == 20:
        return True
    else:
        return False