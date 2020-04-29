# convert 1024 to binary and hexadecimal representation
print(bin(1024))
print(hex(1024))

# round 5.23222 to two decimal places
x = round(5.23222,2)
print(x)

# check whether every letter in string s is lower case or not
s = 'hello how are you Mary, are you feeling okay?'
s.islower()
print(s)

# count letter 'w' in string given
s = 'wxyzzyxw'
s.count('w')
print(s)

# find elements in set1 and not in set2
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
set1.difference(set2)
print(set1)

# find all elements are in either set
set1.union(set2)

# create this dictionary: {0:0, 1:1, 2:8, 3:27, 4:64} using dictionary comprehension
{x:x**3 for x in range(5)}
print(x)

# reverse the list
l = [1,2,3,4]
l.reverse()
print(l)

# sort the list
l = [3,4,2,5,1]
l.sort()
print(l)