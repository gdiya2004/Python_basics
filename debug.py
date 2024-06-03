# import pdb
# a=10
# bin=20
# breakpoint()
# c=0
# breakpoint()
# c=a*bin
# print("multiplication is:")
# breakpoint()
# print(c)

# import pdb
# for i in range(10):
#     breakpoint()
#     if i%2==0:
#         print(f"{i} is even number")
#     else:
#         print(f"{i} is odd number")

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
# import pdb
# def find_grade(marks):
#     pdb.set_trace()  
#     if marks >= 90:
#         grade = 'S'
#     elif 80 <= marks < 90:
#         grade = 'A'
#     elif 70 <= marks < 80:
#         grade = 'B'
#     elif 60 <= marks < 70:
#         grade = 'C'
#     elif 50 <= marks < 60:
#         grade = 'D'
#     else:
#         grade = 'F'
#     return grade
# marks = float(input("Enter the marks: "))
# grade = find_grade(marks)
# print("Grade:", grade)

# import pdb
# a=input("Enter the first number=")
# breakpoint()
# b=input("Enter the second number=")
# temp=a
# a=b
# b=temp
# print(f"After swapping first number={a} and second number={b}")

# a=int(input("Enter the first number="))
# b=int(input("Enter the seconfd number="))
# breakpoint()
# a=a+b
# b=a-b
# a=a-b
# print(f"After swapping 1st no.={a} and 2nd no.={b}")

# import pdb
# def addition(a,b):
#    answer=a+b
#    return answer
# pdb.set_trace()
# x=input("first number=")
# y=input("Second number=")
# sum=addition(x,y)
# print(sum)

###whatis command used to check data type of variable
# a=20
# pdb.set_trace()
# b=10
# s=0
# for i in range(a):
#     s+=a/b
#     b-=1