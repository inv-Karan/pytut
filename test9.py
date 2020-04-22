try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("General error! Watch out!")

try:
    x = 5
    y = 0
    z = x/y
except:
    print("Error!")
finally:
    print("All done")

def ask():

    waiting = True
    while waiting:
        try:
            n = int(input("Enter a number"))
        except:
            print("Please try again \n")
            continue
        else:
            waiting = False

    print("Your number squared is: ")
    print(n**2)