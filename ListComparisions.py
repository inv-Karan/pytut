mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
    print(mylist)
mylist = [letter for letter in mystring]
print(mylist)
mylist = [x for x in 'word']
print(mylist)
mylist = [qwewe for qwewe in 'wordtwo']
print(mylist)
mylist = [num for num in range(0,11)]
print(mylist)
mylist = [x**2 for x in range(0,11)]
print(mylist)
mylist = [x**2 for x in range(0,11) if x%2==0]
print(mylist)
celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)
fahrenheit = []
for temp in celcius:
    fahrenheit.append(((9/5)*temp + 32))
    print(fahrenheit)
results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)
