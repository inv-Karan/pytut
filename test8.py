class Simple():

    def __init__(self,value):

        self.value = value

    def add_to_value(self,amount):

        self.value = self.value + amount
        print('We just added {} to your value'.format(amount))
        #super().__init__()

        myobj = Simple(300)
        print(myobj.value)
        print(myobj.add_to_value)

class Account():

    def __init__(self,owner,balance=0):

        self.owner = owner
        self.balance = balance

    def deposit(self,dep_amt):

        self.balance += dep_amt
        print(f"Added {dep_amt} to the balance")

    def withdrawal(self,wd_amt):

        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print("Withdrawal accepted")
        else:
            print("Sorry, not enough amount!")

    def __str__(self):
        #return super().__str__()
        return f"Owner: {self.owner} \nBalance: {self.balance}"

    a = Account("Sam",500)
    a.owner
    a.balance
    print(a)
    a.withdrawal(500)
    print(a)
    a.withdrawal(1)
    print(a)
