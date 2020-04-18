def vol(rad):
    return (4.0/3)*(3.14)*(rad**3)
#########################################################
def ran_check(num,low,high):
    if num in range(low,high):
        print("%s is in the range" %str(num))
    else:
        print("the number is outside of the range")
def ran_bool(num,low,high):
    return num in range(low,high)
#########################################################
def upr_lwe(s):
    d={"upper":0,"lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.upper():
            d["lower"]+=1
        else:
            pass
    print("Original String" (s))
    print("No. of upper case characters : ", d["upper"])
    print("No. of lower case characters : ", d["lower"])
#########################################################
def unique_list(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return x
#########################################################
def multiply(numbers):
    total=numbers[0]
    for x in numbers:
        total*=x
    return total
#########################################################
def palindrome(s):
    return s==s[::-1]
#########################################################
import string
def ispangram(strl, alphabet=string.ascii_lowercase):
    alphaset=set(alphabet)
    return alphaset<=set(strl.lower())