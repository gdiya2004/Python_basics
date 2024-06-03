#1
# f=open("example.txt","w")
# f.write("Hello, World!")
# f.close()

#2
# f=open("python_code/data.txt","r")
# # data1=f.read()
# # data2=f.readline()
# data3=f.readlines() #returns list of lines
# # print(data1)
# # print(data2)
# print(data3)
# f.close()

#3
# f=open("output.txt","w")
# f.write("[1,2,3,4,5]")
# f.close()
          ###or
# with open("output.txt","w") as f:
#     f.write("[1,2,3]")

#4
# f=open("python_code/log.txt","a")
# f.write(" is a very good boy.")
# f.close()

#5
# f=open("python_code/log.txt","r")
# data=f.read()
# print(data)
# f.close()

#6
# f=open("python_code/data.txt","rb")
# yes=f.read()
# print(yes)
# f.close()

#7
# name="Diya"
# Roll_no=32
# print("I am %s and Roll no. is %d"%(name,Roll_no))
#8.
# name="Diya"
# print(f"I am {name}")

def pallindrome(string):
    if string[:]==string[::-1]:
        return string
    n=len(string)
    i=0
    pallin=[]
    if string[i]==string[n-i-1]:
        i+=1
        pallin.append(string[i])
        continue
    else:
string=input("Write a string:")
output=pallindrome(string)
print(output)
