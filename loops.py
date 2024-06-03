# x=int(input("Enter the value of x="))
# match x:
#     case 0:
#         print("x is zero")
#     case 4:
#         print("x is 4")
#     case _:
#         print(x)
# x=5
# while (x>0):
#     print(x)
#     x=x-1
# else:
#     print("count is 0")
# for i in range(1,101,1):
#     print(i,end=" ")
#     if(i==50):
#         break
#     else:
#         print("diya")
# print("great")
# for int in range(1500,2701):
#     if int%7==0 and int%5==0:
#         print(int)
# m=int(input("Enter no. of rows:"))
# n=int(input("Enter no. of columnns:"))
# for i in range(m):
#     for j in range(n):
#         print(i*j,end=" ")
#     print("\n")
# intg=int(input("Enter any number:"))
# for i in range(1,11):
#     print(intg,"*",i,"=",intg*i)
# l1 = list()
# ele = int(input("Enter no. of elements="))
# for i in range(ele):
#     temp = int(input("Enter the input="))
#     l1.append(temp)
# print(l1)
# for i in range(0,(len(l1)-1)):
#     for j in range(0,(len(l1)-1-i)):
#         if l1[j]>l1[j+1]:
#             temp2=l1[j]
#             l1[j]=l1[j+1]
#             l1[j+1]=temp2
# print(l1)
# def bintodecconvertor(num):
#     temp2=num
#     result=0
#     i=0
#     while temp2!=0:
#         result=result+(temp2%10)*(2**i)
#         temp2=temp2//10
#         i=i+1
#     return result
# li=list()
# length=int(input("enter the no. of binary values u need to compare:"))
# for i in range(length):
#     bin=input("Enter 4 digit binary number=")
#     li.append(bin)
# print(li)
# l2=list()
# for i in range(len(li)):
#     temp1=li[i]
#     bindec= bintodecconvertor(int(temp1))
#     if bindec%5==0:
#         l2.append(temp1)
# print("no. divisible by 5=",l2)
# m=7
# for i in range(1,m):
#     for j in range(1,i):
#         print(j,end=" ")
#     print("\n")
# r=7
# for i in range(1,r):
#     for j in range (i,r):
#         print(" ",end=' ')
#     for k in range (1,i):
#         print(" * ",end=" ")
#     print("\n")
# a=input("Enter your name=")
# print(input("Enter your name="))
# input("Enter ur name=")
# list=[1,2,3,4]
# print(list[-2])
# print(list[1:3])

