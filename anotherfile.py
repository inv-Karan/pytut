#TWO.PY

import newfile

print("TOP LEVEL IN TWO.PY")

newfile.func()

if __name__ == '__main__':
    print("TWO.PY is being run directly!")
else:
    print("TWO.PY has been imported")