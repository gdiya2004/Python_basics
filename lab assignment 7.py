#q1 1
# def add(a,b,c,x,y,z):
#     sum=a+b+c+x+y+z
#     return sum
# s=add(1,2,3,4,5,6)
# print("The sum is=",s)

# def add(a,b,c,/,x,y,z):
#     sum=a+b+c+x+y+z
#     return sum
# s=add(1,2,3,y=4,x=5,z=6)
# print("The sum is=",s)

# def add(a,b,c,x,y,z):
#     sum=a+b+c+x+y+z
#     return sum
# s=add(b=1,c=2,a=3,y=4,x=5,z=6)
# print("The sum is=",s)

## important thing to remember default value is decided after non default value
# def is_factor(n,f=1):
#     if n%f==0:
#         print(f"{f} is factor of {n}")
#     else:
#         print(f"{f} is not factor of {n}")
#     return
# x=int(input("Enter any number="))
# y=int(input("Enter any number which is to be checked as factor= "))
# is_factor(x,y)

#q2 b
# def slope(x1,y1,x2,y2):
#     slope=(y2-y1)/(x2-x1)
#     return slope
# x1=int(input("Enter the first x-coordinate:"))
# y1=int(input("enter the first y-coordinate:"))
# x2=int(input("Enter the second x-coordinate:"))
# y2=int(input("enter the second y-coordinate:"))
# s=slope(x1,y1,x2,y2)
# print("Tne slope formed by given points is=",s)

#q2 e
# Create a recursive function to calculate the factorial of a number.
# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)
# x=int(input("Enter any number="))
# fact=fact(x)
# print("Factorial of given number is=",fact)

#q2 d Create an inner function that calculates the sum of arbitrary number of arguments. Pass
# arbitrary arguments to the outer function.
# def outer_fun(*num):
#     s=0
#     def inner_fun(number):
#         nonlocal s
#         s=s+number
#         return s
#     for i in range(0,len(num)):
#         s=inner_fun(num[i])
#     return s
# numbers=[1,2,3,4,5,6]
# summ=outer_fun(*numbers)
# print(summ)

# Create a function in Python that takes string as an input and returns true if the entered
# string is a palindrome.
# method 1
# def string_input(string):
#     flag=True
#     for i in range(0,len(string)):
#         if string[i]==string[-(i+1)]:
#             flag=True
#             continue
#         else:
#             # flag=False
#             break
#     return flag
# string=input("Enter any string:")
# x=string_input(string)
# print(x)

#method 2
# def string_input(string):
#     if string[::-1]==string:
#         print("It is pallindrome.")
#     else:
#         print("It is not a pallindrome.")

# string=input("Enter any string:")
# x=string_input(string)





