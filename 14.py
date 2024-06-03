# import sys
# args=sys.argv[1:]
# print("Number of command line arguments=",len(args))
# print("list of cmd line arguments=",args)

# import sys
# def odd_even(num):
#     if num%2==0:
#         return "even"
#     else: 
#         return "odd"
# args=sys.argv[1:]

# if len(sys.argv)!=6:
#     print("Inputs are not complete.")
# input_values=[]
# count=0
# try:
#     for arg in args:
#         count+=1
#         input_values.append(int(arg))
# except:
#     print(f"Data type of {count} should be integer")

# for value in input_values:
#     print(f"{value} is {odd_even(value)}")

# import sys
# def odd_even(num):
#     if num%2==0:
#         return "even"
#     else: 
#         return "odd"
# args=sys.argv[1:]
# count=0
# input_values=[]
# if len(sys.argv)==6:
# ##ek baar try mein exception aagaya then rest of statements will not work
#     try:
#         for arg in args:
#             count+=1
#             input_values.append(int(arg))
#     except:
#         print(f"Data type of {count} should be integer")
# else:
#     print("number of args are in complete")
# for value in input_values:
#     print(f"{value} is {odd_even(value)}")
#4:
# try:
#     f=open("diya.txt","r")
# except FileNotFoundError:
#     print("File not found")
 # FileNotFoundError specifically indicates that the file does not exist, whereas 
# IOError is a more general exception that can be raised for various input/output-related issues beyond just the absence of a file.

#attempting to read from close file:
# try:
#     file = open("myfile.txt", "r")
#     file.close()
#     content = file.read()  # Raises IOError: File not open for reading
# except IOError:
#     print("Error: Input/Output error occurred.")

##attempting to write to read only file
# try:
#     file = open("readonlyfile.txt", "r")
#     file.write("This will raise an IOError")
# except IOError:
#     print("Error: Input/Output error occurred.")
# finally:
#     file.close()

#file permission issues: program doesnot have necessary permissions to perform requested file operation

##3:
# import getopt
# import sys
# name = []
# age = []
# cgpa = []

# argv = sys.argv[1:]
# opts, args = getopt.getopt(argv, "n:a:c", ["name=", "age=", "cgpa="])
# for opt, arg in opts:
#     if opt in ['-n', '--name']:
#         name.append(arg)
#     elif opt in ['-a', '--age']:
#         age.append(int(arg))
#     elif opt in ['-c', '--cgpa']:
#         cgpa.append(float(arg))

# print(name)
# print(age)
# print(cgpa)

# max_age = 0
# max_cgpa = 0

# # for ag, cg in zip(age, cgpa):
#     if ag > max_age:
#         max_age = ag
#     if cg > max_cgpa:
#         max_cgpa = cg

# print("max cgpa=", max_cgpa)
# print("max age=", max_age)
# import sys
# import getopt
# name=[]
# age=[]
# cgpa=[]
# argv=sys.argv[1:]
# opts,args=getopt.getopt(argv,"n:a:c",["name=","age=","cgpa="])
# for opt,arg in opts:
#     if opt in ['-n','--name']:
#         name.append(arg)
#     elif opt in ['-a','--age']:
#         age.append(int(arg))
#     elif opt in ['-c','--cgpa']:
#         cgpa.append(float(arg))
# print(name)
# print(age)
# print(cgpa)
# max_age=0
# max_cg=0
# for ag,cg in zip(age,cgpa):
#     if ag>max_age:
#         max_age=ag
#     if cg>max_cg:
#         max_cg=cg
# print("max cgpa=",max_cg)
# print("max age=",max_age)

##4:
# try:
#     name="Diya"
#     print(nme)
# except NameError:
#     print("Variable is not defined")

##4:
# try:
#     print(4+"hello")
# except TypeError:
#     print("TypeError")


###very important difference between typeerror and attribute error:
# my_list = []
# my_list.append(5)  # Works fine
# my_list.extend("hello") #typeerror
# tup=()
# tup.append(5)##attributeerror

# try:
#     name="diya"
#     print(int(name))
# except Exception as e:
#     print(e)

##5:with raise keyword it is important to write inbuit-module
# n=int(input("Enter any number="))
# if n<0:
#     raise ValueError("no numbers below zero are acceptable")

##6:if we write in this way raise will not be executed
# as open itself will raise error
# f=open("dioya.txt","r")
# raise FileNotFoundError("File donot exits")

# try:
#     f=open("dioya.txt","r")
# except FileNotFoundError:
#     raise FileNotFoundError("File donot exits")

##7:
# try:
#     file = open("myfile.txt", "r")
#     file.close()
#     content = file.read()  # Raises IOError: File not open for reading
# except IOError:
#     print("Error: Input/Output error occurred.")

#8
# If there are multiple except blocks after the try block, Python will execute the code inside the first matching except block and then move on.
#  Other except blocks will not be executed.
# import math
# try:
#     answer=math.sqrt(-9)
#     result=math.sqrt(2,3)
# except ValueError:
#     print("Error")
# except TypeError:
# #     print("Type error")
# import math
# try:
#     result=math.sqrt(2,3)
# except TypeError:
#     print("Type error")

##9
# try:
#     list1=[1,2,3]
#     list1.append(4)
#     tup=()
#     tup.append(4)
# except AttributeError:
#     print("attribute error")

###getopt() module:
#syntax-->getopt.getopt(args,options,[long options])
#args-->list of arguments to be passed
#options-->a:b:c or ab:c: or colon is used which reqires argument
#long_options-->list of string. options that require arguments are followed by (=)
# opts,args=getopt.getopt(args,options,[long options])
#opts-->list of (option,value) pairs
#args-->list of extra arguments

##1:
# import sys 
# import getopt 
# def full_name(): 
#     first_name = None
#     last_name = None
#     argv = sys.argv[1:] 
#     try: 
#         opts, args = getopt.getopt(argv, "f:l:") 
#     except: 
#         print("Error") 
#     for opt, arg in opts: 
#         if opt in ['-f']: 
#             first_name = arg 
#         elif opt in ['-l']: 
#             last_name = arg 
#     print( first_name +" " + last_name) 
# full_name() 

##2:all wanted and nunwanted list of arguments will be stored in argv
# unwanted in args such as with which -f or -l is not specified
# import sys 
# import getopt 
# def full_name(): 
#     first_name = None
#     last_name = None
#     argv = sys.argv[1:] 
#     try: 
#         opts, args = getopt.getopt(argv, "f:l:",  ["first_name =","last_name ="]) 
#     except: 
#         print("Error")
#     for opt, arg in opts: 
#         if opt in ['-f', '--first_name']: 
#             first_name = arg 
#         elif opt in ['-l', '--last_name']: 
#             last_name = arg 
#     print( first_name +" " + last_name) 
#     print(argv)
#     print(args)
# full_name() 


###type error:
# x = 5
# y = "hello"
# z = x + y

# def fun(a):
#     if a < 4:
#         b = a/(a-3)
#     print("Value of b = ", b)
# try:
#     # fun(3)
#     fun(5)
# except ZeroDivisionError:
#     print("ZeroDivisionError Occurred and Handled")
# except NameError:##as python tries to access value of b
#     print("NameError Occurred and Handled")

# try: 
#     raise NameError("Hi there")
# except NameError:
#     print ("An exception")
#     raise ###re-raise the same exception: runtime error


##this shows once we get error in try block then rest of statements in try block are not executed
# import math
# try:
#     # result1=math.sqrt(2,3)
#     result2=math.sqrt(-2)
#     print("3")
# except ValueError:
#     print("ValueError")
# except TypeError:
#     print("Error")
