import stringIO

# Arbitrary String

message = 'This is just a normal string.'

# Use StringIO method to set as file object

f = stringIO.stringIO(message)

f,read()

f.write('Second line written to file like object')

f.seek(0)

f.read()

