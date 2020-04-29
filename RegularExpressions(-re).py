import re

patterns = ['term1','term2']

text = 'This is a string with term1, but not the other term'

re.search('hello','hello world!')

for pattern in patterns:
    print('Serarching for "%s" in: \n"%s"' % (pattern,text))
    
    # Check for match
    if re.search(pattern,text):
        print('\n')
        print('Match was found. \n')
    else:
        print('\n')
        print('No match was found. \n')

print(re.search('h','w'))

match = re.search(pattern[0],text)

type(match)

match.start()

match.end()

split_term = '@'

phrase = 'What is your email, is it hello@gmail.com?'

re.split(split_term,phrase)

'hello world'.split()

re.findall('match','Here is one match, here is another match')