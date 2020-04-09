mylist = [1,2,3]
for num in range(0,10,2):
    print(num)
    print(list(range(0,10,2)))

index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1

word = 'abcde'
for item in enumerate(word):
    print(item)
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c']
mylist3 = [100.100,200.200,300.300]
for a,b,c,item in zip(mylist1,mylist2,mylist3):
    print(item)
    print(list(zip(mylist1,mylist2,mylist3)))
    print(a,b,c)