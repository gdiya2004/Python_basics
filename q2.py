# x = 2
# y = 3
# print("ADDITION RESULT : ", x + y)

# x = 2
# y = 3.3
# print("ADDITION RESULT : ", x + y) # both float and int type are accept

# x = 2.7
# y = 3.3
# print("ADDITION RESULT : ", x + y) # both float type are accept

# x = "2"
# y = 3
# print("ADDITION RESULT : ", x + y) #str type and int can't be added.

# x = "2"
# y = "3"
# print("ADDITION RESULT : ", x + y) # concatenation will take place

# x = "2"
# y = 4.8
# print("ADDITION RESULT : ", x + y) # float type and str typr can't be added.

# x = 2
# y = bool(4.8)
# print("ADDITION RESULT : ", x + y) #here bool(4.8) returns True i.e, 1

# x = "2"
# y = bool(4.8)
# print("ADDITION RESULT : ", x + y) #bool type cant be concatenated.

# x = "2"
# y = str(bool(4.8))
# print("ADDITION RESULT : ", x + y)
# #bool returns 1 generally but we converted into str then it gives True

# x = "2"
# y = str(complex(4.8)) #Here both strings so concatenation will take place
# print("ADDITION RESULT : ", x + y)

# x = 2
# y = complex(4.8)
# print("ADDITION RESULT : ", x + y)
# # here both are int type so addtion will take place

# a = 30
# b = 10
# print("Subtraction result : ",a-b)

# a = 30
# b = "10"
# print("Subtraction result : ",a-b)

# a = "30"
# b = "10"
# print("Subtraction result : ",a-b)
# # can not perform subtraction on str type operands.

# a = 20
# b = 10.00
# print("Subtraction result : ",a-b)

# a = 20
# b = bool(10)
# print("Subtraction result : ",a-b)

# num1 = 23
# num2 = 35
# print("MULTIPLICATION RESULT : ",num1 * num2)

# num1 = 23
# num2 = 35.0
# print("MULTIPLICATION RESULT : ",num1 * num2)

# num1 = "23"
# num2 = 5
# print("MULTIPLICATION RESULT : ",num1 * num2) # 23 string will prints 5 times

# num1 = "23"
# num2 = "5"
# print("MULTIPLICATION RESULT : ",num1 * num2)

# l = "(1,2,3,4)"
# print(float(l * 5))


# l = "abc"
# print(float(l * 4))
# #initially it will prints string 5 times and converts it into float

# l = "123"
# b = 2.3
# print("MULTIPLICATION RESULT : ", l * b)

# l = "123"
# b = bool(2.3)
# print("MULTIPLICATION RESULT : ", l * b)

# l =[1,2,3]
# m = [2,4,5]
# print(l * m) # multiplication of two list data types is not possible

# l = (5,6,7)
# m = (1,2,3)
# print(l* m) # multiplication of two tuple data types is not possible

# l = bool(1)
# m = bool(4657)
# print(l * m) # as bool returns 1 it prints only one time

# l = bool()
# m = bool(123456789)
# print(l*m) # As bool doesn't contain any value it consider as zero.

# l = str(bool([1,2,3]))
# m = 99
# print(l*m)

# l =str(bool([]))
# m = 99
# print(l*m)

# a = 3
# b = 45
# print("Division result : ", a/ b) # returns float value

# a = 3
# b = "45"
# print("Division result : ", b / a)

# a = 3
# b = 45.0000
# print("Division result : ", b / a)

##zerodivision error
# a = 3
# b = bool(0.0000)
# print("Division result : ", a / b)

# a = 3
# b = complex((90))
# print("Division result : ", a / b)

# a = [1,2,3]
# b = [7,8,9]
# print("Division result : ", a / b)

# a = (1,2,3)
# b = (1,2,3)
# print("Division result : ", a / b)

# a = {1,2,3}
# b = {1,2,3}
# print("Division result : ", a / b)

# !!!! in case of division answer is in terems of float always
# print(9/3)
# print(9+3)
# print(9-3)
# print(9*3)
# print(9%3)
# print(3**2)

##remember division gives float output
# l = bool()
# m = bool(9)
# print(l / m)

# l=25
# m=5
# print(l/m)

##modulus donot give default answer in float
# a = 3
# b = 4
# print(a%b)
# print(b%a)


# print(10/2)
# print(10/3)
# print(10//2)
# print(10.0/3)
# print(10.0//3)
# print(10//3)
# print(10.0//3.0)
# print(20/2)
# print(20.5/2)
# print(20//2)
# print(20.5//2)
# print(30//2)
# print(30.0//2)

# print(10**2) # meaning of this is 10 to the power 2
# print(3**3)

# a = 10
# b = 20
# print('a < b is', a<b)
# print('a <= b is', a<=b)### a<=b means either a<b or a=b
# print('a > b is', a>b)
# print('a >= b is', a>=b)

# print(ord('a'))
# print(ord('A'))
# print(ord('z'))
# print(ord('Z'))

# print(chr(97))
# print(chr(65))

# print('python' and '0') 
# print('0' and 'python') 

#  #uppercase<lowercase lexicographical order/dictionary order
# s1 = 'nitj' # ASCII value of 'a' is 97
# s2 = 'Nitj' # ASCII value of 'b' is 98
# print(s1<s2)
# print(s1<=s2)
# print(s1>s2)
# print(s1>=s2)

# s1 = 'nitj'
# s2 = 'nitj'
# print(s1<s2)
# print(s1<=s2)
# print(s1>s2)
# print(s1>=s2)
# print(s1==s2)
# print(s1 is s2)

# s1 = 'nitj'
# s2 = 'Nitj'
# print(s1<s2)
# print(s1<=s2)
# print(s1>s2)
# print(s1>=s2)

# print(True > False)
# print(True >= False) # True ==> 1
# print(True < False) # False ==> 0
# print(True <= False)

# print(0>1)
# print(0<1)

##string cannot be compared with integer
# print(10 > 'nitj')

# a = 10
# b = 20
# if a>b:
#    print('a is greater than b')
# else:
#    print('a is not greater than b')

# print(10<20)
# print(10<20<30)
# print(10<20<30<40)
# print(10<20<30<40>50) 

# print(10==20)
# print(10!=20)
# print(1==True)
# print(10==10.0)
# print('nitj'=='nitj')

##(==) can be used to compare incompatible datatypes but notr rest relational can be used like >,<,<=,>=
# print(10=='nitj')
# print(10=='10')

# print(10==20==30==40)
# print(10==10==10==10)

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# print(not True)
# print(not False)

# userName = input('Enter User Name : ')
# password = input('Enter Password : ')
# if userName == 'nitj' and password == 'students':
#     print('valid User')
# else:
#     print('invalid user')

# userName = input('Enter User Name : ')
# password = input('Enter Password : ')
# if userName == 'nitj' and password == 'students':
#      print('valid User')
# else:
#      print('invalid user')

# print(10 and 20)
# print(0 and 20)
# print('nitj' and 'students')
# print('' and 'nitj') # first argument is empty string
# print(' ' and 'nitj')# first argument contains space character, so it is not empty
# print('nitj' and '') # second argument is empty string
# print('nitj' and ' ')# second argument contains space character, so it is not empty

# print(10 or 20)
# print(0 or 20)
# print('nitj' or 'students')
# print('' or 'nitj') # first argument is empty string
# print(' ' or 'nitj')# first argument contains space character, so it is not empty
# print('nitj' or '') # second argument is empty string
# print('nitj' or ' ')

# ##logical not returns value in terms of true or false
# print(not 'nitj')
# print(not '')
# print(not 0)
# print(not 10)

# print(10.5 & 20.6) ##bitwise and cannot be used with float operands :Typeerror
# print('nitj' | 'nitj') ##bitwise donot support string Typeerror
# print(bin(10))##remember output will begin from 0b as hexadecimal begin with 0x
# print(bin(20))
# print(10 & 20) # Valid
# print(10.0 & 20.0) # In valid

##in this case of bitwise operators answer is in the form of  true/false
# print(True & False) #False
# print(True | False) #Ture
# print(True ^ False)  #True

##in this case of bitwise operators answer is in form of integers
# print(~True)#01-->10
# print(~False)#00-->11
# print(True<<2)#1<<2-->1*2*2
# print(True>>2)#1>>2-->0

# print(2^4)

# print(4 & 5) # 100 & 101    4
# print(4 | 5) # 100 | 101  5
# print(4 ^ 5) # 100 ^ 101  1
# print(~4) # 4 ==> 0100  ~4-->1011-->-8+3=-5
# print(~5) # -6

# print(~-4) # negative values are stored in the memory in 2's complement form.  3
# print(10<<2)  #40
# print(10>>2)  #2

# x = 10
# x += 20 # x = x + 20
# print(x)

# x = 10 # 1010
# x &= 5 # 0101
# print(x)

# x = 10
# x **= 2 # x = x**2
# print(x)

# x = 10
# print(++x)
# print(++++x) # Here, + and - are sign bits, not increment and decrement operators
# print(-x)
# print(--x)
# print(++++++++++++-x)
# print(-------------+x)

# a,b=23,43 
# if a>b:
#     c=50
# else:
#     c=100
# print(c)
# x =int(input("Enter First Number:"))
# y =int(input("Enter Second Number:")) 
# if x<y :
#    min=x
# else :
#     min=y
# print("Minimum Value:",min)

# a=int(input("Enter First Number:"))
# b=int(input("Enter Second Number:"))
# c=int(input("Enter Third Number:"))
# min=a if a<b and a<c else b if b<c else c
# print("Minimum Value:",min)

# a=int(input("Enter First Number:"))
# b=int(input("Enter Second Number:"))
# if a==b:
#    print("Both numbers are equal")
# else:
#  if a<b :
#     print("Second Number is greater")
#  else:
#     print("First Number is greater")

# a=10
# b=10
# print(a is b)
# x=True
# y=True
# print( x is y)

##id in case of string , integer remains same but not in case of list
# a="nitj"
# b="nitj"
# print(id(a))
# print(id(b))
# print(a is b)

##is identity operator compares id of 2 operands
# list1=["one","two","three"]
# list2=["one","two","three"]
# print(id(list1))
# print(id(list2))
# print(list1 is list2)
# print(list1 is not list2) # reference comaprison (is & is not)
# print(list1 == list2) # content comparison (==)

##even in case of tuple id is same
# list1=("one","two","three")
# list2=("one","two","three")
# print(id(list1))
# print(id(list2))
# print(list1 is list2)
# print(list1 is not list2) # reference comaprison (is & is not)
# print(list1 == list2)

##in case of set and list id changes
# list1={"one","two","three"}
# list2={"one","two","three"}
# print(id(list1))
# print(id(list2))
# print(list1 is list2)
# print(list1 is not list2) # reference comaprison (is & is not)
# print(list1 == list2)

##even in case of dixctionary id changes
# list1={'one':1,'two':2,'three':3}
# list2={'one':1,'two':2,'three':3}
# print(id(list1))
# print(id(list2))
# print(list1 is list2)
# print(list1 is not list2) # reference comaprison (is & is not)
# print(list1 == list2)

# x="hello learning Python is very easy!!!"
# print('h' in x)
# print('d' in x)
# print('d' not in x)
# print('python' in x) # case sensitivity
# print('Python' in x)

# list1=["sunny","bunny","chinny","pinny"]
# print("sunny" in list1)
# print("tunny" in list1)
# print("tunny" not in list1)

# print(3+10*2)
# print((3+10)*2)

# a=30
# b=20
# c=10
# d=5
# print((a+b)*c/d) # division operoator in Python always going to provide float value as result
# print((a+b)*(c/d))
# print(a+(b*c)/d)

# print(3/2*4+3+(10/5)**3-2)
# print(3/2*4+3+2.0**3-2)
# print(3/2*4+3+8.0-2)
# print(1.5*4+3+8.0-2)
# print(6.0+3+8.0-2)

# x=input("Enter value:")
# print(type(x))

# x=input("Enter First Number:")
# y=input("Enter Second Number:")
# i = int(x)
# j = int(y)
# print("The Sum:",i+j)

# x=int(input("Enter First Number:"))
# y=int(input("Enter Second Number:"))
# print("The Sum:",x+y)

# print("The Sum:",int(input("Enter First Number:"))+int(input("Enter Second Number:")))

# eno=int(input("Enter Employee No:"))
# ename=input("Enter Employee Name:")
# esal=float(input("Enter Employee Salary:"))
# eaddr=input("Enter Employee Address:")
# married=bool(input("Employee Married ?[True|False]:"))
# print("Please Confirm your provided Information")
# print("Employee No :",eno)
# print("Employee Name :",ename)
# print("Employee Salary :",esal)
# print("Employee Address :",eaddr)
# print("Employee Married ? :",married)

# x = (input('Enter Something : '))
# print(type(x))

# ##eval() gives nameerror in case of string
# y = eval((input('Enter Something : ')))
# print(type(y))

# print('nitj')
# print() # prints new line character
# print('students')

# print("Hello World")
# # We can use escape characters also.
# print("Hello \n World")
# print("Hello\tWorld")
# # We can use repetetion operator (*) in the string.
# print(10*"RGM")
# print("RGM"*10)
# # We can use the + operator also.
# print("RGM"+"CET")

# a,b,c=10,20,30
# print("The Values are :",a,b,c) # here, we are passing 4 arguments to the print function.

# a,b,c=10,20,30
# print(a,b,c) # 10 20 30
# print(a,b,c,sep=',') # 10,20,30
# print(a,b,c,sep=':') # 10:20:30
# print(a,b,c,sep='-') # 10-20-30
# print("Hello")
# print("Nitj")
# print("Students")

# print("Hello",end=' ')
# print("Nitj",end=' ') # if end is space character
# print("Students")

# print("Hello",end='')
# print("Nitj",end='') # if end is nothing
# print("Students")

# print('hello',end = '::')
# print('nitj',end = '****')
# print('students')

# print(10,20,30,sep = ':', end = '***')
# print(40,50,60,sep = ':') # default value of 'end' attribute is '\n'
# print(70,80,sep = '**',end = '$$')
# print(90,100)

# print('nitj' + 'students') # Concatanation
# print('nitj','students') # ',' means space is the seperator
# print(10,20,30)

# l=[10,20,30,40]
# t=(10,20,30,40)
# print(l)
# print(t)
# s="Nitj"
# a=6
# s1="java"
# s2="Python"
# print("Hello",s,"Your Age is",a)
# print("You are learning",s1,"and",s2)

# a=10
# b=20
# c=30
# print("a value is %i" %a)
# print("b value is %d and c value is %d" %(b,c))

# s="Nitj"
# list=[10,20,30,40]
# print("Hello %s ...The List of Items are %s" %(s,list))

# price = 70.56789
# print('Price value = {}'.format(price))
# print('Price value = %f'%price)
# print('Price value = %.2f'%price)

# name = "Nitj"
# salary = 100000
# sister = "Students"
# print("Hello {} your salary is {} and Your Sister {} is waiting".format(name,salary,sister))
# print("Hello {0} your salary is {1} and Your Sister {2} is waiting".format(name,salary,sister))
# print("Hello {1} your salary is {2} and Your Sister {0} is waiting" .format(name,salary,sister))
# print("Hello {2} your salary is {0} and Your Sister {1} is waiting" .format(salary,sister,name))
# print("Hello {x} your salary is {y} and Your Sister {z} is waiting" .format(x=name,y=salary,z=sister))
# a,b,c,d = 10,20,30,40 # print a=10,b=20,c=30,d=40
# print('a = {},b = {},c = {},d = {}'.format(a,b,c,d))

# if 10<20:
#  print('10 is less than 20')
# print('End of Program')

# name=input("Enter Name:")
# if name=="Nitj":
#  print("Hello Nitj Good Morning")
#  print("How are you!!!")
# name = input('Enter Name : ')
# if name == 'Nitj':
#  print('Hello Nitj! Good Morning')
# else:
#  print('Hello Guest! Good Morning')
#  print('How are you?')
# brand=input("Enter Your Favourite Brand:")
# if brand=="RC":
#  print("It is childrens brand")
# elif brand=="KF":
#  print("It is not that much kick")
# elif brand=="FO":
#  print("Buy one get Free One")
# else :
# # print("Other Brands are not recommended")

# a=int(input("Enter First Number:"))
# b=int(input("Enter Second Number:"))
# c=int(input("Enter Third Number:"))
# min= a if a<b and a<c else b if b<c else c
# print("Minimum Value:",min)

# a=int(input("Enter First Number:"))
# b=int(input("Enter Second Number:"))
# c=int(input("Enter Third Number:"))
# max=a if a>b and a>c else b if b>c else c
# print("Maximum Value:",max)


























