# Variable
greeting = 'Hello World!'
print (greeting)

# Additional
addition = 2+2
result = addition - 1
print (result)

# Input
name = input('Input your name: ')
print(name)

# Data Typing (Dynamic)
x = 5
print(type(x)) #int

x = "5"
print(type(x)) #str

# Data Type
# Number
x = 6
print(type(x))

x = 6.0
print(type(x))

x = 1+2j
print(type(x))

# Boolean
b = True
print(type(b))

b = False
print(type(b))

# String
s = 'Learn Python Programming'
print(type(s))

# Indexing substring
myInisialName = 'Albi'
print(myInisialName[0])


# indexing and slicing
myLastName = 'AlbiMudakar'
print(myLastName[4:])

# Formatted String
NameUser = input("input your name: ")
print(f"Hello, my name is {NameUser}")

# Type Data Collection List
l = [1, 'albi', True, 1.0]
print(l[2])


# Slicing Python
dataList = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]
print(dataList[0:5:2])
print(dataList[1:])
# print(x[:3]) = 'complex' object is not subscriptable

# Tuple
dataTuple = (5, "albi", 1+3j)
print(type(dataTuple))

# Tuple Slicing
print(dataTuple[1])
print(dataTuple[0:3])

# Set
dataSet = {1, 2, 7, 2, 3, 13, 3}
print(dataSet)
print(type(dataSet))

# Set .union() and intersection()
set1 =  {1,2,3,4,5}
set2 = {4,5,6,7,8}
union = set1.union(set2)
print("union", union) #union {1, 2, 3, 4, 5, 6, 7, 8}

intersection = set1.intersection(set2)
print("intersection", intersection) #union {4, 5,}

# Dictionary
dataDisctionary = {'name': 'John doe', 'age':20, 'isMarried': False}
print(dataDisctionary)
print(dataDisctionary ['name'])
# add data Dictionry
dataDisctionary = "Cloud Engineer"
print(dataDisctionary)

# Del data Dictionary
# del dataDisctionary['name']
# print(dataDisctionary)

# Edit data dictoonary
# dataDisctionary ['age'] = 22
# print(dataDisctionary)

# Convertion Data
# Float
print(float(5))

# Float to Int
print(int(5.6))
print(int(-5.6)) 

# To Str
print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))

# Collection Data
print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))

# Dictionary
print(dict([[1,2],[3,4]]))

