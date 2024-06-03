##(==) can be used to compare incompatible datatypes but notr rest relational can be used like >,<,<=,>=
# print(10=='nitj')
# print(10=='10')

##only division always returns float value

##logical not returns value in terms of true or false
# print(not 'nitj')
# print(not '')
# print(not 0)
# print(not 10)

# print(10.5 & 20.6) ##bitwise and cannot be used with float operands :Typeerror
# print('nitj' | 'nitj') ##bitwise donot support string Typeerror

##in this case of bitwise operators answer is in the form of  true/false
# print(True & False) #False
# print(True | False) #Ture
# print(True ^ False)  #True

# ##in this case of bitwise operators answer is in form of integers
# print(~True)#01-->10
# print(~False)#00-->11
# print(True<<2)#1<<2-->1*2*2
# print(True>>2)#1>>2-->0

# print(~4) # 4 ==> 0100  ~4-->1011-->-8+3=-5
# print(~-4) # negative values are stored in the memory in 2's complement form.  3
#1100-->-8+4=-4 now ~-4-->0011-->3

# x = 10
# print(++x)
# print(++++x) # Here, + and - are sign bits, not increment and decrement operators
# print(-x)
# print(--x)
# print(++++++++++++-x)
# print(-------------+x)

##even in case of dixctionary id changes
##in case of set and list id changes

##eval() gives nameerror in case of string
# y = eval((input('Enter Something : ')))
# print(type(y))

# a,b,c=10,20,30
# print("The Values are :",a,b,c) # here, we are passing 4 arguments to the print function.

# print(10,20,30,sep = ':', end = '***')
# print(40,50,60,sep = ':') # default value of 'end' attribute is '\n'
# print(70,80,sep = '**',end = '$$')
# print(90,100) # ',' means space is the seperator

# a=10
# b=20
# c=30
# print("a value is %i" %a)
# print("b value is %d and c value is %d" %(b,c))

# price = 70.56789
# print('Price value = {}'.format(price))
# print('Price value = %f'%price)
# print('Price value = %.2f'%price)

# a=int(input("Enter First Number:"))
# b=int(input("Enter Second Number:"))
# c=int(input("Enter Third Number:"))
# min=a if a<b and a<c else b if b<c else c
# print("Minimum Value:",min)

# tup=(1)
# print(type(tup))

# tup1=(1,)
# print(type(tup1))

# cities={"m","n"}
# cities.clear()
# print(cities)#set()

# print(type(bin(10.5)))#TYpeError

# cities={"Tokyo","M","B","D"}
# cities2={"Tokyo","S","K","M"}
# city=cities.difference(cities2)
# city3=cities2.difference(cities)
# print(cities)
# print(cities2)
# print(city)
# print(city3)

# x = firstValue if condition else secondValue

###!!!get() and setdefault() both donnot changes value of existing value of key
# info={'name':'Karan','age':19,'eligible':True}
# print(info['name2'])#KeyError
# print(info.get('name2'))#None
# print(info.get('name','khyati'))

##when asserrt statement gets false we get assertionerror
# def divide(x,y):
#     assert y!=0,"cannot divide by zero" #if assert is false then this is printed along with AssertionError.
#     return x/y
# print(divide(8,10))
# print(divide(8,0))

# ##datatypes are classes. variables are instances of classes.
# print(type(4E+2))
# print(type(4e+2))

#ordered data types: tuple, list,string

# a=42,000
# print(type(a))

##docstrimg should be right after function,classs otherwise none is printed if .__doc__ method is used
# def my_function():
# 	'''Demonstrates triple double quotes
# 	docstrings and does nothing really.'''
# 	return None
# print("Using __doc__:")
# print(my_function.__doc__)
# print("Using help:")
# help(my_function)

# Precedence of 'or' & 'and'
# name = "Alex"
# age = 0
# if (name == "Alex" or name == "John") and age >= 2:
# 	print("Hello! Welcome.")
# else:
# 	print("Good Bye!!")

##very important
# name = "Alex"
# age = 0
# if name == "Alex" or name == "John" and age >= 2:
# #same as if name == "Alex" or (name == "John" and age >= 2):
# 	print("Hello! Welcome.")
# else:
# 	print("Good Bye!!")

# print(4*[7])
# print(4*(7,))
# print(2 ** 3 ** 2)##right associativity

# for i in range(3.3):
#     print(i)

#range() with indexing
# ele = range(10)[0]
# print("First element:", ele)
# ele = range(10)[-1]
# print("\nLast element:", ele)
# ele = range(10)[4]
# print("\nFifth element:", ele)

# count=0
# while count<5: count+=1; print("Hello")

# all statements after pass are executed
# a=5
# if a>4:
#     pass
#     print("diya")

# names = ['Mukesh', 'Roni', 'Chari']
# ages = [24, 50, 18]
# for i, (name, age) in enumerate(zip(names, ages)):
# 	print(i, name, age)

# name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
# roll_no = [4, 1, 3, 2]
# marks = [40, 50, 60, 70]
# mapped = zip(name, roll_no, marks)
# mapped = list(mapped)
# print("The zipped result is : ", end="")
# print(mapped)
# print("\n")
# # unzipping values
# namz, roll_noz, marksz = zip(*mapped)
# print("The unzipped result: \n", end="")
# print("The name list is : ", end="")
# print(namz)
# print("The roll_no list is : ", end="")
# print(roll_noz)
# print("The marks list is : ", end="")
# print(marksz)

##debuggers are software tool
#pdb-->python debugger included in the standard library
# Defined as the class Pdb which internally makes use of:
# bdb (basic debugger functions)
# cmd (support for line-oriented command interpreters) modules
#python -m pdb exppdb.py 
#pdb.pm():will tell debug even after execution of program
#break filename: lineno, condition
#pdb.set_trace() or breakpoint()

# import pdb 
# def rec_fxn(r): 
#     if r > 0: 
#         pdb.set_trace() 
#         rec_fxn(r//2) 
#     else: 
#         print("recursion stops") 
#     return 
# pdb.set_trace() 
# rec_fxn(5)

# p=10
# q=20
# r=30
# min= p if p<q and p>r else q if q<r else r
# print("Minimum Value:",min)

# print(~False)
# print(~True)
# a = ~False & ~True
# print(a<<1)#-2
# # 11 & 10 -->10

# print('Python' and '0')
# print(2*3**2)#-->(2*9)

# string="diyagupta"
# print(len(string))
# print(string[3:-2])
# print(string[3:7])
# print(string[-3:-1])
# print(string[6:8])

# inn="Diya is smart girl."
# words=inn.split(" ")
# words=inn.split("")#valueerror empty separator
# words=inn.split()#default-->space
# print(inn)
# print(words)

##arrays::array module ::array.array('datatype',value_list)
# import array as arr
# a = arr.array('i', [1, 2, 3])
# print("The new created array is : ", end=" ")
# for i in range(0, 3):
#     print(a[i], end=" ")
# print()
# b = arr.array('d', [2.5, 3.2, 3.3])
# print("\nThe new created array is : ", end=" ")
# for i in range(0, 3):
#     print(b[i], end=" ")

# import array as arr
# a = arr.array('i', [1, 2, 3])
# print("Array before insertion : ", end=" ")
# for i in range(0, 3):
#     print(a[i], end=" ")
# print()
# a.insert(1, 4)
# print("Array after insertion : ", end=" ")
# for i in (a):
#     print(i, end=" ")
# print()
# b = arr.array('d', [2.5, 3.2, 3.3])
# print("Array before insertion : ", end=" ")
# for i in range(0, 3):
#     print(b[i], end=" ")
# print()
# b.append(4.4)
# print("Array after insertion : ", end=" ")
# for i in (b):
#     print(i, end=" ")
# print()

# import array as arr
# a = arr.array('i', [1, 2, 3, 4, 5, 6])
# print("Access element is: ", a[0])
# print("Access element is: ", a[3])
# b = arr.array('d', [2.5, 3.2, 3.3])
# print("Access element is: ", b[1])
# print("Access element is: ", b[2])

# import array
# arr = array.array('i', [1, 2, 3, 1, 5])
# # arr=list(arr)
# print(list(arr))
# print(type(arr))
# print("The new created array is : ", end="")
# # print(list(arr))
# for i in range(0, 5):
#     print(arr[i], end=" ")
# print("\r")
# print("The popped element is : ", end="")
# print(arr.pop(2))#index
# print("The array after popping is : ", end="")
# for i in range(0, 4):
#     print(arr[i], end=" ")
# print("\r")
# arr.remove(1)#remove first one
# print("The array after removing is : ", end="")
# for i in range(0, 3):
#     print(arr[i], end=" ")

#incompatible datatypes
# import array
# arr=array.array('i',[1,2,'a',4])#TypeError
# arr=array.array('i',[1,2,a,4])#NameError
# print(arr)

# import array as arr
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = arr.array('i', l)
# print("Initial Array: ")
# for i in (a):
#     print(i, end=" ")
# Sliced_array = a[3:8]
# print("\nSlicing elements in a range 3-8: ")
# print(Sliced_array)
# Sliced_array = a[5:]
# print("\nElements sliced from 5th "
#       "element till the end: ")
# print(Sliced_array)
# Sliced_array = a[:]
# print("\nPrinting all elements using slice operation: ")
# print(Sliced_array)

# import array
# arr = array.array('i', [1, 2, 3, 1, 2, 5])
# print("The new created array is : ", end="")
# for i in range(0, 6):
#     print(arr[i], end=" ")
# print("\r")
# print("The index of 1st occurrence of 2 is : ", end="")
# print(arr.index(2))
# print("The index of 1st occurrence of 1 is : ", end="")
# print(arr.index(1))

# import array
# arr = array.array('i', [1, 2, 3, 1, 2, 5])
# print("Array before updation : ", end="")
# for i in range(0, 6):
#     print(arr[i], end=" ")
# print("\r")
# arr[2] = 6
# print("Array after updation : ", end="")
# for i in range(0, 6):
#     print(arr[i], end=" ")
# print()
# arr[4] = 8
# print("Array after updation : ", end="")
# for i in range(0, 6):
#     print(arr[i], end=" ")

# import array
# my_array = array.array('i', [1, 2, 3, 4, 2, 5, 2])
# count = my_array.count(2)
# print("Number of occurrences of 2:", count)

# import array
# my_array = array.array('i', [1, 2, 3, 4, 5])
# print("Original array:", *my_array)
# print("Original array:", my_array)
# my_array.reverse()
# print("Reversed array:", *my_array)
# print("Reversed array:", my_array)

# import array as arr 
# a = arr.array('i', [1, 2, 3,4,5])
# print("The before array extend  : ", end =" ")
# for i in range (0, 5):  
#     print (a[i], end =" ")    
# print()
# a.extend([6,7,8,9,10])
# print("\nThe array after extend :",end=" ")
# for i in range(0,10):  
#     print(a[i],end=" ") 
# print()

# import array as arr
# a=arr.array('i',[1,2,3,4,5,6])
# print("The Before extend array is :",end=" ")
# for i in range(0,6):
#     print(a[i],end=" ")  
# print()
# a.extend([7,8,9,10,11,12])
# print("\nThe After extend array is :",end=" ")
# for i in range(0,12):  
#     print(a[i],end=" ")
# print()
# b = arr.array('d', [2.1,2.2,2.3,2.4,2.5,2.6])
# print("\nThe before extend array is :",end=" ")
# for i in range(0,6): 
#   print(b[i],end=" ")  
# print() 
# b.extend([2.6,2.7,2.8,2.9])
# print("\nThe after extend array is :",end=" ")
# for i in range(0,9+1):
#   print(b[i],end=" ")
# print()  

##numpy.array():automatic type conversion as string
# import numpy as np 
# list_=[2,4,6]
# res=np.array(list_)
# print(res)
# print(type(res))
# print(res.dtype)#tells about type of data , size of data
# print(res.ndim)#tells abt no. of dimensions of array
# list_2=[2.4,5.6]
# res2=np.array(list_2)
# print(type(res))#numpy.ndarray
# print(type(res[0]))#numpy.int32
# print(type(res2[0]))#numpy.float64

# import numpy as np
# dt = np.dtype([('name', np.unicode_, 16), ('grades', np.float64, (2,))])
# # x is a structured array with names and marks of students.
# # Data type of name of the student is np.unicode_ and
# # data type of marks is np.float(64)
# x = np.array([('Sarah', (8.0, 7.0)), ('John', (6.0, 7.0))], dtype=dt)
# print(x[1])
# print("Grades of John are: ",x[1]['grades'])
# print("Names are: ",x['name'])

# tup=('py',2)
# tup=tup*3
# tup=(tup)*3
# print(tup)

##deepcopy is formed
# import array
# lst=[1,7]
# arr1=array.array('i',lst)
# print(arr1)
# arr2=array.array('i',arr1)
# print("arr2:",arr2)
# arr2[1]=23
# print(lst)
# print(arr1)
# print(arr2)
# print(id(arr1))
# print(id(arr2))

##for incompatible datatypes
##array.array()-->we get valueerror or typeerror
#numpy.array()-->automatic conversion to string

# import numpy as np
# test_list=[6.1,'8.3']
# res=np.array(test_list)
# print(res)
# print(type(res[0]))#numpy.str_
# print(type(res[1]))#numpy.str_

##copy of array in numpy.array():deep copy is formed change in one is not reflected in other
# import numpy
# lst=[1,7]
# arr1=numpy.array(lst)
# print(arr1)
# arr2=numpy.array(arr1)
# print("arr2:",arr2)
# arr2[1]=23
# print(lst)
# print(arr1)
# print(arr2)
# print(id(arr1))
# print(id(arr2))

#np.array:it creates a copy of the object array or the original array and does not reflect any changes made to the original array.
#  Whereas on the other hand, when we try to use NumPy asarray, it would reflect all the changes made to the original array.
##numpy.asarray(): shallow copy
# import numpy as np 
# my_list = [1, 3, 5, 7, 9] 
# print ("Input  list : ", my_list)    
# out_arr = np.asarray(my_list) 
# print ("output array from input list : ", out_arr)
# print(type(out_arr))##numpy.ndarray
# print(type(out_arr[0]))#numpy.int32

# import numpy
# lst=[1,7]
# arr1=numpy.asarray(lst)
# print(arr1)
# arr2=numpy.asarray(arr1)
# print("arr2:",arr2)
# arr2[1]=23
# print(lst)##remains same
# print(arr1)
# print(arr2)
# print(id(arr1))
# print(id(arr2))

# import numpy as geek 
# my_tuple = ([1, 3, 9], [8, 2, 6]) 
# print ("Input  tuple : ", my_tuple) 
# out_arr = geek.asarray(my_tuple)  
# print ("output array from input tuple : ", out_arr) 
# print(type(out_arr))#numpy.ndarray
# print(type(out_arr[0]))#numpy.ndarray
# print(type(out_arr[0][0]))#numpy.int32

##conclusion:for array:
#array method:array.array('datatype',list):deep copy + in compatible datatype then error comes
#numpy.array():deep copy is formed + converted to string automatically
#numpy.asarray:shallow copy + same ids + change reflected everywhere

