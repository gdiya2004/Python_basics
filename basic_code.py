# def average(a=1,b=3):

#     print("Average=",(a+b)/2)

# average(b=21,a=9)

# if "iy" in "diya":
#     print("yes")

# else:

#     print("no")

# l=[11,45,1,2,4,6,1,1]
# m=l
# print(id(m))
# print(id(l))
# m[0]=0
# print(l)
# print(m)

# tup=(1)
# print(type(tup))

# tup1=(1,)
# print(type(tup1))

# name="Diya"
# print(f"{name}")

# set1={1,2,3}
# set2={5,7,8}
# set1.update(set2)
# print(set1)
# print(set2)

# cities={"m","n"}
# cities.clear()
# print(cities)

# print(type(bin(10.5)))#TYpeError

# cities={"Tokyo","M","B","D"}
# cities2={"Tokyo","S","K","M"}
# city=cities.difference(cities2)
# city3=cities2.difference(cities)
# print(cities)
# print(cities2)
# print(city)
# print(city3)

# def binary_to_dec_conv(numlist):
#     result_list=[]
#     for num in numlist:
#         i=0
#         result=0
#         while num!=0:
#             result = result + (num % 10)*(2**i)
#             num = num//10
#             i+=1
#         result_list.append(result)
#     return(result_list)
# n=int(input("number of binary numbers to be entered="))
# list=[]
# for i in range(n):
#     num=int(input(f"Enter the {i+1} number="))
#     list.append(num)
# print(list)
# new_list= binary_to_dec_conv(list)
# print(new_list)
# mul_list=[]
# for new in new_list:
#     if new%5==0:
#         mul_list.append(new)
#     else:
#         continue
# print(mul_list)

# def factorial(num):
#     if num==1:
#         return 1
#     num=num*factorial(num-1)
#     return(num)
# a=factorial(5)
# print(a)

# list=[1,2]
# print(type(list[0]))

# def fibonacci(n):
#     fib_series=[0,1]
#     while len(fib_series)<n:
#         fib_series.append(fib_series[-1]+fib_series[-2])
#     return fib_series
# result=fibonacci(10)
# print(result)

# pass_list=[]
# n=int(input("enter the number of passwords ="))
# for i in range(n):
#     password=input("Enter the password=")
#     pass_list.append(password)
# valid_list=[]
# for pas in pass_list:
#     if 6<=len(pas)<=16:
#         if any(c.isdigit() for c in pas) and any(c.isupper() for c in pas) and any(c.islower() for c in pas) and any(char in pas for char in ['$','@','#']):
#             valid_list.append(pas)
# print(valid_list)

# for i in range(1,6):
#     for j in range(1,i):
#         print(j)
#     print('\n')

# for i in range(1,6):
    # for j in range(i,7):
    #     print(" ",end=" ")
    # for k in range(1,i+1):
    #     print(" * ",end=" ")
    # print()

# for i in range(0,5):
#     for j in range(0,5-i):
#         print("*",end=" ")
#     print()

# for i in range(9,0,-2):
#     for j in range(0,10-i,2):
#         print(end=" ")
#     for j in range(i):
#         print(j+1,end=" ")
#     print()
# for i in range(3,10,2):
#     for j in range(0,10-i,2):
#         print(end=" ")
#     for j in range(i):
#         print(j+1,end=" ")
#     print()

# for i in range(1,6):
#     k=1
#     if(i in range(1,5)):
#         for j in range(1,10):
#             if(j==6-i or j==4+i):#i=1,j=5
#                 print(k,end='')
#                 k=2
#             else:
#                 print(' ',end=" ")
#         print() 
#     if(i==5):
#         for x in range(1,10):
#             print(x,end=' ')
               
###!!!get() and setdefault() both donnot changes value of existing value of key
# info={'name':'Karan','age':19,'eligible':True}
# print(info['name2'])#KeyError
# print(info.get('name2'))#None
# print(info.get('name','khyati'))
# print(info.keys())
# print(info.values())

# for key in info.keys():
#     print(f"The value corresponding to the key {key} is {info[key]}")

# for key in info.keys():
#     text="The value corresponding to the key {} is {}"
#     print(text.format(key,info[key]))    
    
# for i in range(6):
#     # print(i)
#     if i==4:
#         continue
#     print(i)
# else:
#     print("Sorry")

#syntax errors(errors)
#logical errors(exception):ZeroDivisionError, Importerror(importing file that doenot exists)
##exceptions:
#1:IndexError
#2.AssertionError:
#3.AttributeError:when attribute/method is not found on an object
#4.ImportError:
#5.KeyError:key of dictionary is not found
#6.NameError:variable is not defined
#7.MemoryError:Program runs out of memory
#8.TypeError:functions and operations are applied in an incorrect type
#9.ValueEror:function/method is called with invalid argumment
#10.ZeroDivision Error:
#11.IOError:

##assertionError occurs when assert statement fails.
#assert statemenets are used to test conditions that are expected to be true
# def divide(x,y):
#     assert y!=0,"cannot divide by zero" #if assert is false then this is printed along with AssertionError.
#     return x/y
# print(divide(8,10))
# print(divide(8,0))

# a=input("Enter Number=")
# print(f"Multiplication table of {a}is:")
# try:
#     for i in range (1,11):
#         print(f"{int(a)}*{i}=")
# except Exception as e:
#     print(e)
# print("True")
# print("Bye")

# def func():
#  try:
#     l=[1,2,3]
#     i=int(input("Enter the index="))
#     print(l[i])
#     return 1
#  except:
#     print("Some Error")
#     return 0
# print("Tata Byee")
# x=func()
# print(x)

# a=[1,2,3]
# try:
#     print(a[1])
#     a[2]=10
#     print(a[3])
#     a[0]=100
# except:
#     print("Index error")
# print(a)

##!!!!!!!!!!!!!!!!Try always requires one except
# try:
#     num=int(input("Enter no.="))
#     result=10/num
#     print(result)
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("Enter valid number")
# except Exception as e:
#     print("unexpected Error",e)
# finally:
#     print("Hard Work is key to success")

##!!!!!!!!!!!try with else:else is executed is no except block works and
#  finally always comes after try and any associated except or else block 
# if else is placed after finally then syntax error will come
# try:
#     num=int(input("Enter no.="))
#     result=10/num
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("Enter valid number")
# except Exception as e:
#     print("unexpected Error",e)
# else:
#     print(result)
# finally:
#     print("Hard Work is key to success")

##Assertion handling code: in this case aas y=0 so only assertion error will be raised 
# we won't reach zeroDivisionerror block as assertion block will prevent from assertion error from happening
# try:
#     x=10
#     y=0
#     assert y!=0, "Divide by zero error"
#     result=x/y
#     print(result)
# except AssertionError:
#     print("Assertion Error")
# except ZeroDivisionError:
#     print("cannot divide by 0")
# except Exception as e:
    # print("unexpected error")

###!!!!!!!!!as keywprd is used for aliasing!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

##complex conditional statements to check errors: instead of it prefer try-except foe exceptional handling
# num_str=input("Enter a number=")
# if num_str.isdigit():
#     num=int(num_str)
#     if num!=0:
#         result=10/num
#         print(result)
#     else:
#         print("ZeroDivisionError")
# else:
#     print("ValueError")

##raise ke baad wali statements execute nhi hoti
# a=int(input("Enter any value between 5 and 9="))
# if a<5 or a>9:
#     print("hello")
#     raise TypeError("Value should be btw 5 and 9")
# print("hii")

# s1="hello"
# try:
#     n1=int(s1)
# except:
#     print("Hiii")
# print(s1)

# with open('python_code/file2.txt','r') as file:
#     content=file.read()
# formatted_content="{:.2f}".format(content)
# print(formatted_content)


# a=input("Enter any string:")
# if a!="quit":
#     raise ValueError("This is not desiewd string")
# else:
#     print("correct")

###greatest of three numbers
# import pdb
# a=int(input("Enter the first number="))
# breakpoint()
# b=int(input("Enter the second number="))
# c=int(input("Enter the third number="))
# breakpoint()
# if a>b:
#     if a>c:
#         print(f"{a} is the greatest")
# else:
#     if b>c:
#         print(f"{b} is the greatest")
#     else:
#         print(f"{c} is the greatest")

##short hand if-else statement
# max= a if(a>b and a>c) else (b if(b>c) else c) 
# print(max)

##strings are immutable
# str="diya"
# str[0]="p"
# print(str[0])
# print(str)

# fruit="banaana"
# print(list(enumerate(fruit)))
# print(len(fruit))

##exception class is base class for all exceptions
##!!!Priyanshu code
# def sort_tuple_by_float(tup):
#     return tuple(sorted(tup,key=lambda x:float(x) if isinstance(x,(int,float)) else float('inf')))#
#     ####sorted() function sort the elemnets of tuple on the basis of key provided
#     ##key: x-->float(x) if x is int ,float otherwise float('inf')-->assigns float value to infinity ensuring that non numeric elements are placed at end of sorted tuple.
# ex_tuple=('b',3.5,'a',1.2,5,2.8)
# sorted=sort_tuple_by_float(ex_tuple)
# print(sorted)

# alist=[4,2,8,6,5]
# blist=[alist]*2 #[[4,2,8,6,5],[4,2,8,6,5]]
# blist=alist*2 #[4,2,8,6,5,4,2,8,6,5]
# alist[3]=999
# print(blist)

# The ndarray.tolist() method converts a NumPy array
#  into a nested Python list.
# import numpy as np 
# gfg = np.array([1, 2, 3, 4, 5]) 
# print(type(gfg))##numpy.ndarray
# gfg_list=gfg.tolist()
# print(gfg_list)
# print(type(gfg_list))##list


# When comparing tuples in Python, Python first compares the elements at index 0 of each tuple. If they are equal, 
# it proceeds to compare elements at index 1, and so o
# t1=(1,2,3)
# t2=(2,)
# print(t2>t1)

# def flatten_list(lst):
#     flattened=[]
#     for sublist in lst:
#         if isinstance(sublist,list):
#             flattened.extend(flatten_list(sublist))
#         else:
#             flattened.append(sublist)
#     return flattened
# list1=[[1,2,3,4,5],[5,3],[4,5,3],[[9,6],[3,0]]]
# x=flatten_list(list1)
# print(x)

# string=input("enter string:")
# stack=[]
# for c in string:
#     stack.append(c)
# print(stack)
# r_str=[]
# for c in stack:
#     r_str+=stack.pop()
# print("".join(r_str))
# # print(str(r_str))
# reversed_str="".join(reversed(string))
# print(reversed_str)

# def fun(list_w):
#     max_w=0
#     lengthy=[]
#     # for word in list_w:
#     #     if max_w<=len(word):
#     #         max_w=len(word)
#     #         lengthy=word
#     max_w=max([len(word) for word in list_w])
#     lengthy=[word for word in list_w if len(word)==max_w]
#     return lengthy,max_w
# list_words=["diya","khyati","namish"]
# lengthy_word,w=fun(list_words)
# print(f"longest word={lengthy_word} and is of {w} length")

# sample1="diya"
# sample2="gupta"
# new_sample1=sample2[:2]+sample1[2:]
# new_sample2=sample1[:2]+sample2[2:]
# sample=new_sample1+" "+new_sample2
# print(sample)

###max is inbuit function in python
# max_num=max(a,b,c)
# print(max_num)

###very important
# x=int(input("Enter the number="))
# if 6>x>2:
#     print("yes")
# else:
#     print("no")

##local and global variables...
# x=4
# def hello():
#     global x
#     x=7
#     print("Hello")
#     print(x)#7
# print(x)#4
# hello()
# print(x)#7

#The nonlocal keyword is used in nested functions 
# to reference a variable in the parent function. 
# global_name = 'geeksforgeeks'
# def foo():
# 	def bar():
# 		nonlocal global_name# Try to reference global variable
# 		global_name = 'GeeksForGeeks'# Try to overwrite it
# 		print(global_name)
# 	bar()
# foo()

#The nonlocal keyword is used in nested functions 
# to reference a variable in the parent function. 
# def foo():
# 	name = "geek"
# 	def bar():
# 		name = "Geek"
# 		def ack():
# 			nonlocal name # Reference to the next upper variable with this name
# 			print(name) 
# 			name = 'GEEK' 
# 			print(name)
# 		ack()
# 	bar() 
# 	print(name) 
# foo()

# Our counter function
# def counter():
#     c = 0 
#     def count():
# 	    nonlocal c
# 	    c += 1#1
# 	    return c
#     return count
# my_counter=counter()#returns inner function count assigned to my_counter
# for i in range(3):
#     print(my_counter())#count()#1 2 3
# print('End of my_counter')
# for i in range(3):
#     print(my_counter())#4 5 6
# print('End of counter')

# strip method() removes any leading and trailing whitespaces
# x = "     banana     "
# x = x.strip()
# print("of all fruits", x, "is my favorite")

##removes trailing and leading characters
# txt = ",,,,,rrttgg.....ba..nana....rrr"
# x = txt.strip(",.grt")##removes trailing and leading characters
# y=txt.rstrip(",.grt")#removes trailing characters
# print(x)
# print(y)

# def distinct_sorted_words(sequence):
#     words = [word.strip() for word in sequence.split(',')]
#     unique_words = list(set(words))
#     sorted_words = sorted(unique_words)
#     sorted_sequence = ', '.join(sorted_words)
#     return sorted_sequence
# input_sequence = input("Enter a comma-separated sequence of words: ")
# result = distinct_sorted_words(input_sequence)
# print("Distinct words in sorted form:", result)

# str = '-'.join('hello')
# print(str)

# list1 = ['g', 'e', 'e', 'k', 's']
# print("".join(list1))#empty separator
# list1 = " geeks "
# print("$".join(list1))

# t1 = ('1', '2', '3', '4')
# s = "-"
# s = s.join(t1)
# print(s)

# set_ = {'1', '2', '3', '4', '4'} #removes duplicate as set
# # put any character to join
# s = "-#-"
# s = s.join(set_)
# print(s)

# dic = {'Geek': 1, 'For': 2, 'Geeks': 3}
# string = '_'.join(dic)#access only keys
# print(string)

# When we join the dictionary keys 
# it only joins the keys which are string only not an integer
#if keys are int then give typeerror
# dic2 = {1:'Geek', 2:'For', 3:'Geeks'}
# string = '_'.join(dic2)
# print(string)

# words = ["apple", "", "banana", "cherry", ""]
# separator = "@ "
# result = separator.join(word for word in words if word)
# print(result)

# string=".....diya..........gupta,,,kkhjkkbk"
# string=string.strip(".,khjb")
# print(string)

# def outer_function():
#     x = 10
#     def inner_function():
#         nonlocal x
#         x = 20  
#     inner_function()
#     print("Value of x after calling inner_function:", x)
# outer_function()

# This function uses global variable s
# def f():
# 	print("Inside Function", s)
# s = "I love Geeksforgeeks"##global decalaration
# f()
# print("Outside Function", s)

##important
# def f():
#     s = "Me too."##redecalared
#     print(s)
# s = "I love Geeksforgeeks" #global variable
# f()
# print(s)

# def f():
#     s += 'GFG'##one type of redecalaration
#     print("Inside Function", s)
# s = "I love Geeksforgeeks"
# f()



# This function modifies the global variable 's'
# def f():
#     global s
#     s += ' GFG'
#     print(s)
#     s = "Look for Geeksforgeeks Python Section"
#     print(s) 
# s = "Python is great!"
# f()
# print(s)

# a = 1
# def f():
# 	print('Inside f() : ', a)#1
# def g():
# 	a = 2 #redecalration so will not change value of global variable
# 	print('Inside g() : ', a)#2
# def h():
# 	global a
# 	a = 3
# 	print('Inside h() : ', a)#3
# print('global : ', a)#1
# f()
# print('global : ', a)#1
# g()
# print('global : ', a)#1
# h()
# print('global : ', a)#3


# sets={1,2,3}
# # sets=sets.remove(3)
# sets=sets.pop()#returns the value
# print(sets)

# def majority_func(lst):
#     count_dict={}
#     for num in lst:
#         if num in count_dict:
#             count_dict[num]+=1
#         else:
#             count_dict[num]=1
#     max_count=0
#     max_elements=[]
#     for key,value in count_dict.items():
#         if value>max_count:
#             max_count=value
#             max_elements=[key]
#         elif value==max_count:
#             max_elements.append(key)
#     return max_count,max_elements
# lst=[1,3,3,4,5,7,2,9,7,6]
# print(majority_func(lst))

# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")

# list_=[j for j in range(3) for i in range (3)]#[outer loop_inner loop]
# list_2=[i for j in range(3) for i in range (3)]
# print(list_)
# print(list_2)

##enumerate function
##in this case order matters it is index,mark matters  remember.......
# marks=[100,300,68,65,49]
# for index,mark in enumerate(marks):
#     print(mark)
    # if(index==3):
        # print("Diya")

# import math
# from math import sqrt
# print(dir(math))

##use of zip function:
# fruits=["lichi","melon","apple"]
# colors=["white","green","red"]
# for fruit,color in zip(fruits,colors):
#     print(fruit,"is",color)

# fruits=["lichi","melon"]
# colors=["white","green","red"]
# for fruit,color in zip(fruits,colors):
#     print(fruit,"is",color)

# numbers=[5,6,32,21,9]
# running_total=0
# for number in numbers:
#     running_total=running_total+number
# print(running_total)

# a=[1,2,3,4]
# while a:
#     print(a.pop())

# a=[1,2,3]
# a.pop()
# print(a)

# num=18
# match num:
#     case 0:
#         print("zero")
#     case 1:
#         print("one")
#     case default:
#         print("Anything")

# char='A'
# print(ord(char))
# print(ord('A'))
# print(ord("A"))
# print(ord("""A"""))
# print(ord('''A'''))
# print(ord(A))#NameError

# def name(fname,mname,lname):
#     print("Hello")
# name("Diya Guota")

# def myfun(**kwargs):
#     for key,value in kwargs.items():
#         print("%s==%s"%(key,value))
# myfun(first="Hello",second="Diya",third="Gupta")

# def fun(d,e,/,a,b,c):
#     sum=a+b+c+d+e
#     return sum
# y=fun(5,3,b=2,a=3,c=4)
# print(y)

# str1="diya gupta"
# upper=lambda str1:str1.upper()
# print(upper(str1))

# g=lambda a,b:a if a>b else b
# print("Greatest:",g(20,30))
# print(g)
# print(type(g))

# def tuple_to_list(tuple_):
#     if isinstance(tuple_,tuple):
#         return [tuple_to_list(item) for item in tuple_]
#     elif isinstance(tuple_,list):
#         return [tuple_to_list(item) for item in tuple_]
#     else:
#         return tuple_
# def list_to_tuple(list_):
#     if isinstance(list_,list):
#         return tuple(list_to_tuple(item) for item in list_)
#     elif isinstance(list_,tuple):
#         return tuple(list_to_tuple(item) for item in list_)
#     else:
#         return list_
# nested_tup=(1,(2,3),[4,(5,6)])
# nested_list=[[1,2],[3,[4,5]],6]
# conv_tup=tuple_to_list(nested_tup)
# conv_list=list_to_tuple(nested_list)
# # print(conv_tup)
# # print(conv_list)

# #sorted() function: sorted(iterable,key,reverse):data type is list
# x = ['q', 'w', 'r', 'e', 't', 'y'] 
# print(sorted(x)) 
# x = ('q', 'w', 'e', 'r', 't', 'y') 
# print(sorted(x)) 
# # String-sorted based on ASCII translations 
# x = "python"
# print(sorted(x)) 
# print(type(sorted(x)))###list
# ###dictionary keys aare sorted
# x = {'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6} 
# print(sorted(x)) 
# x = {'q', 'w', 'e', 'r', 't', 'y'} 
# print(sorted(x)) 
# x = frozenset(('q', 'w', 'e', 'r', 't', 'y')) 
# print(sorted(x)) 

# Python3 code to demonstrate 
# Reverse Sort a String 
# using join() + sorted() + reverse 
	
# test_string = "geekforgeeks"  
# res = ''.join(sorted(test_string, reverse = True))
# # print result 
# print("String after reverse sorting : " + str(res))

# L = ["cccc", "b", "dd", "aaa"] 
# print("Normal sort :", sorted(L)) 
# print("Sort with len :", sorted(L, key=len)) 

# def func(x): 
# 	return x % 7
# L = [15, 3, 11, 7] 
# print("Normal sort :", sorted(L)) 
# print("Sorted with key:", sorted(L, key=func)) 

# my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5] 
# sorted_list = sorted(my_list) 
# print(sorted_list) 
# my_string = "hello, world!"
# sorted_string = sorted(my_string) 
# print(sorted_string) 
# my_tuples = [(1, "one"), (3, "three"), (2, "two"), (4, "four")] 
# # sorted_tuples = sorted(my_tuples, key=lambda x: x[1]) 
# # sorted_tuples=sorted(my_tuples)
# print(sorted_tuples)

# filter,map,lambda,reduce
# def avg_score(tup_list):
#     maths=[]
#     science=[]
#     eng=[]
#     for i in range(0,3):
#         maths.append(tup_list[i][1])
#         science.append(tup_list[i][2])
#         eng.append(tup_list[i][3])
#     print(maths)
#     print(science)
#     print(eng)
#     maths_av=sum(maths)/3
#     science_av=sum(science)/3
#     eng_av=sum(eng)/3
#     return (maths_av,science_av,eng_av)

# tup_list=[("Diya",100,98,91),("Khyati",100,100,98),("Namish",100,100,100)]
# averagee=avg_score(tup_list)
# print(averagee)

# from functools import reduce
# numbers=[1,2,3,4,5]
# filter_is=list(filter(lambda x:x%2==0,numbers))
# print(filter_is)
# reduce_is=reduce(lambda x,y:x+y,numbers)
# print(reduce_is)
# print(list(reduce_is)) ##!!!!very important 

 ##int will be converted into list in 2 ways:
# integer=3
# list_=list(str(integer))
# print(list_)

##or By without converting it to string
# integer=5
# list_=[integer]
# print(list_)
# print(type(list_))##list
# print(type(reduce_is))
# map_is=list(map(lambda x:x*2,numbers))
# print(map_is)

# list1=[1,2]
# list2=[3,4]
# is_map=list(map(lambda x,y:x+y,list1,list2))
# print(is_map)

##factorial
# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# integer=int(input("Enter the number:"))
# fact=factorial(integer)
# print(fact)

## nthfibonacci number
# def fibo(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fibo(n-1)+fibo(n-2)
# x=int(input("Enter the no. of fibonacci:"))
# y=fibo(x)
# print(y)


# n=int(input("Enter a number="))
# fib0=0
# fib1=1
# print(f'{fib0},' ,end="")
# for i in range(1,n):
#     print(f'{fib1},',end=(""))
#     temp=fib0
#     fib0=fib1
#     fib1=temp+fib1
# # print(fib1)

# name="diya gupta"
# print(name.title()) #Diya Gupta
# print(name.capitalize())#Diya gupta

# fruit="banana"
# print(list(enumerate(fruit)))

# string="ASTRING"
# s1=slice(3)
# print(s1)#slice(NONe,3,None)
# print(string[s1])#AST
# print(string[slice(3)])
# print(string)
# print(string[5:3])

##lexicographical order also called as dictionary order
# a="apple"
# b="banana"
# c="cow"
# d="Apple"
# if d<a:
#     print("Uppercase comes before lowercase")
# if a<b:
#     print("Alphabetically a comes before b")
# if c=="cow":
#     print("Comparison between strings can be done using ==")

##split method:splits single multi word string into list of individual words, removing all the white spaces
# phrase="Never give much importance to someone"
# words=phrase.split()
# print(words)
# print(phrase.split(','))

# string="one,two,three,"
# words=string.split(",")
# print(words)
# word="catbatmat"
# print(word.split("t"))

##datetime() module:
# datetime.datetime.now() and datetime.datetime.today() is used
# import datetime
# today=datetime.datetime.today()
# print(f"{today:%B %d %Y}")
# current_time=datetime.datetime.now()
# print("The attributes of now() are:")
# print("Complete:",current_time)
# print("year:",current_time.year)
# print("month:",current_time.month)
# print("day:",current_time.day)
# print("hour:",current_time.hour)
# print("minutes:",current_time.minute)
# print("seconds:",current_time.second)
# print("microsecond:",current_time.microsecond)

# import numpy as n
# list=[1,2,3,'a']
# res=n.asarray(list)
# print(res)
# print(type(res))
# print(type(res[2]))

# from array import array
# list=[1,2,3]
# res=array('i',list)
# print(res)
# print(res[0])
# print(type(res[0]))
# res2=array("i",res)
# # res2[2]=4
# print(f'{res} and id={id(res)}')
# print(res2)
# print(f'{res2} and id={id(res2)}')

##to remove duplicate either convert into set or use dict.fromkeys(list,tuple)
# my_list=('a','a','a','b','b')
# # my_list=tuple(dict.fromkeys(my_list))
# print(tuple(set(my_list)))
# print(type(my_list))

#filter(function,sequence)
# def fun(variable):
# 	letters = ['a', 'e', 'i', 'o', 'u']
# 	if (variable in letters):
# 		return True
# 	else:
# 		return False
# sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
# filtered = filter(fun, sequence)
# print('The filtered letters are:')
# for s in filtered:
# 	print(s)

# a list contains both even and odd numbers. 
# seq = [0, 1, 2, 3, 5, 8, 13]
# # result contains odd numbers of the list
# result = filter(lambda x: x % 2 != 0, seq)
# print(list(result))
# # result contains even numbers of the list
# result = filter(lambda x: x % 2 == 0, seq)
# print(list(result))

# def is_multiple_of_3(num):
# 	return num % 3 == 0
# # Create a list of numbers to filter
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = list(filter(lambda x: is_multiple_of_3(x), numbers))
# print(result)

##map(function,iterable)
# def addition(n):
# 	return n + n
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))

# l = ['sat', 'bat', 'cat', 'mat']
# # map() can listify the list of strings individually
# test = list(map(list, l))
# print(test)

# Define a function that doubles even numbers and leaves odd numbers as is
# def double_even(num):
# 	if num % 2 == 0:
# 		return num * 2
# 	else:
# 		return num
# numbers = [1, 2, 3, 4, 5]
# result = list(map(double_even, numbers))
# print(result) # [1, 4, 3, 8, 5]

# tup1=(8,9,90)
# (rollno,engg,maths,gpa)=tup1
# print(rollno)

##File handling:allows to store data permanently into file(non-volatile)
##file may be used as input and output
##2 types of files-->Text and Binary

##advantages of file handling: versatility(c,a,w,r,del,rename)
#flexible(allows to work with diff file formats)
##user friendly(easy to create, read and manipulate)
##cross-platform: funtcions work across diff platforms

##limitations:
#error-prone: may provide error if code not written crefully+file permissions,file locks
##security risks:access/modify sensitive files
#complex:if new file formarts / operations introduced
#Performance:file handling operations in python can be slower


#opening of file:f=open("file name",mode='',buffering,encoding=None,errors=None,newline=None,closefd=True)//default value of mode='r'
# f is file handler, file pointer
# f=open("python_code/myfile1.txt",mode='r')
# if f:
#     print("success open")
# print(f.seek(-1,2))
# print(f.tell())
# print(f.read())
# print(f.tell())

##buffering:positive integer value used to set buffer size for file
##buffer memory:temporary memory is part of main memory where data to be processed is stored.
##in text mode, buffer size should be 1 or more than 1 i.e it can read 1 bit at a time
##in binary mode , buffer size can be 0.
#default size:4096-8192 bytes

##encoding:type used to encode and decode file.
##should be used in text mode only.
#default value depends on OS.

#errorS:how encoding / decoding errors are to be handled
#cannot be used in binary mode but only in text mode.
#some standard values are: strict(error ko notify),ignore(ignore the error),replace;

##newline: it can be \n(default),\r,\r\n.

# import os
# f=open("python_code/myfile1.txt",mode='r',buffering=10,encoding='utf-8')## ek time pr 8 bits move to buffer memory
# #returns file object of file class(built-in class)
# # print(type(f))
# # #position / order matters
# f=open("python_code/myfile1.txt",mode='rb')##binary doenot take encoding:encoding nhi hota binary mode mein
# if f:
#     print("success open")
# # print(list(f)) #now cursor has moved to end of file
# data3=f.readline()#[]
# print(data3)
# print(type(data3))
# for line_ in data3:
#     print(line_)
# print(f.readlines())#[] always return a list
# for line in f:
    # print(line)
# line=f.readline()
# line1=f.readline(9)##if size is more than no. of characters in a single line then also single line is only executed
# print(line)
# print(line1)
# data=f.read(5)
# data1=f.read(2)
# data2=f.read(1)
# print(data)
# print(data1)
# print(data2)
# print(os.path.isfile("myfile1.txt")) #we import os

# print(f.readable())
# print(f.writable())

# print(f.name)
# print(f.encoding)
# print(f.closed)
# print(f.mode)

# f.close()##filehandler.close()
# print(f.closed)

##what happens when we close file?
# file object is deleted from memory and file is no more accessible until we open it 

##what happens when we not close file?
#after program execution,python garbage collector will destroy file object  only after whole program is executedand close file automatically
#Posiible outcomes if we rely on garbage collector: Data will curropt and memory wastage

##ways of closing file:
#1. normal way:#not surity given that file willbe closed
# f=open("filenmae",mode="w")
# #operations
# f.close()

# # 2. using exceptional handling:
# try:
#     f=open("filenmae",mode="w")
#     #operations
# finally:#hamesha execute hota hai.
#     f.close()

#3.with statement:f.close() likhne ki zarurat nhi padhti
# with open('filenamee',mode="r") as f:
#     #operations
#     data=f.read()
#     print(read)

##file object variables:
#1.name:has name of specified file.
#2.mode:mode of specified file.
#3.closed:has boolean value.shows file closed/opened.
#4.encoding: has encoding name
#file_object.variable_name;

##file object methods:
##1.readable():method used to check whether file is readable or not
##2.writable():method used to check whether file is writable or not

##to check whether file exists or not we use isfile():
##isfile() method belongs to path module which is submodule of os module
##returns True/False
##import os
# os.path.isfile(filename)

#mode of opening files:mode specifies purpose of opening file.
#there are 2 types of modes:
#1.text mode: content treated as string type. 
# when u get data from text mode file, python first decodes raw bytes using either a platform dependent encoding or specified encoding
#2.binary mode: data is used without any encoding. binary mode file reflects the raw data directly in file.
#python treats file content as bytes type. THese modes are used while dealing with non text files like images,audio,videos

#text_modes-->
# r:read: operation+ if file doesnot exists raises I\O error
##w-->write:data previously written is overridden and creates file if not present
##a-->append: donot override and creates new file if not exists
##r+-->read and write:I/O error if file donot exists
##w+-->write and read
#a+--> append and read
##x-->open for exclusive creation for writing.the specified file must not be available. it creates a new file and then we write data into it. if file exists it will give an error.

##binary modes:
#rb:open for reading in binary mode
#wb:open for writing in binary mode
#ab:open for appending
#xb:open for exclusive creation and writing(same as x)
# rb+:open for read and then write in binary.
#wb+:open for writing and then reading in binary.
#ab+:open for append and then read in binary.

## volatile memory: data removed after execution so need to store data

#reading data from file:
#1.read():method to read data and returns it as a string in text mode. and returns bytes in binary mode
##syntax:file_object.read(size)::size-->no. of characters to be read in text mode and not to be given in binary mode
#in size '\n' and white spaces are also included.
#if size is specified negative or not specified anything then whole content is shared

#2.readline():used to read a single line from a file
##syntax:file_object.readline(size)
#size:no. of characters to be read from a line

#3.readlines():udes to read all lines and !!!!!!!!!!!!!!!!!!!!!!!!!return list of lines

##readline() to read a single line and for multiple lines we will use loop wwhile True:
# f=open("python_code/myfile.txt","r")
# i=0
# while True:
#     i=i+1
#     line=f.readline()
#     if not line:
#         break
#     m1=line.split(' ')[0]##gets first part of split
#     m2=line.split(' ')[1]##gets second part of split
#     m3=line.split(' ')[2] ##gets third part of split
#     print(f"Marks of student {i} in Maths is: {m1}")   
#     print(f"Marks of student {i} in eng is: {m2}") 
#     print(f"Marks of student {i} in science is: {m3}")
#     print(line) 

## writelines()
#The writelines() method takes an iterable (such as a list) of strings as input and writes each string to the file. 
# It does not automatically add newline characters between the strings
# f=open("python_code\myfile.txt","w")
# lines=['line1\n','line2\n','line3\n']
# f.writelines(lines)
# f.close()

# ##writelines() with loop
# f=open("python_code/file2.txt","w")
# lines=['line1','line2','line3']
# for line in lines:
#     f.writelines(line)
# f.close()

##difference between readline() and writelines():
##readline(): it is used to read a single line in file. It returns next line of the file as a string
#  and newline character at the end of the line.

##The writelines() method takes an iterable (such as a list) of strings as input and writes each string to the file. 
# It does not automatically add newline characters between the strings

##readlines(): reads all the lines of file and returns them as a ''list of strings''.
##Each string in the list represent a single line from the file,
#  including the new line character at end of each line.

##readline(): it is used to read a single line in file. It returns next line of the file as a string
#  and newline character at the end of the line.
# ##If we have reached to the end of the file , it returns an empty string ''.
# f=open("python_code/myfile.txt","r")
# line1=f.readlines()
# print(line1) ##56 65 49
#              ##
# print(len(line1[1]))
# line2=f.readline()
# print(line2) ##34 0 78
#              ##
# line3=f.readline() ## end of the file
# print(line3) ## 35 89 97 ''

##readlines(): reads all the lines of file and returns them as a ''list of strings''.
##Each string in the list represent a single line from the file,
#  including the new line character at end of each line.
# with open("python_code\myfile.txt","r") as f:
#     lines=f.readlines()
#     print(lines)

##Data type of any file is _io.TextIOWrapper
# f=open("python_code/myfile1.txt","r")
# print(type(f))

# ##use of seek() function:used to change position of file pointer
# start from 0 
# f=open("python_code/file2.txt","r")##192004gupta@gmail.com
# f.seek(10)##192004gupta 10th byte tk pahunchna
# data=f.read(5)#a@gma vahan(usi pt se/use include krte huye) se next 5 bytes read krni
# print(data)# 11th 12th 13th 14th 15th
# f.close()

# ssek krke jahan pahunche vahin se read hona shuru hoga 

##f.tell() and f.seek() ko index ke basis pr dekhte hain.....!!!
##use of tell():method used to find current position of file pointer from beginning of file starts from 0.
# f=open("python_code/file2.txt","r")
# data=f.read(7)
# print(data)##192004g
# print(f.tell())#initially=0 ,now yahan pr 7 index aayega
# print(f.read())#completly read krlega
# print(f.tell())#index 21 aayega

# f.read() ke baad wala index f.tell() print krega 

# f=open("python_code/file2.txt ","r")
# data=f.read(10)#192004gupt
# print(data)
# # current_position=f.tell()#10
# # f.seek(current_position) 
# print(f.tell())

##truncate() function:used to resize file to specific size
# with open("python_code/file2.txt","a") as f:
#     f.write("Diya Gupta is a goood girl")
#     f.truncate(36)

#detach() method:
#file descriptor(raw stream object)
# used to separate file descriptor from file object.
# file descriptor:unique identifier/integer value that os to files that is opened by process
#method returns raw stream object rather than file object
#Raw stream object:lower level abstraction closer to file descriptor
#file object:higher level of absrractions

# Open a file for writing
# file_obj = open("python_code/file2.txt", mode='w', encoding='utf-8')
# # Detach the file object from the underlying stream
# raw_stream = file_obj.detach()
# # Now, you can use the raw stream object directly
# # For example, you can write to the file using the raw stream
# raw_stream.write(b"Hello, world!\n")##lower level abstraction
# # Close the raw stream (not necessary if you've already closed the file object)
# raw_stream.close()

##fileno(): used to obtain file descriptor
# Open a file
# file_obj = open("python_code/file2.txt", mode='r')
# Get the file descriptor associated with the file object
# fd = file_obj.fileno()
# This method is mainly used when you need to work with low-level operating system functions or when interacting 
# with external libraries that require file descriptors.
# Now you can use the file descriptor for low-level operations, if needed
# For example, you can use it with os.read() or os.write()
# print(fd)
# print(type(fd))
# import os
# data = os.read(fd, 5)# Read up to 5 bytes from the file using the file descriptor
# print(data)
# file_obj.close()

##flush(): used to ensure any buffered data is written immediately
#buffer is region of memory where temporary storage of data 
#while it is being transferred b/w program and I/O device(file,terminal,network socket)
#program data-->buffer memory-->I/O devices
##buffering improves performance by reducing no. of system calls needed to write data
#flush method is used when we want data to be written immediately withut buffering or waiting for file to be closed

# file_obj = open("example.txt", mode='w')
# file_obj.write("Hello, world!")
# # Flush the data to ensure it's written immediately
# file_obj.flush()
# file_obj.close()

#isatty() method:return True/False
# True:if file descriptor is associated with terminal
# import sys
# # Check if stdout (standard output) is associated with a terminal
# # sys.stdout.isatty(),sys.stdin.isatty(),sys.stderr.isatty()::TRUE
# if sys.stdout.isatty():
#     print("stdout is associated with a terminal")
# else:
#     print("stdout is not associated with a terminal")
# # Open a file and check if it's associated with a terminal
# file_obj = open("python_code/file2.txt", mode='w')
# if file_obj.isatty():
#     print("File is associated with a terminal")
# else:
#     print("File is not associated with a terminal")
# #false:input /output is redirected to file/another program rather than terminal
# file_obj.close()

# from io import BytesIO
# #BytesIO is to write binary data in file
# write_byte=BytesIO(b'\xC3\x80')#represents hexadecimal
# #xC3 and x80 are hexadecimal values
# with open("test.bin","wb") as f:#bin file is used to store binary data
#     f.write(write_byte.getbuffer())
# So, in your code, write_byte.getbuffer() is like opening the BytesIO box 
# and looking at the binary data inside. Then, f.write() takes that data and 
# writes it directly to a file without making an extra copy. 
# This is faster and saves memory, especially when dealing with a lot of data.

##steganography:hiding 1 data within other data


#id of same list is different
# list1=[1,2,3]
# list2=[1,2,3]
# print(list1 is list2)
# print(list1==list2)

# a=10
# b=10
# print(a==b)
# print(a is b)

# print("Diya is %s girl but fat"%'good')
# print("Diya is %s " %'good ' "girl but fat")
# print("MIsha %s" %'walked' "and %s around" %'looked')

# print("{a2} {a4} {a3} {a1}".format(a1="Smart",a2="A",a3="Students",a4=3))

# point ke baad jitna number hoga utne places tk roundoff hojaayega
#%5.3 means rouund off given number to 3 places

# print(f"Age is:{(lambda x:x*2)(x=2)}")
# print(f"List op. {(lambda x:[x]*2)(x=[2,4,6])}")

##{value/variable:{digits before decimal pt}.{max total digits}}
# t=31.4159
# print(f"pi is: {t:{1}.{5}}")

# t=153.14159
# print(f"pi is:{t:{3}.{2}}")
##.format()-->{[index]:[width][.precision][type]}
#f-->floating point numbers
#e--> floating point in exponent form
##id of same tuples is same
# tup1=(1,2,3)
# tup2=(1,2,3)
# print(tup1 is tup2)
# print(tup1==tup2)

##id of same sets is different
# set1={1,2}
# set2={1,2}
# print(set1==set2)
# print(set1 is set2)

##id of same dictionaries is different
# dict1={'one':1,'two':2}
# dict2={'one':1,'two':2}
# print(dict1 is dict2)
# print(dict1==dict2)

##jo cheez immutable hoti python ko pta hai vo change nhi hoga toh uske liye pehle se ek memory allocate krdi jaati jaise ki for tuple and for constant
##strings,constant/int,tuple are immutable so have same id for same.

##strings are immutable
# a="Diya"
# b="Diya"
# print(a==b)
# print(a is b)

# a=None
# b=None
# print(a is b)
# print(a==b)

##Lab Assignment 9:
##counting vowels
# def count_vowels(s):
#     count=0
#     vowels=['a','e','i','o','u']
#     for i in s.lower():
#         if i in vowels:
#             count+=1
#     return count

# str=input("Enter any string=")
# c=count_vowels(str)
# print(c)

##pallindrome
# def pallin(s):
#     if s==s[::-1]:
#         return 1
#     else:
#         return 0
# str=input("Enter any string=")
# rev_str=(pallin(str))
# if rev_str==0:
#     print("not p")

##no. of letters and digits in string
# def dig(s):
#     digit=0
#     letter=0
#     for i in s:
#         if i.isalpha():
#             letter+=1
#         if i.isdigit():
#             digit+=1
#     print("Digits=",digit)
#     print("Letters=",letter)

# str=input("Enter any string:")
# dig(str)

##reverse string using stack method
# str=input("Enter string=")
# stack=[] ##list
# for i in str:
#     stack.append(i) 
# r_str=''
# # while stack:
# for c in range(len(stack)):
#     r_str+=stack.pop()
# print("reverse=",r_str)

###reverse method:''.join(reversed(string))
# reverse_str=''.join(reversed(str))
# print("reverse=",reverse_str)

# def longest(lst):
#     maxcount=0
#     long=""
#     for word in lst:
#         if maxcount<len(word):
#             maxcount=len(word)
#             long=word
#     return maxcount,long
# list=["name","PHP","Exercises","Backend"]
# count,len=longest(list)
# print("Longest word=",len)
# print("Length of longest word =",count)

# str1=input("Enter the string1:")#abd
# str2=input("Enter the string2:")#xyz
# # str3=str1+" "+str2#abd xyz
# new_str1=str2[:2]+str1[2:]
# new_str2=str1[:2]+str2[2:]
# str3=new_str1+" "+new_str2
# print(str3)



# lst=["diya","khyati","namu","mumma","papa"]
# lst=['red','blue','green','red']
# lst=[word.strip() for word in lst]#removes leading and trailing extra spaces from word in list
# distinct_words=list(set(lst)) #conversion into set to remove duplicate and then again into list
# distinct_words.sort()#using list.sort()
# for word in distinct_words:
#     print(word)

###Aliasing:Means to create deep copy. They will have same id only different names.Changes will be reflected in both.
##1
# a=1
# b=a
# print(a)
# print(b)
# print(id(a))
# print(id(b))
# a=a+1 # will not bring change in value of b
# print(a)
# print(b)

##2
# warm=['red','yellow','orange']
# hot=warm##deep copy is formed hot and warm have same id
# print(id(hot))
# print(id(warm))
# hot.append('pink') #will bring change in warm also
# print(hot) 
# print(warm)
# hot[2]='abc'#will bring change in warm also
# print(hot) 
# print(warm)

##Cloning:copying. deep copy is formed.
#alaising: diff name same id change reflected everywhere
# cool=['blue','green','grey']
# chill=cool#shallow copy
# print(id(chill))#id will be same
# print(id(cool))
# chill.append('black')#will bring change in cool
# print(chill)
# print(cool)

##Summary:Aliasing means different names but same id done by lst1=lst2 , changes done in one will be reflected in other.Aliasing is done by assignment operator.
##cloning creates 2 copies having different ids and change done will not be reflected in other. lst2=lst1[:]
##cloning is done by append() ,extend() ,slicing,.copy(),list comprehension.list method
##Different ways to clone:
##1 slicing Technique: 
# li1=[2,3,5,1,6]
# li2=li1[:]

##2 extend method():
# li1=[2,3,5,1,6]
# li2=[]
# li2.extend(li1)
# print(li2)
# li2.append("diya")
# print(li2)
# print(li1) ##no changes in li1 according to defination of cloning

# ##3 Method of deep copy:
# import copy
# li1=[2,3,5,1,6]
# li2=copy.copy(li1)
# print(li2)
# li2.append("diya")
# print(li1)
# print(li2)

##4 Using list comprehension:
##syntax:newlist=[expression(element) for element in oldlist if condition]
#expression:represent operation want to execute on every item
#element:value taken from iterable
#eg1
# li1=[2,3,5,1,6]
# li2=[i for i in li1] ##offer shorter syntax when u have to create a new list
# print(li2)
# li2.append("diya")
# print(li1)
# print(li2)

#5: list() method:
# list1=[1,2,3]
# list2=list(list1)
# print(list2)
# list2.append(3)
# print(list1)
# print(list2)

# list_=[1,2]
# list_=list_.append(4)#returns None
# print(list_)

#eg2:
# num=[1,2,3,4,5]
# squared=[x**2 for x in num] #list comprehension
# print(squared)

#eg3: if old list is not given
# list=[i for i in range(11) if i%2==0]
# print(list)

###geeks4geeks imp questions
# lis = [num for num in range(100)  if num % 5 == 0 if num % 10 == 0] ##checks for both divisible by 10 and 5
# print(lis)

# import time 
# def for_loop(n): 
#     result = [] 
#     for i in range(n): 
#         result.append(i**2) 
#     return result 
# # define function to implement list comprehension 
# def list_comprehension(n): 
#     return [i**2 for i in range(n)] 
# begin = time.time() 
# for_loop(10**6) 
# end = time.time() 
# print('Time taken for_loop:', round(end-begin, 2)) 
# begin = time.time() 
# list_comprehension(10**6) 
# end = time.time()  
# print('Time taken for list_comprehension:', round(end-begin, 2)) 

#eg4:##nested list comprehension   !!!!!!!!important
##[j for j in range(1,3)]:inner loop will iterate for 3 times dependent on outer loop i.e i in range (3)
# matrix=[[j for j in range(1,3)] for i in range(3)]
# print(matrix)

# !!!!!very important transpose of matrix!!!!!!
# Assign matrix 
# twoDMatrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]] 
# trans = [[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix[0]))] 
# print(trans) 

# !!!imp:zip(,)
# names = ["G", "G", "g"] 
# ages = [25, 30, 35] 
# print(zip(names,ages))
# data=zip(names,ages)
# print(data)
# print(list(data))

#  !!!geek4geeks
#bit being "set," it means that its value is 1. Conversely, when a bit is "unset" or "clear," its value is 0.
# def digitSum(n): 
# 	dsum = 0
# 	for ele in str(n): 
# 		dsum += int(ele) 
# 	return dsum 
# List = [367, 111, 562, 945, 6726, 873] 
# newList = [digitSum(i) for i in List if i & 1] ##if (i & 1)--> checks if least significant bit is odd i.e. one
# ##so it filters odd number from list
# print(newList) 

##slicing in negative indices
#  Leaving the Initial and End as blank. 
#  We need to choose the Initial and End values according to a reversed list if the IndexJump value is negative. 
# List = ['Geeks', 4, 'geeks !']
# print("Original List:\n", List)
# print("\nSliced Lists: ")
# print(List[::-1])
# print(List[::-3])#['geeks !',4,'Geeks'] negative jump means to reverse it and then do it normally skipping 2 elemnest
# print(List[:1:-2])#['geeks !',4,'Geeks']-->now treat as [0:1:2]

##very important
# List = [-999, 'G4G', 1706256, '^_^', 3.1496]
# print(List[10::2])#
# print(List[1:1:1])#
# print(List[-1:-1:-1])
# print(List[:0:])

# !!!!!!!modifying with help of slicing
# List = [-999, 'G4G', 1706256, 3.1496, '^_^']
# List[2:4] = ['Geeks', 'for', 'Geeks', '!'] #replaces from index 2-->3 with given elements
# print(List)
# List[:6] = []
# print(List)

# List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# newList = List[:3]+List[7:]##[1,2,3,8,9]
# print(newList)
# List = List[::2]+List[1::2]##[1,3,5,7,9,2,4,6,8]
# print(List)

# def sort_list(list1, list2):
#     zipped_pairs = zip(list2, list1)
#     # print(list(zipped_pairs))
#     # print(list( zip(list2, list1)))
#     z = [x for _, x in sorted(zipped_pairs)]#_,-->used to ignore particular element deliberately
#     return z
# x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
# y = [0,   1,   1,    0,   1,   2,   2,   0,   1]
# print(sort_list(x, y))
# x = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
# y = [0,   1,   1,    0,   1,   2,   2,   0,   1]
# print(sort_list(x, y))

# def sorting_of_element(list1, list2):
#     final_list = []
#     #converting list to dictionary
#     f_1 = {list1[i]: list2[i] for i in range(len(list2))}##{'a':0,'b':1,'c':1,'d':0,'e':1,'f':2,'g':2,'h':0,'i':1}
#     f_lst = {k: v for k, v in sorted(f_1.items(), key=lambda item: item[1])}#{'a':0,'d':0,'h':0,'b':1,'c':1,'e':1,'i':1,'f':2,'g':2}
#     # sorted(f_1.items(), key=lambda item: item[1]):key parameter specifies function that takes second element of tuple (item)
#     for i in f_lst.keys():
#         final_list.append(i)
#     return final_list
# list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
# list2 = [0,   1,   1,    0,   1,   2,   2,   0,   1]
# list3 = sorting_of_element(list1, list2)
# print(list3)

# list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
# list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]
# a = list(set(list2))#[0,1,2]
# a.sort()#[0,1,2]
# res = []
# for i in a:
#     for j in range(0, len(list2)):#range(0,9)
#         if(list2[j] == i):
#             res.append(list1[j])#['a','d','h','b','c','e','i','f','g']
# print(res)

# The collections module in Python provides additional data structures beyond the built-in data types like lists, tuples, dictionaries, and sets. These data structures offer specialized ways to store and manipulate data,
#  which can be more efficient or convenient for certain tasks
##OrderedDict: subclass of dict taht maintains order of insertion of items
# from collections import OrderedDict
# list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
# list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]
# d = OrderedDict(zip(list1, list2))
# # res = list(OrderedDict(sorted(d.items(), key=lambda x: x[1])))
# res = [(k, d[k]) for k in sorted(d, key=d.get)]
# print(res)##retrieves only keys in first case

##very important use of argsort retuns array of indices after sorting element of list
# import numpy as np
# # Define a function that takes two lists as input, sorts the first list based on
# # the order of the second list, and returns the sorted list as a numpy array
# def sort_list(list1, list2):
#     # argsort() returns an array of indices that would sort the input array. 
#     # These indices can then be used to sort another array based on the order of elements in the input array.
# 	idx = np.argsort(list2)
# 	# Index the first list using the sorted indices and return the result as a numpy array
# 	return np.array(list1)[idx]
# x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
# y = [0, 1, 1, 0, 1, 2, 2, 0, 1]
# print(sort_list(x, y))
# x = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
# y = [0, 1, 1, 0, 1, 2, 2, 0, 1]
# print(sort_list(x, y))


# # !!!!!very inmportant
# string = 'Geeks4Geeks'
# List = list(map(lambda i: chr(ord(i) ^ 32), string)) #ord(i)-->ASCII code , ord(i)^32-->XOR(converts a-->A,A-->a)
# print(List)

##5 using append method:
# li1=[2,3,5,1,6]
# li2=[]
# for i in li1:
#     li2.append(i)
# print(li2)
# li2.append("diya")
# print(li1)

##6 list.copy()##.copy() donot take any argument
# list1=[1,4,6,7]
# list2=list1.copy()
# print(list2)
# print(id(list1))
# print(id(list2))
# list2.append(5)
# print(list1)
# print(list2)
                ##lab assignment 10
##2 
#by slicing
# list1=[1,2,3]
# list2=list1[:]
# print(list2)
# print(id(list1))
# print(id(list2))

#by extend() method:
# list1=[1,2,3]
# list2=[]
# list2.extend(list1)
# print(list2)
# print(id(list1))
# print(id(list2))

# by list() method:
# list1=[1,2,3]
# list2=list(list1)
# print(list2)
# print(id(list1))
# print(id(list2))

#by list comprehension:
# list1=[1,2,3]
# list2=[i for i in list1]
# print(list2)
# print(id(list1))
# print(id(list2))

#by append method():
# list1=[1,2,3]
# list2=[]
# for i in list1:
#     list2.append(i)
# print(list2)
# print(id(list1))
# print(id(list2))

# by copy method:
# list1=[1,2,3]
# list2=[]
# list2=list1.copy()
# print(list2)
# print(id(list1))
# print(id(list2))

#by map(method):
# list1=[1,2,3]
# cloned_list=list(map(lambda x:x,list1))
# print(cloned_list)
# print(id(list1))
# print(id(cloned_list))
##1
# def majority(lst):
#     dict={}
#     maxcount=0
    
#     # for i in range(len(lst)):
#     #     for j in range(i+1,len(lst)):
#     #         if lst[i]==lst[j]:
#     #           print(dict.keys())
#     #           dict.keys[i]=lst[i]
#     #           dict.values[i]+=1 
#     #         else :
#     #             continue
#     #     print(dict)
# lst=[1,2,3,4,3,3,2,6,5]
# x=majority(lst)
# print(x)


##4 a
# list1=[1,2,3,4,5,4]
# print(list(set(list1)))

##4 b
# list1=[1,2,3,4]
# list1.reverse()
# print(list1)

##4 c
# list1=[1,2,3,4]
# if list==[]:
#     print("It is empty")
# else:
#     print("it is not empty")

##4 d
# def target(lst):
#  for i in range(len(list1)):
#     if list1[i]==n:
#         return i
#     else:
#         continue
# n=int(input("Enter the number="))
# list1=[1,2,1,4,2,3,4]
# x=target(list1)
# print("index is=",x)

 ##4 e
# list1=[1,2,3,4,5,6,3,7]
# list2=[i for i in list1 if i%2==0]
# print(list2)

##4 f
# list1=[1,2,3,4,5,6,3,7]
# n=int(input("Enter the number u want to remove:"))
# list1=[i for i in list1 if i!=n]
# print(list1)

##4 g
# list1=[1,2,5,4,7,3,8]
# list2=[9,4,6,3,7,2,8]
# set1=set(list1)
# set2=set(list2)
# set1.intersection_update(set2)
# print(list(set1))

##4 h !!important
# def flatten_list(lst):
#     flattened=[]
#     for sublist in lst:
#         if isinstance(sublist,list):
#             flattened.extend(flatten_list(sublist))
#         else:
#             flattened.append(sublist)
#     return flattened

# list1=[[1,2,3,4,5],[5,3],[4,5,3],[[9,6],[3,0]]]
# x=flatten_list(list1)
# print(x)


##isinstance() function is used to check if an object belongs to specific class or data type
# x=5
# if isinstance(x,int):
#     print(x is int)

##3
# def generate_parenthesis(n):
#     def backtrack(s='',left=0,right=0):#left represent count of open parenthesis and right represent count of close
#         if len(s)==2*n: #means all n pairs of parenthesis have been used
#             result.append(s)
#             return
#         if left<n:
#             backtrack(s+'(',left+1,right) #recursively calls until left=n
#         if right<left:
#             backtrack(s+')',left,right+1)
#     result=[]
#     backtrack()
#     return result
# n=3
# print(generate_parenthesis(n))


##1
# def majority_func(ist):
#     count_dict={}
#     for num in lst:
#         if num in count_dict:
#             count_dict[num]+=1
#         else:
#             count_dict[num]=1
#         max_count=0
#         max_elements=[]
#     for key,value in count_dict.items():
#         if value>max_count:
#             max_count=value
#             max_elements=[key]
#         elif value==max_count:
#             max_elements.append(key)
#     return max_elements       
# lst=[1,3,3,4,3,5,6,4,7,5]
# print(majority_func(lst))

# nums=list({1:'one',2:'two'})#list() method converts keys of dictionary to list
# print(nums)

# list_=['one','two','three','four']
# # print(list_.sort()) #list.sort() returns none
# list_.sort()
# print(list_)#lexicographical order

                                  ###!!!!!!lsr.clear() == del lsr[:]
# lsr=[1,2,3,4,5]
# # del lsr
# # print(lsr)#nameerror
# # del lsr[:]
# # print(lsr)#[]
# lsr.clear()###lsr.clear() == del lsr[:]
# print(lsr)

# lst=[1,2,3]
# lst[:]=[4,5,6]
# print(lst)

# n=max('ten',10,10.00) #Typeerror as cannot comparestring and integer
# print(n)

# n=max(10.00,10)
# print(n)
# n=max(10,10.00)    #integer are implicitly converted to float when compairing
# print(n)

# names=('jeff','Bill')
# # a,b,c,d= names#nameerror not enough values to give
# a,b=names
# print("Hello",a)
# print("Hello",b)

# a=[1,2,3,4]
# print(id(a))
# # b=a[::-1] #reverse of a
# # print(id(b)) #different id of b
# a=a[::-1] #reverse of a
# print(id(a)) #different id

# a=1
# b=a
# #id of a and b will be same
# print(id(a))
# print(id(b))
# a=a+1
# #id of a will be changed but b will remain same
# print(id(a))
# print(id(b))

##quiz2
# t1=(1,2,3)
# t2=(2,)
# print(t2>t1)//True

##syntax to check number of dimensions in numpy array:
#numpy_array_name.ndim

# sampleList=[10,20,30,40]
# del sampleList[0:6]
# print(sampleList)

# method to convert array to list:
# tolist()
# import numpy as np
# arr=np.array([1,2,3])
# list_array=arr.tolist()
# print(type(list_array))
# print(list_array)

#syntax to know datatype of an array:
# numpy_array_name.dtype

#syntax to initialize empy array:
# import array
# my_array=array.array('i',[])

# Tup=('Py',)
# print(Tup*3)

# When we say that blist contains two references to the same list, it means that blist is a list where both of its
#  elements point to the same memory location in the computer's memory where the list alist is stored.
# alist=[4,2,8,6,5]
# blist=[alist]*2##blist created a list with same reference . alist list is getting repeated twice in blist
# alist[3]=999
# print(blist)

# alist=[4,2,8,6,5]
# blist=(alist)*2##alist elements are getting repeated twice in blist
# alist[3]=999##doesnot affect blist as blist is created different
# print(blist)

# # Dictionary methods
dict1={"name":"Diya","Branch":"IT"}
# print(dict1.keys())##dict_keys(['name,'brnach])
# print(type(dict1.keys()))##classs dict_keys
# print(dict1.values())
# print(type(dict1.values()))##classs dict_values

# # get method(): dict.get(key,default value):default value is returned if key is not found if not provided then Non exist returned
# print(dict1.get('name'))
# print(type(dict1.get('name')))##str
# print(dict1.get('age',"Mention your age"))
# print(dict1.get('age'))##if key is not present then None is output

#!!!!!!!!!In this case first there is shallow copy but id of original and copied dictionary is not same,
# key and values have same addresses. change in on will not be reflected in other. 
# after changing value ,id of keys will not remain same
# dict_o={'a':1,'b':2,'c':3}
# copy_dict=dict_o.copy()##new dictionary with references to same keys and values as orginal 
# but keys and values are not recursively copied
# print(id(dict_o))
# print(id(copy_dict))
# print(id(copy_dict['a']))
# print(id(dict_o['a']))
# copy_dict['a']=9
# print("----------------------------------------------")
# print(copy_dict)
# print(dict_o)
# print(id(copy_dict['a']))
# print(id(dict_o['a']))
# print(id(copy_dict['b']))
# print(id(dict_o['b']))
# copy_dict['d']=10
# print(copy_dict)
# print(dict_o)
# in this case id of original and copied would be differnt becoz copy creates new object but copies references to smae keys and values from original dictionay.

##however if values are mutable:
# id of both original and copied will be different
# orig_dict={'a':[1,2,3],'b':[4,5,6]}
# copied_dict=orig_dict.copy()
# print(id(copied_dict))#id will be different
# print(id(orig_dict))
# print(id(copied_dict['a'][0]))
# print(id(orig_dict['a'][0]))
# copied_dict['a'][0]=100
# print(copied_dict)#change reflected in both as they copy refernces of mutable vlaue soc hange in one is reflected in both
# print(orig_dict)
# copied_dict['a']=1
# print(copied_dict)
# print(orig_dict)

#summary:1.shallow copy copies references to values.
# 2. for immutable objects, changes in values of one dictiaionary not visible in other becoz integers,strings are immutable objects
#3. for mutabl;e objects changes in one are reflected in other

#items( )method:
# dict1={"name":"Diya","Branch":"IT"}
# print(dict1.items())
# print(type(dict1.items()))#class dict_items
# print((dict1.items()))

#setdefault method :it is to set default value for a key that may not exist in dictionary. returns value of lkye if it is present. if not present the  it inserts key with specified default value and returns that value.
# dict.setdefault(key,default_value)
# mydict={'a':1,'b':2,'c':3}
# value_a=mydict.setdefault('a',100)#dopenot changes value of existing
# print(value_a)
# print(mydict)
# print((mydict.setdefault('e',10)))##returns value
# print((mydict.setdefault('f')))
# value_a=mydict.setdefault('d',100)#changes value of non-existing
# print(mydict)

#update() method:
# my_dict={'a':1,'b':2}
# other_dict={'b':3,'c':4}
# my_dict.update(other_dict)
# print(my_dict)#value of b will be updated and c key will be added
# print(other_dict)

# my_dict={'a':1,'b':2}
# key_value=[('b',3),('c',4)]
# my_dict.update(key_value)
# print(my_dict)#b will be updated and c key will be added

# dictionary comprehension:
# my_dict={'a':1,'b':2,'c':3}
# iff= my_dict.has_key('a')
# print(iff)
# new_dict={key.upper(): value**2 for key,value in my_dict.items()}
# print(new_dict)
# print(my_dict)

# print(my_dict.clear())#None
# my_dict.clear()
# print(my_dict)##{}

# del my_dict
# print(my_dict)#NmaeError

# del my_dict['a']#remeber it is square bracket
# print(my_dict)

# Dict = {} 
# print("Empty Dictionary: ") 
# print(Dict) 
# Dict[0] = 'Geeks'
# Dict[2] = 'For'
# Dict[3] = 1
# print("\n Dictionary after adding 3 elements: ") 
# print(Dict) 
  
# Dict['Value_set'] = 2, 3, 4
# print("\nDictionary after adding 3 elements: ") 
# print(Dict) 
# print(type(Dict['Value_set']))
  
# Dict[2] = 'Welcome'
# print("\nUpdated key value: ") 
# print(Dict) 
# Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}} 
# print("\nAdding a Nested Key: ") 
# print(Dict) 

##fromkeys(seq,values)-->creates dictionary from key and values
#1
# seq = ('a', 'b', 'c')
# print(dict.fromkeys(seq, None))

#2
# seq = {'a', 'b', 'c', 'd', 'e'}
# res_dict = dict.fromkeys(seq)
# print("The newly created dict with None values : " + str(res_dict))
# res_dict2 = dict.fromkeys(seq, 1)
# print("The newly created dict with 1 as value : " + str(res_dict2))

# seq = {'a', 'b', 'c', 'd', 'e'}
# lis1 = [2, 3]
# res_dict = dict.fromkeys(seq, lis1)
# print("The newly created dict with list values : "+ str(res_dict))
# lis1.append(4)
# print("The dict with list values after appending : ", str(res_dict))
# lis1 = [2, 3]
# print('\n')
# res_dict2 = {key: list(lis1) for key in seq}
# print("The newly created dict with list values : "+ str(res_dict2))
# lis1.append(4)
# print("The dict with list values after appending (no change) : "+ str(res_dict2))

# Python3 code to demonstrate 
# to initialize dictionary with list 
# using fromkeys()

# using fromkeys() to construct
# new_dict = dict.fromkeys(range(4), [])
# print ("New dictionary with empty lists as keys : " + str(new_dict))

# d={"name":"diya","age":19}
# d.pop('age')##one argument is important to give in dictionary
# print(d)

##ways to write update methodd():
# D1={'A':'B5'}
# D1.update(B='passed',C='python')
# D1.update({'key':800})
# print(D1)

# !!!!very important
# a=2,
# print(type(a))#tuple
# print(type((2,)))#tuple
# print(type(2,))#int
# b=(2)
# print(type(b))#int
# print(type((2)))#int

# a=0
# b=20
# c=b/a
# print(c) ##ZerpDivisionError

##lab assignment 11:

##1
# tup1=(1,2,3)
# tup2=(4,5,6)
# n=int(input("Enter a number="))
# tup3=(tup1+tup2)*n
# print(tup3)

##2 
# def tuple_to_list(tuple_):
#     if isinstance(tuple_, tuple):
#         return [tuple_to_list(item) for item in tuple_]
#     elif isinstance(tuple_, list):
#         return [tuple_to_list(item) for item in tuple_]
#     else:
#         return tuple_
# def list_to_tuple(list_):
#     if isinstance(list_, list):
#         return tuple(list_to_tuple(item) for item in list_)
#     elif isinstance(list_, tuple):
#         return tuple(list_to_tuple(item) for item in list_)
#     else:
#         return list_
# nested_tuple = (1, (2, 3), [4, (5, 6)])
# nested_list = [[1, 2], [3, [4, 5]], 6]
# conv_list = tuple_to_list(nested_tuple)
# conv_tuple = list_to_tuple(nested_list)
# print("Converted Tuple to List:", conv_list)
# print("Converted List to Tuple:", conv_tuple)

##3
# tup1=(1,2,3)
# tup2=(3,4,1)
# flag=True
# if len(tup1)!=len(tup2):
#     flag=False
# for i in range(len(tup1)):
#     if tup1[i]==tup2[i]:
#         flag=True
#         continue
#     else:
#         flag=False
#         break
# if flag==True:
#     print("Tuples are equal element wise")
# else:
#     print("Tuples are not equal element wise")

##4
# def fun(*numbers):
#     sum=0
#     product=1
#     for number in numbers:
#         sum+=number
#         product*=number
#     return (sum,product)
# s=fun(1,2,3,4,5,6)
# print(s)

# zip () function is used to combine multiple iterables element wise into tuples.
#it takes one or more iterables and return iterator thta generate tuples wherethe i-th tuple contain i-th element from each of input iterables
# list1=[1,2,3]
# list2=['a','b','c']
# list3=['x','y','z']
# zipped=zip(list1,list2,list3)
# for item in zipped:
#     print(item)

#if input iterables are of varying length:
# list1 = [1, 2, 3]
# list2 = ['a', 'b']
# zipped = zip(list1, list2)
# for item in zipped:
#     print(item)

#if iterables are tuple
# tup1=(1,2,3)
# tup2=(3,2,5)
# zipped=zip(tup1,tup2)
# for item in zipped:
#     print (item)

#unzipping:
# pairs=[(1,'a'),(2,'b'),(3,'c')]
# numbers,letters=zip(*pairs)
# print(numbers)##tuple
# print(letters)##tuple

# #combining with enumerate():
# names=['Alice','Bob','Charlie']
# for index,name in zip(range(len(names)),names):
# # for index,name in enumerate(names):
#     print(f"Index {index}:{name}")

##creating dictionaries:
# keys=['a','b','c']
# values=[1,2,3]
# dictionary=dict(zip(keys,values))
# print(dictionary)

##5
# list1=[1,2,3]
# list2=[4,5,6]
# zipped=zip(list1,list2)
# list3=[]
# for item in zipped:
#     list3.append(item)
# print(list3)
# number1,number2 = zip(*list3)##assignment operator
# print(list(number1))
# print(list(number2))

##6
# list1=[1,(2,3),5,(1,3,6,(7,8)),(),8]
# for item in list1:
#     if isinstance(item,tuple):
#         if item==():
#             list1.remove(item)
#         else:
#             continue
#     else:
#         continue
# print(list1)

# ##!!important
# def remove_empty_tuples(list_of_tuples):
#     return [tuple_ for tuple_ in list_of_tuples if tuple_]
# list_of_tuples = [(1, 2), (), (3, 4), (), (), (5, 6), ()]
# filtered_list = remove_empty_tuples(list_of_tuples)
# print("List after removing empty tuples:", filtered_list)

##7
# tup1=(3.4,7.5,4.2,2.9,9)
# list1=list(tup1)
# list1.sort()
# print(tuple(list1))

# def sort_tuple_by_float(input_tuple):
#     sorted_tuple = tuple(sorted(input_tuple))
#     return sorted_tuple
# input_tuple = (3.5, 1.2, 4.0, 2.1)
# sorted_tuple = sort_tuple_by_float(input_tuple)
# print(sorted_tuple)

# ##sorted()
# tup1=(1,4.5,3,2,7.9,4.6)
# sorted_tup=sorted(tup1)
# print(sorted_tup)##returns list
# print(tuple(sorted_tup))

# def sort_tuple_by_float(tuple_list):
#     sorted_tuple = sorted(tuple_list, key=lambda x: float(x[1]))
#     return sorted_tuple

# # Example usage:
# tuple_list = (('a', '3.5'), ('b', '1.2'), ('c', '4.0'), ('d', '2.1'))
# sorted_tuple = sort_tuple_by_float(tuple_list)
# print(sorted_tuple)

# def flatten_list(lst):
#     flattened=[]
#     for sublist in lst:
#         if isinstance(sublist,list):
#             flattened.extend(flatten_list(sublist))
#         else:
#             flattened.append(sublist)
#     return flattened

# list1=[[1,2,3,4,5],[5,3],[4,5,3],[[9,6],[3,0]]]
# x=flatten_list(list1)
# print(x)
##8
# def average(lst):
#     total=sum(lst)
#     count=len(lst)
#     return total/count if count>0 else 0
# def flatten (tup):
#     flattened=[]
#     for subtup in tup:
#         if isinstance(subtup,tuple):
#             flattened.extend(flatten(subtup))
#         else:
#             flattened.append(subtup)
#     return flattened
# tup=(1,(2,3),(7,(8,9),10,(11,5),9))
# list_=flatten(tup)
# avg=average(list(list_))
# print(avg)


# def average_tuple_of_tuples(tup):
#     flattened = [item for sub_tup in tup for item in sub_tup if isinstance(item, (int, float))]
#     total = sum(flattened)
#     print(total)
#     count = len(flattened)
#     return total / count if count > 0 else 0
# tup = ([1, 2, 3], (4,(5,6) ,5), (6, 7, 8, 9))
# avg = average_tuple_of_tuples(tup)
# print("Average:", avg)

##9
# tup=("Dal","Paneer","Rice","Butter Naan","Onion")
# list_=list(tup)
# list_[0]="Rajma"
# list_[3]="Lady finger"
# for food in list_:
#     print(food)

##10
# def calculate_average_scores(students):
#     num_students=len(students)
#     # num_subjects=len(students[0])-1
#     math_sum=0
#     science_sum=0
#     eng_sum=0
#     for student in students:
#         math_sum+=student[1]
#         science_sum+=student[2]
#         eng_sum+=student[3]
#     math_avg=math_sum/num_students
#     science_avg=science_sum/num_students
#     eng_avg=eng_sum/num_students
#     return(math_avg,science_avg,eng_avg)
# list_=[("Diya",99,98,92),("Khyati",100,100,100),("Namish",100,99,98)]
# average=calculate_average_scores(list_)
# print(average)

###deep copy vs shallow copy imp concept:
##!!!!!!! for copy and deep copy iterable should be mutable,.....
##copy() method:
##1 D list then id diff and deep copy
# l1=[1,2,3]
# l2=[]
# l2=l1.copy()
# print(id(l1))
# print(id(l2))
# l1[0]=3
# print(l1)
# print(l2)

##2D list: 2D list will have different id
# l1=[id(l1[0]),id(l1[1])]    l2=[id(l1[0]),id(l1[1])]
#l1 and l2 have different ids so when we change any of there elemt directly change done in one is not reflected in other.
#but id of element of elemnt is same so change done in it is reflected in all
# l1=[[1,2,3],[4,5,6]]
# l2=[]
# l2=l1.copy()
# #l1 and l2 have different ids
# print(id(l1))
# print(id(l2))
# #element of element have same ids
# print(id(l1[0]))
# print(id(l1[1]))
# print(id(l2[0]))
# print(id(l2[1]))
# l1[1][1]=10
# #so chande done in element of element is reflected in both
# print(l1)
# print(l2)
# l1[0]=2
# #but change done in element is not reflected in both
# print(id(l1[0]))
# print(id(l1[1]))
# print(id(l2[0]))
# print(id(l2[1]))
# print(l1)#second change is reflected.
# print(l2)
# l1.append([99,98])
# #change reflected in l1 as li and l2 have different ids only elemnt of element had same ids
# print(l1)
# print(l2)
# #same id will come.
# print(id(l1[1]))
# print(id(l2[1]))

##copy.copy():
# import copy
# l1=[[1,2,3],[4,5,6]]
# l2=[]
# l2=copy.copy(l1)
# #l1 and l2 have different ids
# print(id(l1))
# print(id(l2))
# #element of element have same ids
# print(id(l1[0]))
# print(id(l1[1]))
# print(id(l2[0]))
# print(id(l2[1]))
# l1[1][1]=10
# #so chande done in element of element is reflected in both
# print(l1)
# print(l2)
# l1[0]=2
# #but change done in element is not reflected in both
# print(id(l1[0]))
# print(id(l1[1]))
# print(id(l2[0]))
# print(id(l2[1]))
# print(l1)#second change is reflected.
# print(l2)
# l1.append([99,98])
# #change reflected in l1 as li and l2 have different ids only elemnt of element had same ids
# print(l1)
# print(l2)
# #same id will come.
# print(id(l1[1]))
# print(id(l2[1]))

##conclusion--.list2=list1.copy()==import copy and l2=copy.copy(l1)

##copy.deepcopy():change done of any type in one of list is never reflected in other
# import copy
# l1=[[1,2,3],[4,5,6]]
# l2=[]
# l2=copy.deepcopy(l1)
# #l1 and l2 have different ids
# print(id(l1))
# print(id(l2))
# #element of element have different ids
# print(id(l1[0]))
# print(id(l1[1]))
# print(id(l2[0]))
# print(id(l2[1]))
# l1[1][1]=10
# # #so chande done in element of element is reflected in only one
# print(l1)
# print(l2)
# l1[0]=2
# #  change done in element is not reflected in both
# print(l1)
# print(l2)
# print(id(l1[0]))
# print(id(l1[1]))
# print(id(l2[0]))
# print(id(l2[1]))
# l1.append([99,98])
# # #change reflected in l1 as li and l2 have different ids only elemnt of element had same ids
# print(l1)
# print(l2)
# # #diff id will come.
# print(id(l1[1]))
# print(id(l2[1]))

##file permissions: way to control who can read(r), write(w) or execute(x). 
# 3 sets of permissions for 3 sets of people:owner,group,others
#rw-r--r--:owner can read and write while gp and others can only read

##file locks:mechanisms used to prevent concurrent accesss(multiple processes/threads attempting to acccess and modify same resource such as file at a same time) to file by multiple processes / threads
##locks are managed by operating system and are typically used in environment where strict contro over file access is necessary.
##there are 2 types of locks: 
##advisory locks: other processes can still access file without being blocked
##mandatory locks: prevent any access to file that conflicts with lock

##!!!!!!not aliasing
# x=[1,2,3]
# y=x[:]
# print(id(x))
# print(id(y))
# y.append(4)
# print(x)
# print(y)

##recursion is generally less memory intensive than iteration

##quiz 3:
###concatenation of dictionary:
dict1={'a':1,'b':2}
dict2={'c':3,'d':4}
# dict1.update(dict2)
# print(dict1)

##using (**)-->syntax
# concatenated_dict={**dict1,**dict2}
# print(concatenated_dict)

# concatenated_dict=dict(dict1,**dict2)
# print(concatenated_dict)

# concatenated_dict=dict1.copy()
##if particular key is not present then it is concatenated in dictionary
# concatenated_dict={}
# for key,value in dict2.items():
#     concatenated_dict[key]=value####important
# print(concatenated_dict)

###swaping of key and value:
# dict3={value:key for key,value in dict1.items()}
# print(dict3)

##hexadecimal format opertor: %x

##try always requires atleast one except
# def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k= foo()
# print(k)

# try: 
#     raise Exception("An Error Occured")
# except ValueError:
#     print("ValueError")
# except Exception as e:
#     print(e)

##Lookup Error:
# exception when key is not found in dictionary or when accessing an item in seq using index i.e. out of the range

# with open('python_code/file2.txt','r') as file:
#     content=file.read()
# formatted_content="{:.2f}".format(content)
# print(formatted_content)

# x=int("20")
# x=float("20")
# y=float("ab") ##ValueError
# print(y)
# z=int("abo")##ValueERror
# print(z)
# print(x)

##input should be iterable for typecasting for all the cases
# x=5
# y=set(x)
# y=tuple(x)
# y=list(x)
# y=dict(x)
# print(y)

# s3=set()
# print(s3)

##important
# set1={}
# print(type(set1))###dictionary

##set considers True and 1 as same and False and 0 as same
# s1={"d","l","True",1,True}
# s2={"d","l","False",0,False,True}
# print(s1)
# print(s2)

##add method :adds a given element to a set if the element is not present in the set
# GEEK = set()
# GEEK.add('s')
# print("Letters are:", GEEK)
# GEEK.add('e')
# print("Letters are:", GEEK)
# GEEK.add('s')
# print("Letters are:", GEEK)

# GEEK = {'g', 'e', 'k'}
# GEEK.add('s')
# print("Letters are:", GEEK)
# GEEK.add('s')
# print("Letters are:", GEEK)

# GEEK = {6, 0, 4}
# GEEK.add(1)
# print('Letters are:', GEEK)
# GEEK.add(0)
# print('Letters are:', GEEK)

# Python code to demonstrate addition of tuple to a set.
# s = {'g', 'e', 'e', 'k', 's'}
# t = ('f', 'o')
# l = ['a', 'e']
# s.add(t)
# # s.add(l) cannot add list to set using add method we require update method
# s.update(l)
# print(s)

###frozenset method():frozenset in python are immutable objects only support methods and opeartors that donot affect frozen set
# normal_set = set(["a", "b","c"])
# print("Normal Set")
# print(normal_set)
# # A frozen set
# frozen_set = frozenset(["e", "f", "g"])
# print("\nFrozen Set")
# print(frozen_set)
# frozen_set.add(9)###AttributeError

###internal working of set:'
#based on data structure Hashtable.
#if multiple values are present at same index position, then value is appended to that index position forming linkedlist
#sets are implemented using dictionary with dummy variables

##remove is used to remove a single element from set:
# set1={1,2,3}
# set1.remove(2)
# set1.remove(1,3)##typeerror
# set1.remove()#typeerror
# print(set1)#typeerror

# people = {"Jay", "Idrish", "Archi"}
# print("People:", end = " ")
# print(people)
# people.add("Daxit")
# for i in range(1, 6):
#     people.add(i)
# print("\nSet after adding element:", end = " ")
# print(people)

##union--> |
# people = {"Jay", "Idrish", "Archil"}
# vampires = {"Karan", "Arjun"}
# dracula = {"Deepanshu", "Raju"}
# population = people.union(vampires)
# print(population)
#  ##!!very important
# # Union using "|" operator
# population = people|dracula
# print("\nUnion using '|' operator")
# print(population)

#intersection &
# set1 = set()
# set2 = set()
# for i in range(5):
#     set1.add(i)
# for i in range(3,9):
#     set2.add(i)
# set3 = set1.intersection(set2)
# print(set3)
# # "&" operator
# set3 = set1 & set2
# print("\nIntersection using '&' operator")
# print(set3)

##differences of 2 sets:
# set1 = set()
# set2 = set()
# for i in range(5):
#     set1.add(i)#{0,1,2,3,4}
# for i in range(3,9):
#     set2.add(i)#{3,4,5,6,7,8}
# set3 = set1.difference(set2)#{0,1,2}
# print(set3)
# # using '-' operator
# set3 = set1 - set2
# print("\nDifference of two sets using '-' operator")
# print(set3)

#symmetric difference of 2 sets:
# set1 = set()
# set2 = set()
# for i in range(5):
#     set1.add(i)#{0,1,2,3,4}
# for i in range(3,9):
#     set2.add(i)#{3,4,5,6,7,8}
# set3 = set1.symmetric_difference(set2)#{0,1,2}
# print(set3)
# # using '^' operator
# set3 = set1 ^ set2
# print("\nDifference of two sets using '-' operator")
# print(set3)
# set1 = {1,2,3,4,5,6}
# set1.clear()
# print("\nSet after using clear() function")
# print(set1)

# list1=[1,2,3]
# list2=[1,2,3]
# print(list1 is list2)
# print(list1==list2)

# set1={1,2}
# set2={1,2}
# print(set1 is set2)
# print(set1==set2)

# set1={1,2,3}
# set2={1,2}
# print(set1>=set2)

###symmetric difference: ^
#elements in both the sets except common elements
# set1={1,2,3}
# set2={1,2}
# print(set1^set2)

##string formatting:
# print("The mangy, scrawny stray dog %s gobbled down" %'hurriedly ' 
	# "the grain-free, organic dog food.")

# %5.4f format specifier is used to format a floating-point number with a minimum width of 5 and a precision of 4 decimal places.

# print('The value of pi is: %5.4f' %(3.141592))

# print('{2} {1} {0}'.format('directions','the', 'Read'))
# print('a: {a}, b: {b}, c: {c}'.format(a = 1,b = 'Two',c = 12.3))

# Syntax: {[index]:[width][.precision][type]}-->.format()
# print('The valueof pi is: %1.5f' %3.141592)
# print('The valueof pi is: %0.5f' %3.141592)
# print('The valueof pi is: {0:1.5f}'.format(3.141592))

# txt = "I have {an:.2f} Rupees!"
# print(txt.format(an = 4))

# parameters in format function.
# my_string = "{}, is a {} {} science portal for {}"
# print(my_string.format("GeeksforGeeks", "computer", "geeks"))

# +20-->right aligned
# -20-->left aligned
# width.noofcharacters
# print("%6.5s" % ('geeksforgeeks', ))
# print("%-20s" % ('Interngeeks', ))
# print("%.5s" % ('Interngeeks', ))

# ##%i and %d are for signed int
# match = 12000
# site = 'Amazon'
# print("%s is so useful. I tried to look\up mobile and they had a nice one that cost %i rupees." % (site, match))

# print("This site is {0:f} securely {1}!!".format(100, "encrypted"))
# print("My average of this {0} was {1:.2f}%".format("semester", 78.234876))
# print("My average of this {0} was {1:.0f}%".format("semester", 78.234876))
# print("The {0} of 100 is {1:b}".format("binary", 100))
# print("The {0} of 100 is {1:o}".format("octal", 100))


# When explicitly converted floating-point
# values to decimal with base-10 by 'd'
# type conversion we encounter Value-Error.
# print("The temperature today is {0:d} degrees outside !".format(35.567))
# Instead write this to avoid value-errors
# ''' print("The temperature today is {0:.0f} degrees outside !".format(35.567))'''

##!!important!!!
# print("my score is {0:d}".format(23.4))###valueerror

# Syntax: {value:{width}.{precision}}
# num = 3.14159
# print(f"The value of pi is: {num:{1}.{5}}")

##string template class
# from string import Template
# n1 = 'Hello'
# n2 = 'GeeksforGeeks'
# n = Template('$n3 ! This is $n4.')
# print(n.substitute(n3=n1, n4=n2))
# print(n.template)

# center() method :
# The center() method is a built-in method in Python’s str class that returns a new string
#  that is centered within a string of a specified width. 
# string = "GeeksForGeeks!"
# width = 30
# centered_string = string.center(width)
# print(centered_string)

# s1={1,True}
# s2={True,1}
# print(s1)
# print(s2)