#Creating a Class
'''
CAR = CLASS
PORSCHE = OBJECT
COLOR,SPEED = ATTRIBUTES
DRIVE,BREAK = METHODS
'''
#the industry standard for making classes using caps (MyClass) unlike in functions (my_class);
class MyClass:
    """
    This is me learning OOPS in python
    """
    pass

#Creating a object
obj1 = MyClass()
obj2 = MyClass()

#printing type of data using type() func
print(type(obj1))
print(type(obj2))
#Gives an output: __main__.MyClass so this means that the class is in the same file/module and not elsewhere

#doc function __doc__
print(MyClass.__doc__)

'''
#ATTRIBUTES----------------------------------------------------
'''
class Character:
    pass

char1 = Character()
char2 = Character()

char1.name = "Esdeath"
char1.sex = "Female"

char2.name = "Flins"
char2.sex = "Male"

print(char1.__dict__)
print(char2.__dict__)

'''
#INSTANCE METHOD ------------------
'''

class Students:
    """
    this class talks about student activities
    """
    # is called a instance------
    def study(self): #<-------- This is a method so calling it like a function
                    #          it won't work unless you keep smtg in the bracket
        print("The students studied 3 hours a day")

student1 = Students()
print(student1)  # We are getting the memory address when doing this
student1.study()

#BANK ACC
class BankAcc:
    """
    BANK ACCOUNT APPLICATION MANAGEMENT
    """
    pass

user1 = BankAcc()

print(BankAcc.__doc__)

user1.holdername = input("Enter Account holder name: ")
user1.accnum = int(input("Enter Account Number: "))
user1.balance = int(input("Enter balance: $"))

print("What would you like to do?: ")
print("A).deposit amount B).withdraw amount C).display acc details")
i = input("Enter A,B,C to choose the option: ")
if i == "A":
    x = int(input("Deposit amount: "))
    user1.balance = user1.balance + x
    print(f"Remaining balance: ${user1.balance}")
elif i == "B":
    y = int(input("Withdraw amount: "))
    user1.balance = user1.balance - y
    print(f"Remaining balance: ${user1.balance}")
elif i == "C":
    print("=======================================")
    print(user1.__dict__)
else:
    print("enter valid input")
