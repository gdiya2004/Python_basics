# ##to print fibonacci nth number
# def fibonacci(n):
#     fib0=0
#     fib1=1
#     for i in range(1,n-1):
#         temp=fib0
#         fib0=fib1
#         fib1=temp+fib0
#     print(fib1)
#     return
# n=int(input("Enter the no.="))
# fibonacci(n)

# #print fibonacci series containing n values
# def fibonacci(n):
#     fib0=0
#     fib1=1
#     print(fib0 , fib1,end=" ")
#     for i in range(n-2):
#         temp=fib0
#         fib0=fib1
#         fib1=temp+fib0
#         print(fib1,end=" ")
#     print(fib1)
#     return
# n=int(input("Enter the no.="))
# fibonacci(n)

##using recursion print nth fibonacci number
# def fibo(n):
#     if n<=1:
#         return n
#     else:
#         f=fibo(n-1)+fibo(n-2)
#         return f
# x=int(input("Enter the number="))
# y=fibo(x)
# print(y)

# ##using recursion print fibonacci series
# def fibo(n):
#     if n<=1:
#         return n
#     else:
#         f=fibo(n-1)+fibo(n-2)
#         return f
# def print_fibo_series(count):
#     for i in range(count):
#         print(fibo(i))
# x=int(input("Enter the number="))
# y=print_fibo_series(x)


# def TOH(numbers,start,aux,end):
#     if numbers==1:
#         print("Move disc 1 from rod {} to rod {}".format(start,end))
#         return
#     TOH(numbers-1,start,end,aux)
#     print("Move disc {} from rod {} to rod {}".format(numbers,start,end))
#     TOH(numbers-1,aux,start,end)
# n=int(input("Enter no. of discs="))
# disc=TOH(n,"A","B","C")

###GCD or HCF:
# def gcd(a,b):
#     while b!=0:
#         a,b=b,a%b 
#     return a 
# num1=8
# num2=24
# f=gcd(num1,num2)
# print(f)

# def fun(n): 
#     if (n > 0):  
#         print(n, end=" ")  #3 2 1
#         fun(n - 1)  #2 1 0
#         fun(n - 1)  
# fun(3)

# Python program to show Nested Recursion 
# def fun(n): 
# 	if (n > 100): 
# 		return n - 10
# 	return fun(fun(n + 11)) #fun(fun(106))-->fun(96)-->fun(fun(107))
# r = fun(95) 
# print("", r) 

# def fibonacci_tail(n, a=0, b=1):
#     if n == 1:
#         return a
#     else:
#         return fibonacci_tail(n-1, b, a+b)
# x=fibonacci_tail(5)
# print(x)
# This code is contributed by shivanisinghss2110


# importing pdb 
import pdb 
# simple function 
def fxn(n): 
    l = [] 
    for i in range(n): 
        l.append(i) 
    return
# set trace 
pdb.set_trace() 
fxn(5) 

# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)
# num1 = 48
# num2 = 18
# print("GCD of", num1, "and", num2, "is:", gcd(num1, num2))

# n1=int(input("enter no.="))
# n2=int(input("enter no.="))
# gcd=0
# for i in range(1,n1+1):
#     if(n1%i==0 and n2%i==0):
#         gcd=i
# print(gcd)

##linear search using iteration
# def search(t,*num):
#     flag=True
#     for i in range(len(num)):
#         if i==t:
#             flag=True
#         else:
#             flag=False
#     return flag

# n=int(input("Enter the target value="))
# numbers=[1,3,5,7,2,9,5]
# exist=search(n,numbers)
# print(exist)

##linear search using recursion
# def linear_search_recurs(arr,target,index=0):
#     if index==len(arr):
#         return -1
#     elif arr[index]==target:
#         return index
#     else:
#         return linera_search_recurs(arr,target,index+1)

##binary search using recusion
# def binary(arr,target,low,high):
#     if low<=high:
#         mid=(low+high)//2
#         if arr[mid]==target:
#             return mid
#         elif arr[mid]<target:
#             return binary(arr,target,mid+1,high)
#         else:
#             return binary(arr,target,low,mid-1)
#     else:
#         return -1

##bubble sort
# def bubble(arr,n):
#     if n==1:
#         return arr
#     for i in range(n-1):
#         if arr[i]>arr[i+1]:
#             arr[i],arr[i+1]=arr[i+1],arr[i]
#     return bubble(arr,n-1)
# list=[9,5,7,3]
# sort=bubble(list,4)
# print(sort)

# for i in range(len(arr)):
#     swap=False
#     for j in range(len(arr)-i-1):
#         if arr[i]>arr[i+1]:
#             arr[i],arr[i+1]=arr[i+1],arr[i]
#             swap=True
#         if swap==False:
#             break

#selection sort
# def selection_sort(arr):
#     if len(arr)<=1:
#         return arr
#     min_index=arr.index(min(arr))
#     arr[0],arr[min_index]=arr[min_index],arr[0]
#     return [arr[0]]+selection_sort(arr[1:])
# list=[3,7,9,2]
# sort=selection_sort(list)
# print(sort)

# arr=[3,7,9,2]
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         min_index=arr.index(min(arr[i:]))
#         arr[i],arr[min_index]=arr[min_index],arr[i]
# print(arr)


##insertion sort
# def insertion_sort(arr,n):
#     if n<=1:
#         return arr
#     insertion_sort(arr,n-1)
#     last=arr[n-1]
#     j=n-2
#     while j>=0 and arr[j]>last:
#         arr[j+1]=arr[j]
#         j=j-1
#     arr[j+1]=last
#     return arr
# list=[10,9,5,3]
# sort=insertion_sort(list,4)
# print(sort)

#insertion
# for i in a:
#     j=a.index(i)
#     while j>0:
#         if a[j-1]>a[j]:
#             a[j-1],a[j]=a[j],a[j-1]
#         else:
#             break
#         j=j-1

##list can be added
# list1=[2,3]
# list2=[4,5]
# print(list1+list2)

#merge sort:
# def merge(a,b):
#     c = []
#     while len(a)!=0 and len(b)!=0 :
#         if a[0] < b[0]:
#             c.append(a[0])
#             a.remove(a[0])
#         else:
#             c.append(b[0])
#             b.remove(b[0])
#     if len(a) == 0:
#         c=c+b
#     else:
#         c=c+a
#     return c
# def divide(x):
#     if len(x) == 0 or len(x) == 1:
#         return x
#     else:
#         middle = len(x)//2
#         a = divide(x[:middle])
#         b = divide(x[middle:])
#         return merge(a,b)

# x=[38,27,43,3,9,82,10]
# c=divide(x)
# print(c)

# def histogram(a):
#     for i in a:#4
#         sum = ''
#         while(i>0):
#             sum=sum+'#'
#             i=i-1
#         print(sum)
# a=[4,5,7,8,12]
# histogram(a)

##tuples can be added too
# tup1=(1,2)
# tup2=(3,4)
# print(tup1+tup2)

##set cannot be added
# set1={1,2}
# set2={3,4}
# print(set1+set2)

##recursive function to find sum of elements of list
# def list_sum(lst):
#     if not lst:
#         return 0
#     else:
#         return lst[0]+list_sum(lst[1:])
# list=[1,2,3,4,5]
# sum=list_sum(list)
# print(sum)

##
# import math
# def area(radii):
#     return 3.14*radii*radii
# def radius(xc,yc,x1,y1):
#     rad=math.sqrt((xc-x1)*(xc-x1)+(yc-y1)*(yc-y1))
#     return area(rad)
# xc=int(input("Enter the X-coordinate of center:"))
# yc=int(input("Enter the Y-coordinate of center:"))
# x1=int(input("Enter the X-coordinate :"))
# y1=int(input("Enter the Y-coordinate :"))
# are_circle=radius(xc,yc,x1,y1)
# print(are_circle)

# def permutations(lst):
#     if len(lst) == 0:
#         return [[]]
#     perms = []
#     for i in range(len(lst)):
#         current = lst[i]
#         remaining = lst[:i] + lst[i+1:]
#         for perm in permutations(remaining):
#             perms.append([current] + perm)
#     return perms
# my_list = [1, 2, 3]
# print(permutations(my_list))

##2445
# def split_dict_of_lists_to_list_of_dicts(dict_of_lists):
#     # Get keys and values from the dictionary
#     keys = list(dict_of_lists.keys())
#     values = list(dict_of_lists.values())
    
#     # Get the length of the lists (assuming all lists have the same length)
#     length = len(values[0])
    
#     # Create a list of dictionaries
#     list_of_dicts = [{keys[i]: values[i][j] for i in range(len(keys))} for j in range(length)]
    
#     return list_of_dicts

# # Example usage
# dict_of_lists = {
#     'a': [1, 2, 3],
#     'b': ['x', 'y', 'z'],
#     'c': ['apple', 'banana', 'orange']
# }

# list_of_dicts = split_dict_of_lists_to_list_of_dicts(dict_of_lists)
# print(list_of_dicts)


# def mul_list(l):
#     for i in range(len(l)):
#         l=l.append(l[i]*2)
#     return l
# list_=[1,2,3]
# print(f"Id before={id(list_)}")
# x=mul_list(list_)
# print(x)
# print(f"Id after={id(list_)}")

##very imporatnat making Sum and n global variable.
# Sum=0
# n=int(input("Enter the number:"))
# def do_sum():
#     Sum=sum(range(1,n+1))
#     return Sum
# print("Sum is=",do_sum())

# def outer_fun(numb):
#     def reverse():
#         nonlocal n
#         rev=0
#         while n>0:
#             rev=rev*10+n%10
#             n=n//10
#     reverse()
# n=int(input("Enter the number="))
# num=outer_fun(n)
# ###OR
# n=int(input("Enter the number="))
# def outer_fun():
#     def reverse():
#         rev=0
#         while n>0:
#             rev=rev*10+n%10
#             n=n//10
#     reverse()
# print("reverse is=",outer_fun())

# midsem 
# class StudentRecord:
#     def __init__(self):
#         self.records = {}
#     def register_student(self):
#         while True:
#             student_id = input("Enter student id: ")
#             name = input("Enter student name: ")
#             marks_input = input("Enter PCM marks separated by commas (e.g., 88,78,90): ")
#             marks = [int(x) for x in marks_input.split(",")]
#             self.records[student_id] = {'name': name, 'marks': marks}
#             choice = input("Do you want to continue? (Y/N): ")
#             if choice.upper() != 'Y':
#                 break
#     def fxn_result(self):
#         def public_percentage(marks):
#             total_marks=sum(marks)
#             percentage = (total_marks / (len(marks) * 100)) * 100
#             private_distinction(percentage)
#             return percentage

#         def private_distinction(percentage):
#             if percentage > 70:
#                 return "Yes"
#             else:
#                 return "No"
#         result_copy = {}
#         for student_id, info in self.records.items():
#             name = info['name']
#             marks = info['marks']
#             percentage = public_percentage(marks)
#             distinction = private_distinction(percentage)
#             result_copy[student_id] = {'name': name, 'percentage': percentage, 'distinction': distinction}
#         return result_copy
# def main():
#     record_system = StudentRecord()
#     record_system.register_student()
#     result = record_system.fxn_result()
#     print("\nResult Copy:")
#     print("Student ID\tName\tPercentage\tDistinction")
#     for student_id, info in result.items():
#         print(f"{student_id}\t\t{info['name']}\t{info['percentage']:.2f}%\t\t{info['distinction']}")


# if __name__ == "__main__":
#     main()

##output1:
# x=3
# if x>2 or x<5 and x==6:#1 or 0
#     print("ok")
# else:
#     print("no")

##2:
# a=True 
# b=False 
# c=True 
# if not a or b: #falsae or false
#     print("a")
# elif not a or not b and c:# false or true
#     print("b")
# elif not a or b or not b and a:
#     print("c")
# else:
#     print("d")

##3:
# String="My Computer Course"
# print(len(String))
# x1=slice(-1,-9)#(17,9)
# # x2=slice(9)#(0,9)
# print(String[x1])#e
# # print(String[x2[1,3]])

##4:
# x=0
# a=5
# b=5
# if a>0:
#     if b<0:
#         x=x+5
#     elif a>5:
#         x=x+4
#     else:
#         x=x+3#x=3
# else:
#     x=x+2
# print(x)

##5:
# n=7
# c=0
# while(n):
#     if n>5:#7,6
#         c=c+n-1#c=6,11
#         n=n-1#n=6,5
#     else:
#         break
#     print(n)
#     print(c)

##6:
# list1=[3,2,5,6,0,7,9]
# sum=0
# sum1=0
# for elem in list1:
#     if elem%2==0:
#         sum=sum+elem#2+6+0
#         continue
#     if elem%3==0:
#         sum1=sum1+elem#3+9
# print(sum)
# print(sum1)

# import array
# lst=[1,2,3,4,5,6]
# array.array("i",lst)
