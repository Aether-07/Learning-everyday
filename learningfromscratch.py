

#BASIC OF BASIC CALCULATORS
print("Basic Calculator")
print("Types of operators: + - / * ")
#Inputs
value1 = float(input("Enter first number: "))
value2 = float(input("Enter second number: "))
operator = input("Enter operator: ") #takes the operators in string "+"

#if elif and else truth or false with conditions:-

if operator == "+":
    result = value1 + value2
    print(f"{value1} {operator} {value2} = {result}")
elif operator == "-":
    result = value1 - value2
    print(f"{value1} {operator} {value2} = {result}")
elif operator == "/":
    result = value1 / value2
    print(f"{value1} {operator} {value2} = {result}")
elif operator == "*":
    result = value1 * value2
    print(f"{value1} {operator} {value2} = {result}")
else:
    print("Invalid operator")
#terminated
'''
#LOOPS-----------------------------------------
'''
for i in range(1,11):
    print(i)

for i in range(5):
    print("Hello")

for i in range(21):
    if i % 2 == 0:
        print(i)

num = int(input("enter n: "))
for i in range(num):
    print(i+1)

i = 1
while i>=1 and i<=5:
    print(i)
    i += 1
    
for i in range(10,0,-1): #(x,y,z) x and y and two ends of a range and z is the frequency
    print(i)
'''
#Functions---------------------------------------
'''
#simple calling of func
def myfunc():
    print("Hello Python")
myfunc()
myfunc()
myfunc()
#simple mathematical operation of custom input for factorial---------------
def squares(n):
    return n*n
num = int(input("Enter n:"))
print(squares(num))
#simple mathematical operations for summation----------------
def sum(a,b):
    return a+b
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(sum(a,b))
#loop of n numbers---------------
def lp(n):
    for i in range(1,n+1):
        print(i)
n = int(input("Enter n: "))
lp(n)
#even or odd---------------
def type(n):
    if n%2 == 0:
        print("Even")
    else:
        print("Odd")
n = int(input("Enter n: "))
type(n)
#sentence completion----------
def autfil(name):
    print(f"Hello {name}!")
name1 = input("Enter name: ")
autfil(name1)
#finding max of two numbers-----------------
def maxx(a,b):
    if a>b:
        return a
    else:
        return b
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(maxx(a,b))
'''
#List------------------------------------
'''
nums1 = [1,2,3,4,5]
print(nums1)

nums2 = [3, 6, 9, 12, 15]
print(nums2[0])
#x = len(nums2)-1
#print(nums2[x])
print(nums2[len(nums2)-1])

lists = [1,2,3,4,5,6,7,8,9]
for i in lists:
    print(i)

list1 = [1,2,3,4,5,6,7,8,9,10]
for i in list1:
    if i%2 == 0:
        print(i)
n = 0
for i in list1:
    n = n + 1
print(f"no.of values: {n}")

max1 = list1[0]
for i in list1:
    if i>max1:
        max1 = i
print(max1)
'''

#Strings------------------------------------
'''
string1 = "hello"
for c in string1:
    print(c)
print(len(string1))

vowels = "aeiou"
string2 = "hello my name is aether"
n = 0
for i in string2:
    if i in vowels: #this logic spot confuses me alot
        n = n+1
print(n)

string3 = "i love boob"
string4 = ""
n = len(string3)
for i in string3:       #take i = 0, for 0 in string3:(w) ; take i = 1, for 1 in string3:(h)
    string4 = i+string4 #string4 = w + "-" {string4 = w} ; string4 = h + "w" {string4 = hw}
print(string4)

wordd = "hi my name is a e t h e r"
spaces = " "
y = 0
for c in wordd:
    if c in spaces:
        y = y+1
print(y)

worddd = "ass"
copy_wordd = ""
for c in worddd:
    copy_wordd = c+copy_wordd
if copy_wordd == worddd:
    print("is palindrome")
else:
    print("is not palindrome")
'''
#Dictionaries-------------------------------
'''
dataas = {
    "name":"Aether",
    "age":22,
    "city":"New York"
}
print(dataas)

dataas["age"] = 24
print(dataas)

print(dataas["name"])
print(dataas["age"])

n = 0
for keys in dataas.keys():
    print(keys, ":", dataas[keys])
    n += 1
print(n)

person = {
    "Name" : "Lumine",
    "Age" : 22,
    "City" : "New York"
}
if "Age" in person:
    print("True")
else:
    print("False")

text = "apple banana apple mango banana apple"
words = text.split()
count = {
    "apple": 0,
    "banana": 0,
    "mango": 0
}
count.get("apple",0)
count.get("banana",0)
count.get("mango",0)
for x in words:
    if x == "apple":
        count["apple"] += 1
    elif x == "banana":
        count["banana"] += 1
    else:
        count["mango"] += 1
print(count)

#--------------
def word_count(text):
    words = text.split()
    return len(words)


def vowel_count(text):
    vowels = "aeiouAEIOU"
    count = 0
    for c in text:
        if c in vowels:
            count += 1
    return count


def space_count(text):
    count = 0
    for c in text:
        if c == " ":
            count += 1
    return count


def is_palindrome(text):
    clean = ""
    for c in text:
        if c != " ":
            clean += c

    rev = ""
    for c in clean:
        rev = c + rev

    return clean == rev


text = input("Enter a sentence: ")

print("Words:", word_count(text))
print("Vowels:", vowel_count(text))
print("Spaces:", space_count(text))

if is_palindrome(text):
    print("Palindrome: Yes")
else:
    print("Palindrome: No")
