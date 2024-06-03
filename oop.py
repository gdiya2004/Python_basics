##OOP--> object oriented Programming
##CLass is a blueprint or template for creating objects. It defines properties and methods that object of that class will have.
##Properties are data or state of an object and methods are action or behaviors that an object can perform.
##Object is an instance of class and it contains the own data and methods
## For example : you could create a class named "person" that has properties such as name and age and also methods such as speak() and walk(). Each instance of person class would be unique object with its own name and age, but they would have same methods to speak and walk.

###Encapsulation:internal state of an object is hidden and can only be accessed or modified through object's methods. This helps to protect the object's data and prevent from being leaked.
###Inheritance:which allows new classes to be created which inherit properties and methods of an existing class. This allows for code reuse and make it is easy to create new class have similar functionality to existing class.
###Polymorphism:objects of different classes can be treated as if they are objects of common class. This allows greater flexibility in the code and make it easier to run the code that can run work with multiple types  of objects.

##creating class. Class is a keyword and self is a keyword.
# class Person:
#     name="Diya"
#     occupation="software developer"
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")
# a=Person()
# a.name="Khyati"
# a.occupation="scientist"
# a.info()
# print(a.name)
# print(a.occupation)

###self reference is reference to current instance of class and it is used to access variables that belong to class.

###Constructor: is a special method in a class used to create and initialize an object of a class.
# it is a unique function that is called automatically as when object is created. 
# the main aim is to initialize or assign values to data membersd of that class.
## Constructor always returns none

##Parameterised Constructor
# class Person:
#     def __init__(self,n,o):
#         self.name=n
#         self.occ=o     
#     def info(self):
#         print(f"{self.name} is {self.occ}")
# a=Person("Diya","Software developer")
# a.info()
##c=Person() ##Type error will be raised that it is missing two arguments that is n and o
##c=Person(1,2,3) ###type error : there is passing of four arguments as one of them is passed automatically i.e. c

## DEfault Constructor: doesnot accept any argument from the object and has only one argument , self in the constructor
# class Person:
#     def __init__(self):
#         print("Hey! I am diya gupta")
# a=Person()

###Decorators: are used to modify the function
##decorator is a function that takes a function as a argument and returns a new function after modifying the behaviour of original function. The function modified is called "decorated"
# def greet(fx):
#     def mfx(*args,**kwargs):
#         print("Good Morning")
#         fx(*args,**kwargs)
#         print("Thanks for coming")
#     return mfx

# @greet
# def hello():
#     print("Hello World")
# # greet(hello)()
# @greet
# def add(a,b):
#     print(a+b)
# hello()
# add(2,3)

##Practical use of decorators: to add logging to a function
# import logging ##logging module
# def log_function_call(func):
#     def decorated(*args,**kwargs):##takes any number of positional and keyword arguments using args and kwargs
#         logging.info(f"Calling {func.__name__} with args ={args} , kwargs={kwargs}")
#         result=func(*args,**kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated
# @log_function_call
# def my_function(a,b):
#     return a+b
# x=my_function(2,3)
# print(x)

###Getters and Setters
# class MyClass:
#     def __init__(self,value):
#         self._value=value
#     def show(self):
#         print(f"Value is {self._value}")
#     @property##getter method
#     def ten_value(self):
#         return 10*self._value
#     @ten_value.setter
#     def ten_value(self,new_value):
#         self._value=new_value/10
# obj= MyClass(10)
# obj.ten_value=67
# print(obj.ten_value)
# obj.show()
##Property decorator is a in-built function that allows u to define properties for ur class in away that enables u to use getter, setter and deleter methods.
##it provides a convinient way to encapsulate the access to attributes of an object, allowing u to control how these attributes are accessed.
##getter: This method retrieves the value of property when it is accessed. to access the value of object's properties. These are defined by using @property decorator.
##setter:this method sets the value of property when it is assigned a new value. This is done by @property_name.setter
##deleter:this method delets the property when del is called on the property.

# class MyClass:
#     def __init__(self,value):
#         self._value=value
#     def show(self):
#         print(f"Value is {self._value}")
#     @property
#     def value(self):
#         return self._value
#     @value.setter
#     def value(self,new_value):
#         self._value=new_value

##Inheritance in python: 
#class BaseClass():
#   Body of BaseClass
#class DerivedClass():
#   Body of DerivedClass
##Type of inheritance: Single, Multiple, Multilevel, Hybrid, Hierarichal
# class Employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def show(self):
#         print(f"The name of employee:{self.id} is {self.name}")
# class Programmer(Employee):###Inheritance::allmethods and properties of employee are accessible by programmer
#     def show_lang(self):
#         print("The Python is default language.")
# e1=Employee("Diya",400)
# e1.show()
# e2=Programmer("Baani",401)
# e2.show()
# e2.show_lang()

##Acess specifiers/modifiers:are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.
##Types of accesss specifiers:
##Public access modifier:(by default) class ke bahar se access kiye ja sakte hain
##Private Access Modifier:class ke bahar se access nhiu honge. it is done by prefixing its name with double underscore. This is known as weak internal use indicator
##Protected Access modifier:can be accessed within the class and through sub or child class

# class Employee:
#     def __init__(self):
#         # self.name="Diya"
#         self.__name="Diya"
# a=Employee()
# # print(a.name) ##Public access modifier
# # print(a.__name) #private access modifier cannot be accesed dorectly
# print(a._Employee__name) ##private can be accesed indirectly

# class Student:
#     def __init__(self,age,name):
#         self._age=age
#     def _funName(self):
#         self.y=34
#         print(self.y)
# class Subject(Student):
#     pass
# obj=Student(21,"Diya")
# obj1=Subject(16,"Khyati")
# print(obj._age)
# print(obj._funName())
# print(obj1._age)
# print(obj1._funName())

# ##Private access modifier::
# class Employee:
#     def __init__(self):
#         self.__name="Diya"
# a=Employee()
# # print(a.__name) ##AttributeError
# print(a._Employee__name)  ## This is basicaly name mangling where single underscore is followed by double underscore.##This prints Diya
# print(a.__dir__()) ## to print all methods and attributes assocuated with a

##one more example Private v/s Public access modifiers
# class MyClass:
#     def __init__(self):
#         self._private_attribute="I am a private attribute"
#         self.__mangled_attribute="I am a mangles attribute"
# my_object=MyClass()
# print(my_object._private_attribute)
# print(my_object.__mangled_attribute)##Attribute Error
# print(my_object._MyClass__mangled_attribute)

##Protected access modifiers:it is indicated by prefixing its name with single underscore. Single underscore is just a naming convention but donot provide any protection or restriction
# class Student:
#     def __init__(self):
#         self._name="Diya"
#     def _funName(self):
#         return "Diya_Gupta"
# class Subject(Student):
#     pass
# obj=Student()
# obj1=Subject()
# #Calling by object of student class
# print(obj._name)
# print(obj._funName())
# #Calling by object of Subject class
# print(obj1._name)
# print(obj1._funName())

##static method are method that belongs to a class rather than an instance of class. Defined by using @staticmethod decorator
# class Math:
#     def __init__ (self,num):
#         self.num=num
#     def addTonum(self,n):
#         self.num+=n
#     @staticmethod ##static method ke liye decorator
#     def add(a,b):
#         return a+b
# a=Math(5)
# print(a.num)
# a.addTonum(6)
# print(a.num)
# print(Math.add(2,3))
# print(a.add(2,3))

# class Employee:
#     CompanyName="Apple" ##Class variable
#     noOfEmployee=0 ##Class Variable
#     def __init__(self,name):
#         self.name=name
#         self.raise_amount=0.02 ##instance variable
#         Employee.noOfEmployee+=1
#     def showDetails(self):
#         print(f"The name of the employee is {self.name} and raise amount in {Employee.noOfEmployee} sized company {self.CompanyName} is {self.raise_amount}")
# emp1=Employee("Diya")
# emp1.raise_amount=0.3
# emp1.CompanyName="Apple India"
# emp1.showDetails()
# Employee.CompanyName="Google" ##this will change class variable CompanyName value for all following cases
# print(Employee.CompanyName)
# ##OR
# # Employee.showDetails(emp1)
# emp2=Employee("khyati")
# emp2.showDetails()

##Class Methods
# class Employee:
#     company="Apple"
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(f"The name is {self.name} and company is {self.company}")
#     @classmethod #this decorator will give cls-->class as first parameter and bring direct change in value of class variable
#     def changeCompany(cls,newCompany):
#         self.company=newCompany  
# e1=Employee("Diya")
# e1.show()
# # Employee.company="Google" ##changed the value of classs variable
# e1.changeCompany("Tesla") ##changed value of class variable for that particular instance
# e1.show()
# e2=Employee("Khyati")
# Employee.show(e2)
# e3=Employee("Namish")
# Employee.show(e3)

##Class Methods as alternative to constructors
##eg1
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     @classmethod
#     def fromStr(cls,string):
#         return cls(string.split("-")[0],string.split("-")[1])
# e1=Employee("Diya",200000)
# print(e1.name)
# print(e1.salary)
# string="Khyati-300000"
# e2=Employee.fromStr(string)
# # e2=Employee(string.split("-")[0],int(string.split("-")[1]))
# print(e2.name)
# print(e2.salary)

# ##eg 2:
# class Rectangle:
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     @classmethod
#     def square(cls,size):
#         return cls(size,size)
# sq=Rectangle.square(3)
# print(sq.width)
# print(sq.height)

##Eg 3:
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     @classmethod
#     def from_string(cls,string):
#         name,age=string.split(",")
#         return cls(name,int(age))
# person=Person.from_string("Diya,19")
# print(person.name)
# print(person.age)

##dir()
# x=[1,2,3]
# print(dir(x)) ## will tell all methods and attributes of x
# print(x.__add__) ##will tell about __add__

##__dict__ method:returns dictionary representation of object attributes
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p=Person("Diya",19)
# print(p.__dict__) ##all self one will be included in the dictionary
# print(help(Person)) ##help() method

##help() method:
# print(help(str))

##super keyword: it is used to refer to parent class
##example 1:
# class ParentClass:
#     def parent_method(self):
#         print("This is a parent method")
# class ChildClass(ParentClass):
#     # def parent_method(self):
#     #     print("Diya")
#     #     super().parent_method() #3calls parent class ka parent_method
#     def child_method(self):
#         print("This is a child method")
#         super().parent_method() #3calls parent class ka parent_method
# child_object=ChildClass()
# child_object.child_method()
# child_object.parent_method() ##calls parent_method of ChildClass but if ChildClass mein nhi hoga toh ParentClass ka directly call krdega

##example 2:
# class Employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
# class Programmer(Employee):
#     def __init__(self,name,id,lang):
#         # self.name=name
#         # self.id=id
#         super().__init__(name,id) ##super() keyword will help to access the parent class methoids
#         self.lang=lang
# Rohan=Employee("Rohan","420")
# Diya=Programmer("Diya","2345","Python")
# print(Diya.name)
# print(Diya.id)

##Magic/Dunder methods: these are special methods you can define in your class and when included they give powerful waay to manipulate objecyts and their behaviour
# class Employee:
#     # name="Diya"
#     def __init__(self,name):
#         self.name=name
#     def __len__(self):
#         i=0
#         for c in self.name:
#             i+=1
#         return i
#     def __str__(self):
#         return f" The name of the employee is {self.name} str"
#     def __repr__(self):
#         return f" The name of the employee is {self.name} repr"
#     def __call__(self):
#         print("hey!")
# e=Employee("Diya")
# print(e.name)
# print(len(e.name))
# print(len(e)) ##__len__
# print(e) ## will provide info about e i.e. its location but if str is used then that will be printed even if repr is present. if str not present the repr will be executed
# print(str(e)) ##__str__
# print(repr(e)) ##__repr__
# e() ##__call__ method
##__init__ method: constriuctor+ special method automatically ccalled when u create a new instance and it is here we define object variables
##__str__  and __repr__ method: used to convert an object to string representation. "str is used when u want to print out an object" and "repr is used when u want to get a string representation of an object that can be used to recreate the object"
##call method : the call method  is used to make  an object callable, meaning that u can pass it as a parameter to a function is called. This is incredibly powerful tool that allows  u to create objects that behave that functions.

## Method overriding:how to change method of parent class from child class. allows u to redefine a method in a derived class. The method in derived class is saild to override the method in bse class.
# class Shape:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def area(self):
#         return self.x*self.y
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
#         super().__init__(radius,radius)
#     def area(self):###Method Overriding
#         # return 3.14* self.radius*self.radius
#         return 3.14*super().area()
# rec=Shape(3,5)
# print(rec.area())
# c=Circle(5)
# print(c.area())

##Operator Overloading: it allows developors to define the custom behavior for operators for objects of custom classes
# class Vector:
#     def __init__(self,i,j,k):
#         self.i=i
#         self.j=j
#         self.k=k
#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
#     def __add__(self,x):
#         # return f"{self.i+x.i}i + {self.j+x.j}j + {self.k+x.k}k" ##it is returning us string but not vector
#         return Vector(self.i+x.i,self.j+x.j,self.k+x.k) ##This will return it as vector type
# v1=Vector(3,5,6)
# print(v1)
# v2=Vector(1,2,9)
# print(v2)
# print(v1+v2)
# print(type(v1+v2))

##eg2:
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     # Overloading the addition operator '+'
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
    
#     # Overloading the equality operator '=='
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
    
#     # Overloading the string representation operator '__str__'
#     def __str__(self):
#         return f"({self.x}, {self.y})"

# # Creating instances of Point class
# point1 = Point(1, 2)
# point2 = Point(3, 4)

# # Adding two Point objects
# result = point1 + point2
# print("Sum of two points:", result)

# # Checking equality of two Point objects
# print("Are the points equal?", point1 == point2)

# print(point1) ##__str__

#3single inheritance:common type Syntax: class ChildClass(ParentClass):#class body
# class Animal:
#     def __init__(self,name,species):
#         self.name=name
#         self.species=species
#     def make_sound(self):
#         print("Sound made by animal")
# class Dog(Animal): ##single inheritance
#     def __init__(self,name,breed):
#         # Animal.__init__(self,name,species="Dog")
#         super().__init__(name,species="Dog")
#         self.breed=breed
#     def make_sound(self): ## Method overriding
#         print("Bark")
# class Cat(Animal):
#     def __init___(self,name,breed):
#         self.breed=breed
#         super().__init__(name,species="Cat")
#     def make_sound(self): ##Method Overriding
#         print("Meow!")
# d=Dog("Tom","P")
# d.make_sound()
# c=Animal("John","Multi")
# c.make_sound()

##Multiple Inheritance: allows class to inherit attributes and methods from multiple parent classes.
##Syntax: class ChildClass(ParentClass1,ParentClass2,ParentClass3):#classbody
##eg1:
# class Employee:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(f"The name is {self.name}")
# class Dancer:
#     def __init__(self,dance):
#         self.dance=dance
#     def show(self): 
#         print(f"The dance is {self.dance}")
# class DancerEmployee(Dancer,Employee):
#     def __init__(self,dance,name):
#         self.dance=dance
#         self.name=name
# o=DancerEmployee("Kathak","Diya")
# print(o.name)
# print(o.dance)
# o.show() ##Pehle wala show() print hoga DancerEmployee(Employee,Dancer) or DancerEmployee(Dancer,Employee)
# print(DancerEmployee.mro()) #3mro stands for method resolution order

##mro stands for order in which python searches for methods and attributes in class hierarchy
# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B, C):
#     pass
# print(D.mro())

##MultiLevel Inheritance: dada ji-->papa ji --> beti
#Syntax:class BaseClass:
##        #Base class code
##      class DerivedClass1(BaseClass):
##        #Derivedclass1 code
##      class DerivedClass22(DerivedClass1):
##        #Derivedclass2code

# class Animal:
#     def __init__(self,name,species):
#         self.name=name
#         self.species=species
#     def show_detail(self):##5th
#         print(f"Name:{self.name}")
#         print(f"Species:{self.species}")
# class Dog(Animal):
#     def __init__(self,name,breed):
#         Animal.__init__(self,name,species="Dog")
#         self.breed=breed
#     def show_detail(self):##3rd
#         Animal.show_detail(self) ##4th
#         print(f"Bread:{self.breed}") ##6th
# class GoldenRetriever(Dog):
#     def __init__(self,name,color):
#         Dog.__init__(self,name,breed="Golden Retriever")
#         self.color=color
#     def show_detail(self): ##first will come here
#         Dog.show_detail(self) #2nd
#         print(f"Color:{self.color}") ##7th
# # o=GoldenRetriever("tommy","Black")
# o=Dog("Tommy","Dog")
# o.show_detail()
# print(GoldenRetriever.mro())

###Hybrid Inheritance:Combination of two or more inheritances
# class BaseClass:
#     pass
# class Derived1(BaseClass): ##single inheritance
#     pass
# class Derived2(BaseClass):
#     pass
# class Derived3(Derived1,Derived2): ##multiple inheritance
#     pass

###Hierarchical Inheritance: where multiple subclasses inherit from a single base class. Single BaseClass --> Parent Class
# class BaseClass:
#     pass
# class D1(BaseClass):
#     pass
# class D2(BaseClass):
#     pass
# class D3(D1):
#     pass

##Creating Command line utilitues in python: These are the programs that can be run from terminal or command line interface. In python we can create our own command line utilities using built-in argparse methods
##Command Line: Prompt, shell ,terminal
# import argparse ##module used to create command line utilities
# import sys ##module to print on prompt
# def calc(args):
#     if args.o=='add':
#         return args.x+args.y
#     elif args.o=='mul':
#         return args.x*args.y
#     elif args.o=='sub':
#         return args.x-args.y
#     elif args.o=='div':
#         return args.x/args.y
#     else:
#         print("Something went wrong")
# parser=argparse.ArgumentParser() ##ArgumentParser() is a class in argparse
# parser.add_argument('--x',type=float,default=1.0,help="Enter the first number= . This is utility for calculation. Please Contact Diya") ##Command line mein argument add krna chahte hain
# parser.add_argument('--y',type=float,default=1.0,help=" Enter second number= . This is utility for calculation. Please Contact Diya") ##Command line mein argument add krna chahte hain
# parser.add_argument('--o',type=str,default="add",help=" This is utility for calculation. Please Contact Diya") ##Command line mein argument add krna chahte hain
# args=parser.parse_args() ##yeh saare arguments ko parse kr deta hai
# sys.stdout.write(str(calc(args))) ##arguments ko calculatee krega phir use string mein convert krega and sys.stdout.write usse prompt pr print krwayega

##walrus Operator(:=) : helps in doing assignment in expression
# eg1:
# a=True
# print(a:=False)

#eg2:
# numbers=[1,2,3,4,5]
# while (n:= len(numbers))>0:
#     print(numbers.pop())

#eg3:
# names=["John","Jane","Jim"]
# if (name:=input("Enter a name:") )in names:
#     print(f"Hello,{name}!")
# else:
#     print("Name not found!")

#eg4:
# foods=list()
# while True:
#     food=input("What food do you like?:")
#     if food=="quit":
#         break
#     foods.append(food)
# print(foods)
         ##Or
# foods=[]
# while(food:=input("What food do u like?:") != "quit"): ##precedencee of walrus operator is less than assignment operator
#     foods.append(food)

##walrus operator v/s assignment operator:
# Using both operators in the same expression
# x = 5
# y = 10
# # result = (x := 2) + (y = 5)  # This line will raise a SyntaxError due to incorrect syntax
# # The correct usage would be:
# result = (x := 2) + (y := 5)
# print(result)  # Output: 7
# print(x, y)    # Output: 2 5

##shutil module: it provides high level interface for working with file and directories. It is short name for shell utility. shutil:sh--> shell + util-->utility
##It is used to automate tasks that are commonly performed on files and directories
# import shutil
# shutil.copy("async.py","os.py") ##copy async.py in os.py
# shutil.copy("async.py","main2.py") ##create main2.py and copy async.py in it
##shutil.copy2(src,dst):function is similar to copy, but preserves more metadata like timestamps
##shutil.copytree(src,dst):function recursively copies the directory located at src to new location specified by dst. if dst location already exists the original directory will be mergged with it
##shutil.move(src,dst): moves the file locatewd at src to new location specified by dst. equivalent to renaming a file.abs
##shutil.copy() and shutil.copy2() used for files and shutil.copytree() used for folders
##shutil.rmtree(path): function recursively deletes directory located at path along with all of its content)
##shutil.rmtree(): is used to delete folder
##to delete file we need to use os module: os.remove("file_name")

##Request module:module in http library and is to send https requests
##bs4 module

# import requests
# from bs4 import BeautifulSoup
# response=requests.get("https://www.codewithharry.com") ##html code
# print(response) ##print HTTP status code indicating success
# print(response.text) #HTML markup, text, and other elements retrieved from the URL
# soup=BeautifulSoup(response.text,'html.parser') # parsing the HTML content retrieved from the URL..##In Python, parsing is process of analyzing structured data, code, to extract relevant information or to transform it into a more usable format. 
# So, 'html.parser' in this context means that BeautifulSoup will use Python's built-in HTML parser to parse the HTML content fetched from the URL provided (response.text).
# print(soup)
# print(soup.prettify()) ## The prettify() method adds indentation and line breaks to make the HTML content more readable when printed.
# for heading in soup.find_all("h2"):
#     print(heading.text)
# response=requests.get("https://www.google.com") #sends get request to Google Homepage

# a "response object" refers to the object returned by making an HTTP request using the requests.get(), requests.post(), or similar functions. 
# This object contains information about the HTTP response received from the server.
# The response object typically includes attributes such as:
# Status code: An integer representing the HTTP status code of the response (e.g., 200 for "OK", 404 for "Not Found", etc.).
# Headers: A dictionary containing the HTTP headers sent by the server in the response.
# Content: The body of the HTTP response, which can be accessed in various formats such as bytes, a string, or a JSON object, depending on the response content type.
# Additionally, the response object may include other attributes or methods for interacting with the response data, such as accessing cookies, redirects, or streaming content.
# Metadata refers to data that provides information about other data. In simpler terms, it's data about data. In various contexts, metadata serves to describe characteristics of the primary data, helping to organize, find, interpret, and manage it efficiently.
# HTTP stands for Hypertext Transfer Protocol. It is an application protocol used for transmitting hypermedia documents, such as HTML files, over the World Wide Web. HTTP is the foundation of data communication on the web and is used by web browsers and web servers to communicate with each other.


###Generators: are special type of functions that allow u to create an iterable sequence of values. Memory Friendly
# It returns a generator object, which can be used to generate values one by one as u iterate over it. They allow u to generate values on fly, Rather than storing entire sequence in memory.
# def my_generator(): #in this way all the values are not stored but if we would return a list then values were to be stored that is memory was to be used. It is powerful tool for working with complex data sets.
#     for i in range(5):
#         yield i #instead of return. in python generator is created by using yield. yield returns the value from generator and suspends the execution of func until next value is req. Values are generated only when they are requested.
# gen=my_generator()
# #using next keyword
# print(next(gen)) #0
# print(next(gen))#1
# print(next(gen))#2
# print(next(gen))#3
# print(next(gen))#4
# ##or
# for j in gen:
#     print(j)

##function caching:Program maintains cache i.e remembers result for particular value
##expensive function:function having complex computation and taking more time for execution
#use function caching if we know fuction is only for limited values i.e. domain and if it is computational expensive
#3donot maintain cache if we know values are hardly going to be repeated
# import functools
# import time
# @functools.lru_cache(maxsize=None) #program will get memoize for particular value. lru_cache apne aap mein bhi memory le rhi hai
# ##memoize:To store so that it can be subsequently retrieved without repeating the computation.
# #cache is maintained only for one run of the program
# def fx(n):
#     time.sleep(5)
#     return n*5
# print(fx(20))
# print("done for 20")
# print(fx(2))
# print("done for 2")
# print(fx(6))
# print("done for 6")
###now the code will run superfast as compared to before
# print(fx(20))
# print("done for 20")
# print(fx(2))
# print("done for 2")
# print(fx(6))
# print("done for 6")
      ###or
# from functools import lru_cache
# import time
# @lru_cache(maxsize=None)
# def fx(n):
#     time.sleep(5)
#     return n*5
# print(fx(20))
# print("done for 20")
# print(fx(2))
# print("done for 2")
# print(fx(6))
# print("done for 6")


###Regular expressions:"regex" are powerful tool for working with strings and text data.
#They allow to match and manipulate strings based on patterns, making it easy to perform complex string operations with just few lines of code.
# [] Represent character class
# ^ Matches the beginning
# $ Matches the end
# . Matches any character except newline
# ? Matches zero or one occurence
# | Means OR (Matches with any of character seoarated by it)
# * Any number of occurences (including 0 occurences)
# + One or more occurences

##regexr.com
# import re
# pattern=r"[A-Z]+nstagram"##we can even use in keyword but for complex we need to use regular expressions
# text='''4Nw&list=PLu0W_9lII9ahKZ42vg2w9ERPmShYbYAB7 JavaScript[1 Hr]: https://www.yo
# utube.com/watch?v=onbBV0uFVpo&list=PLu0W_9lII9ahKZ42vg2w9ERPmShYbYAB7 C[1.3 Hr]-https://www.youube.com/watch?v=YXcgD8hRHYY&list=PLu0W_9lII9ahKZ42vg2w9ERPmShYbYAB7 php[1 Hr]: https://www.youtube.com/watch?v=xW7ro3lwaCI&list=PLu0W_9lII9ahKZ42vg2w9ERPmShYbYAB7 php[2.3 Hr]:https://www.youtube.com/watch?v=1SnPKhCdlsU&list=PLu0W_9lII9ahKZ42vg2w9ERPmShYbYAB7 php[Project]- https://www.youtube.com/watch?v=-al2bECumKg&list=PLu0W_9lII9ahKZ42vg2w9ERPmShYbYAB7 HTML[30 Min]:https://www.youtube.com/watch?v=E3ByCRqE7Lo&list=PLu0W_9lII9ahKZ42vg2w9ERPmShYbYAB7 CSS[8.5 Hr]:https://www.youtube.com/watch?v=Edsxf_NBFrw&list=PLu0W_9lII9ahKZ42vg2w9ERPmShYbYAB7 CSS[1.4 Hr]:https://www.youtube.com/watch?v=u5-K_ua9sOw&list=PLu0W_9lII9ahKZ42vg2w9ERPmShYbYAB7 Wordpress[3.2 Hr]:https://www.youtube.com/watch?v=GlLRYml8mCY&list=PLu0W_9lII9ahKZ42vg2w9ERPmShYbYAB7 Angular[2 Hr]:https://www.youtube.com/watch?v=0LhBvp8qpro&list=PLu0W_9lII9ahKZ42vg2w9ERPmShYbYAB7 Java[2.3 Hr]:https://www.youtube.com/watch?v=rV_3Lewxx6o&list=PLu0W_9lII9ahKZ42vg2w9ERPmShYbYAB7 Web Scraping[1 Hr]:https://www.youtube.com/watch?v=uufDGjTuq34&list=PLu0W_9lII9ahKZ42vg2w9ERPmShYbYAB7 MongoDB[2 Hr]:https://www.youtube.com/watch?v=oSIv-E60NiU&list=PLu0W_9lII9ahKZ42vg2w9ERPmShYbYAB7 Numpy[1 Hr]:https://www.youtube.com/watch?v=Rbh1rieb3zc&list=PLu0W_9lII9ahKZ42vg2w9ERPmShYbYAB7 Android Dev[12 Hr]- https://www.youtube.com/watch?v=mXjZQX3UzOs Linux[1 Hr]:https://www.youtube.com/watch?v=_tCY-c-sPZc&list=PLu0W_9lII9ahKZ42vg2w9ERPmShYbYAB7 JQuery[1.1 Hr]:https://www.youtube.com/watch?v=YFlx1C8XwR0&list=PLu0W_9lII9ahKZ42vg2w9ERPmShYbYAB7 Git and GitHub[1.1 Hr]:https://www.youtube.com/watch?v=gwWKnnCMQ5c&list=PLu0W_9lII9ahKZ42vg2w9ERPmShYbYAB7 ►Complete course [playlist]: React: https://www.youtube.com/playlist?list=PLu0W_9lII9agx66oZnT6IyhcMIbUMNMdt Python-https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME OOP Python-https://www.youtube.com/playlist?list=PLu0W_9lII9ahfRrhFcoB-4lpp9YaBmdCP Java:https://www.youtube.com/playlist?list=PLu0W_9lII9agS67Uits0UnJyrYiXhDS6q JavaScript- https://www.youtube.com/playlist?list=PLu0W_9lII9ajyk081To1Cbt2eI5913SsL PHP-https://www.youtube.com/playlist?list=PLu0W_9lII9aikXkRE0WxDt1vozo3hnmtR C-https://www.youtube.com/playlist?list=PLu0W_9lII9aiXlHcLx-mDH1Qul38wD3aR C++-https://www.youtube.com/playlist?list=PLu0W_9lII9agpFUAlPFe_VNSlXW5uE0YL Git & GitHub-https://www.youtube.com/playlist?list=PLu0W_9lII9ahVQekD7ePHmnirTePXwIln Android Dev- https://www.youtube.com/playlist?list=PLu0W_9lII9aiL0kysYlfSOUgY5rNlOhUd Python GUI- https://www.youtube.com/playlist?list=PLu0W_9lII9ajLcqRcj4PoEihkukF_OTzA Web Development- https://www.youtube.com/playlist?list=PLu0W_9lII9agiCUZYRsvtGTXdxkzPyItg Python Django:https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9 Projects Using HTML, CSS & Javascript- https://www.youtube.com/playlist?list=PLu0W_9lII9aiQiOwthuSvinxoflmhRxM3 Data Structure and Algo:https://www.youtube.com/playlist?list=PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi Follow Me On Social Media ►Website (created using Django Rest & Angular): https://www.codewithharry.com ►Facebook: https://www.facebook.com/CodeWithHarry ►
# Instagram: https://www.instagram.com/codewithharry/ Twitter: https://twitter.com/CodeWithHarry Comment "#HarryBhai" if you read this'''
# # match=re.search(pattern,text) ##pehle search pr ruk jaata hai
# # print(match)
# matches=re.finditer(pattern,text)
# for match in matches: #will provide all the matches
#     print(match)
#     print(match.span()) #span means range of values or indices within a sequence
#     print(type(match.span())) #tuple