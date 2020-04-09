x=0
while x<5:
    print(f'the current value of x is {x}')
    x += 1
else:
    print("X is not less than 5")

x = [1,2,3]
for item in x:
    pass
print('emd of the script')

mystring = 'this'
for letter in mystring:
    if letter == 'a':
        break
    print(letter)
    if letter == 't':
        continue
    print(letter)

x=0
while x<5:
    if x==2:
        break
    print(x)
    x += 1