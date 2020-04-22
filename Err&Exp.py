def add(n1,n2):
    print(n1+n2)

add(10,20)
print(add)

number1 = 10
number2 = input("Please provide a number: ")

add(number1,number2) # Error occurs as can not add str and int togather
print(add)
print("Something happened!")

try:
    # WANT TO ATTEMPT THIS CODE
    # MAY HAVE AN ERROR
    result = 10 + 10
    result = 10 + '10'
except:
    print("Hey it looks like you aren't adding correctly!")
    print(result)
else:
    print("Add went well!")
    print(result)

try:
    f = open('testfile','w')
    f1 = open('testfile','r')
    f.write("Write a test line")
    f1.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print('Hey you have an OS Error')
finally:
    print("I always run")

def ask_for_int():

    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("End of try/except/finally")
            print("I am going to ask again \n")
            print("I will always run at the end")
