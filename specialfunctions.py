def square(num):
    result = num**2
    return result
    for item in map(square, num):
        print(item)
    list(map(square, num))
    list(map(lambda num:num**2))

def splicer(mystirng):
    if len(mystirng)%2==0:
        return 'EVEN'
    else:
        return mystirng[0]
    list(map(lambda x:x[0],mystirng))
    list(map(lambda x:x[::-1],mystirng))

def check_even(num):
    return num%2==0
    for n in filter(check_even,num):
        print(n)
    list(filter(check_even,num))

