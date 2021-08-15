# print("Hello World")
#
# message = "Welcome to Python"
# print(message)
#
# print(message[0:7])
# print(message[:7])
# print(message[6:])
# print(message[-6:])
# print(len(message))
# print(message.lower())
# print(message.upper())
# print(message.count(message))
# print(message.find("World"))
#
# info ="""Person of Iterest was a popular
# series between 2010 and 2021"""
# print(info)
#
# greetings_message = "Hello World"
# greetings_message=greetings_message.replace("World","_Universe")
# print(greetings_message)
#
# greeting = "Hello"
# name = "Hamisi"
# message= greeting + name
# message = greeting +", "+ name
# message ="{}, {} -Welcome".format(greeting, name)
# message= f"{greeting}, {name.upper() },-Welcome"
# print(message)
#
# greetings = "Hello"
# print(dir(message))
# print(help(str.lower()))

num = 3
num = 3.14
print(type(num))

print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3//2) #Floor Division
print(3 ** 2) #Exponent
print(3 % 2)  #Modulus

#order of operations
print(3 *(2 + 1))
num=1
#num += 1
num *= 10
print(num)

print(abs(-3))
print(round(3.75, 1))

#comparison operators
num_1 = 3
num_2 = 2
print(num_1 == num_2)   #Equal
print(num_1 != num_2)   #Not Equal
print(num_1 > num_2)    #Greater than
print(num_1 < num_2)    #less than
print( num_1 >= num_2)   #Greater or Equal to
print(num_1 <= num_2)    #less than or equal to

num_1 = '100'
num_2 = '200'

num_1 =int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)

courses=['History', 'Maths','Physics', 'Computer Science']
print(len(courses))
print(courses)
print(courses[0])
print(courses[3])
print(courses[-1])
print(courses[0:2])
print(courses[:2])
print(courses[2:])
courses.append('Art')
courses.insert(0, 'Statistics')
print(courses)

courses_2 = ['Art','Education']
courses.insert(0, courses_2)
print(courses)
print(courses[0])
courses.extend(courses_2)
print(courses)
print(courses[0])

courses.append(courses_2)
print(courses)

#removing values
courses.remove('Art')
print(courses)

popped =courses.pop()
print(courses)
print(popped)

courses.reverse()
print(courses)

courses.pop()
courses.sort()
print(courses)

nums = [1,5,2,4,3]
nums.sort(reverse=True)
print(nums)
print(min(nums))
print(max(nums))
print(sum(nums))

sorted_courses =sorted(courses)
print(courses)
print(courses.index("Computer Science"))
print("Computer Science" in courses)

for item in courses:
    print(item)

for index, item in enumerate(courses, start=1):
    print(index, item)

course_str =', '.join(courses)
print(course_str)

new_list = course_str.split(" - ")
print(new_list)


#LISTS ARE MUTABLE
list_1 = ['History', 'Math', 'Physics', 'Computer Science']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0]= 'Art'
print(list_1)
print(list_2)


#TUPLES ARE IMMUTABLE
tuple_1 = ('History', 'Math', 'Physics', 'Computer Science')
tuple_2 =tuple_1
print(tuple_1)
print(tuple_2)

# tuple[0] = "Art"
# print(tuple_1)
# print(tuple_2)

# sets
cs_courses= {'History', 'Math', 'Physics','Comp Science'}
art_courses= {'History', 'Math', 'Art','Design'}
print(cs_courses)
print("Math"in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

# empty list
empty_list = []
empty_list = list()

# empty tuple
empty_tuple = ()
empty_tuple= tuple()

# empty sets
#
empty_set = {} #This isnt right its dict
empty_set= set()


language = 'Python'
if language == 'Python':
    print("Language is Python")
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No Match')

#and
#or
#not

user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in:
    print("Admin Page")
else:
    print("Bad Credentials")

user = 'Admin'
logged_in = False
if user == 'Admin' or logged_in:
    print("Admin Page")
else:
    print("Bad Credentials")

user = 'Admin'
logged_in = False
if not logged_in:
    print("Please Log in")
else:
    print("Welcome")

a= [1,2,3]
b= [1,2,3]
b = a
print(a==b)
print(id(a))
print(id(b))
print(a is b)

condition = False

if condition:
    print("Evaluated to True")
else:
    print("Ealuated to False")


condition = None
if condition:
    print("Evaluated to True")
else:
    print("Ealuated to False")


condition = 0

if condition:
    print("Evaluated to True")
else:
    print("Ealuated to False")



condition = 10

if condition:
    print("Evaluated to True")
else:
    print("Ealuated to False")


condition = []

if condition:
    print("Evaluated to True")
else:
    print("Ealuated to False")


condition = ''

if condition:
    print("Evaluated to True")
else:
    print("Ealuated to False")

condition = ()

if condition:
    print("Evaluated to True")
else:
    print("Ealuated to False")


condition = { }

if condition:
    print("Evaluated to True")
else:
    print("Ealuated to False")



condition = 'Test'

if condition:
    print("Evaluated to True")
else:
    print("Ealuated to False")

nums = [1,2,3,4,5]
for num in nums:
    print(num)

for num in nums:
    if num == 3:
        print("Found")
        break
    print(num)


for num in nums:
    if num == 3:
        print("Found")
        continue
    print(num)

for num in nums:
    for letter in 'abc':
        print(num, letter)


for i in range(1, 11):
    print(i)

x = 0
while x <= 10:
    if x == 5:
        break
    print(x)
    x +=1


# x = 0
# while True:
#     print(x)
#     x +=1


# FUNCTIONS
def hello_func():
    pass

print(hello_func)


def hello_func():
    print('Hello Function. ')

print(hello_func)
hello_func()
hello_func()
hello_func()
hello_func()

def hello_func():
    return ('Hello Function.')

print(hello_func())
print(len('Test'))
print(hello_func().upper())
print(hello_func().lower())
print(hello_func().title())

def hello_func(greeting):
    return ('{} Function.'.format(greeting))

print(hello_func('Hi'))


def hello_func(greeting, name = "You "):
    return ('{} {}.'.format(greeting, name))

print(hello_func('Hi', name ="Hamisi"))


# def student_info(args, **kwargs):
#     print(args)
#     print(kwargs)
#
# courses = ['Math', 'Art']
# info = {'name':"John", 'age':22}
#
# student_info(*courses, **info)


month_days = [8,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return  year %4 ==0
   #return true for leap year , false for non leap year


