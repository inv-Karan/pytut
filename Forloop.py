list = [1,2,3,4,5,6,7,8,9,10]
for num in list:
    print('Hello')
    if num%2 == 0:
        print(num)
    else:
        print(f'Odd Numbers: {num}')
    
list_sum = 0
for num in list:
    list_sum = num + list_sum
    print(list_sum)

mystring = 'hello world'
for letter in mystring:
    print(letter)
for ghghg in 'hello world':
    print('cool')
for _ in 'hello world':
    print('yes')

tup = (1,2,3)
for item in tup:
    print(item)
for a,b,c in tup:
    print(a)
    print(b)
    print(c)
    print(a,b,c)
    print(item)

mylist = [(1,2),(3,4),(5,6),(7,8)]
print(len(mylist))
for item in mylist:
    print(item)
for a,b in mylist:
    print(a)
    print(b)
    print(a,b)
    print(item)
for (a,b) in mylist:
    print(a)
    print(b)
    print(a,b)
    print(item)

d = {'k1':1, 'k2':2, 'k3':3}
for key,value in d.items():
    print(key)
    print(value)
    print(item)
