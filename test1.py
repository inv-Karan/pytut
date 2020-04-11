def myfunc(*args):
    return sum(args)

def myfunc(*args):
    return [list for list in args if list%2 == 0]

def myfunc(*args):
    str = []
    for index, c in enumerate(*args):
        if index%2==0:
            str.append(c.upper())
        else:
            str.append(c.lower())
    return ''.join(str)

def myfunc(args):
    str = []
    for index in range(len(args)):
        if index%2==0:
            str.append(args[index].upper())
        else:
            str.append(args[index].lower())
    return ''.join(str)