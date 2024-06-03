# #time stamp
# import time
# t = time.strftime('%H:%M:%S')
# print(t)
# hour = int(time.strftime('%H'))
# print(hour)
# hour=int(input("Enter Hour="))
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
# # https://docs.python.org/3/library/time.html#time.strftime
# if hour>=8 and hour<12:
#     print("Good Morning")
# elif hour>=12 and hour<=17:
#     print("Good Afternoon")
# else:
#     print("Good Night")

##Kaun Banega Crorepati
# questions=[["Who is prime minister of india?","Diya","Khyati","Namish","Narendra Modi",4],
# ["Who is president of india?","Diya","Khyati","Namish","Draupadi Murmu",4],
# ["How many states in india?",28,10,29,25,1],
# ["How many UT in india?",8,9,10,7,1],
# ["Who is prime minister of india?","Diya","Khyati","Namish","Narendra Modi",4],
# ["Who is president of india?","Diya","Khyati","Namish","Draupadi Murmu",4],
# ["How many states in india?",28,10,29,25,1],
# ["How many UT in india?",8,9,10,7,1],
# ["How many states in india?",28,10,29,25,1],
# ["How many UT in india?",8,9,10,7,1]]
# levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
# money=0
# for i in range(0,len(questions)):
#     question=questions[i]
#     print(f"{question[0]} for {levels[i]}")
#     print(f"1.{question[1]}    2.{question[2]}   3.{question[3]}   4.{question[4]}")
#     answer=int(input("Enter the Answer(1-4) or Enter 0 to quit:"))
#     if answer==0:
#         print("Quit Game")
#         money=levels[i-1]
#         break
#     if answer==question[5]:
#         print(f"Correct and You earned {levels[i]}")
#         if i==4:
#           money=10000
#         if i==9:
#           money=320000 
#     else:
#         print("Incorrect Answer.")
#         break
# print(f"Total Prize money won is={money}")


##Snake water gun game:
# import random
# usercount=0
# compcount=0
# while True:
#  computer=random.randint(0,2)
#  user=int(input("Enter 0 for Snake, 1 for water and 2 for gun "))
#  comp=print(f"Number choosed by computer={computer}")  
#  if computer==user:
#     cb=input("Do u want to continue Y/N?")
#     if cb=='Y':
#         continue
#     else:
#         break
#  elif computer==0 and user==1:
#     compcount+=1
#     cb=input("Do u want to continue Y/N?")
#     if cb=='Y':
#         continue
#     else:
#         break
#  elif computer==0 and user==2:
#     usercount+=1
#     cb=input("Do u want to continue Y/N?")
#     if cb=='Y':
#         continue
#     else:
#         break
#  elif computer==1 and user==2:
#     compcount+=1
#     cb=input("Do u want to continue Y/N?")
#     if cb=='Y':
#         continue
#     else:
#         break
#  elif user==0 and computer==1:
#     usercount+=1
#     cb=input("Do u want to continue Y/N?")
#     if cb=='Y':
#         continue
#     else:
#         break
#  elif user==0 and computer==2:
#     compcount+=1
#     cb=input("Do u want to continue Y/N?")
#     if cb=='Y':
#         continue
#     else:
#         break
#  elif user==1 and computer==2:
#     usercount+=1
#     cb=input("Do u want to continue Y/N?")
#     if cb=='Y':
#         continue
#     else:
#         break
# print(f"User score={usercount}")
# print(f"Computer score={compcount}")
# if usercount>compcount:
#     print("User is the winner")
# elif usercount<compcount:
#     print("Computer is the winner")
# else:
#     print("Draw")


# import random
# usercount=0
# compcount=0
# def check(computer,user):
#     if computer==user:
#         return 0
#     elif computer==0 and user==1:
#         return -1
#     elif computer==2 and user==0:
#         return -1
#     elif computer==1 and user==2:
#         return -1
#     else:
#         return 1
# computer=random.randint(0,2)
# user=int(input("Enter 0 for Snake, 1 for water and 2 for gun "))
# comp=print(f"Number choosed by computer={computer}")
# print(f"you:{user}")
# print(f"computer={computer}")
# value=check(computer,user)
# if value==0:
#     pass
# elif value==1:
#     usercount+=1
# else:
#     compcount+=1

###Library Management System
# class Library:
#     def __init__(self):
#         self.no_of_books=0
#         self.books=[]
#     def addBook(self,book):
#         self.books.append(book)
#         self.no_of_books=len(self.books)
#     def showInfo(self):
#         print(f"The library has {self.no_of_books} books\n Books are:")
#         for book in self.books:
#             print(book)
# l1=Library()
# l1.addBook("Harry Potter1")
# l1.addBook("Harry Potter2")
# l1.addBook("Harry Potter3")
# l1.addBook("Harry Potter4")
# l1.showInfo()

##datetime() module :
# import datetime
# print(datetime.datetime()) ##gives error
# today=datetime.datetime.today() ##date
# print(f"{today:%B %d %Y}")
# current_time=datetime.datetime.now() ##date+time
# print("The attributes of now() are:")
# print("Complete:",current_time)
# print("year:",current_time.year)
# print("month:",current_time.month)
# print("day:",current_time.day)
# print("hour:",current_time.hour)
# print("minutes:",current_time.minute)
# print("seconds:",current_time.second)
# # print("microsecond:",current_time.microsecond)
# print(today)
# print(today.year)
##time module():
# import time
## time.time(): returns time in seconds
# def usingWhile():
#     i=0
#     while i<5000:
#         i+=1
#         print(i)
# def usingFor():
#     for i in range(5000):
#         i+=1
#         print(i)
# init1=time.time() ##prints time in second
# usingFor()
# t1=time.time()-init1
# init2=time.time()
# usingWhile()
# t2=time.time()-init2
# print(f"Time by for loop:{t1}") ##time taken keeps on changing
# print(f"Time by while loop:{t2}")

# import time
# print(4)
# time.sleep(3)
# print("This is printed after 3 seconds")

# import time
# ##time.strftime() function formats time value as a string based on specified format
# t1=time.localtime()
# # t2=time.time() ##prints time in seconds
# print(t1)
# # print(t2)
# formatted_time=time.strftime("%Y-%m-%d %H:%M:%S",t1)
# print(formatted_time)

# import time
# t=time.localtime()
# print(t)
# print("Year:",t.tm_year)
# print("Month:",t.tm_mon)
# print("Date:",t.tm_mday)
# print("Hour:",t.tm_hour)
# print("Minute:",t.tm_min)
# print("Second:",t.tm_sec)

###The 'm' in tm_mday stands for "month". However, the naming might be a bit misleading. The "m" actually indicates the day of the month, not the month itself. So, tm_mday is used to represent the day of the month, ranging from 1 to 31.
###The 'y' in tm_yday stands for "year". However, similar to tm_mday, the naming can be somewhat confusing. In this context, 'y' doesn't refer to the year itself but rather to the "day of the year" within that year. It's an integer value ranging from 1 to 366, representing the ordinal day of the year, where January 1st is day 1 and December 31st is day 365 or 366 (in leap years).
##The 'w' in tm_wday stands for "weekday". This attribute indicates the day of the week as an integer, where Monday is 0, Tuesday is 1, and so on, up to Sunday, which is 6.

##Merging the pdf solution.
# from PyPDF2 import PdfWriter
# import os
# merger=PdfWriter()
# files=[file for file in os.listdir() if file.endswith(".pdf")]
# for pdf in files:
#     merger.append(pdf)
# merger.write("merged-pdf.pdf")##gives name of new pdf
# merger.close()

##converting text to voice
# import pyttsx3
# def text_to_speech(text):
#     engine = pyttsx3.init()    # Initialize the text-to-speech engine
#     # Set properties, including voice and rate
#     engine.setProperty('rate', 100)  # Speed of speech
#     engine.setProperty('voice', 'english')  # You can change the voice
#     engine.say(text)# Convert text to speech
#     engine.runAndWait()    # Wait for speech to finish
# text_to_speech("Namish is sweetest brother ever i love him infinity")

##using NewsAPI and the requests module to fetch the daily news related to different topics
# import requests
# import json 
# query=input("What type of news are u interseted in?")
# url=f"https://newsapi.org/v2/everything?q={query}tesla&from=2024-03-03&sortBy=publishedAt&apiKey=5fa7810778b9434989721d39383c0f41"
# r=requests.get(url)
# # print(r.text)
# # print(type(r.text)) ##string
# news=json.loads(r.text) ##to convert json formatted string into python object
# # print(news,type(news))
# for article in news["articles"]:
#     print(article['title'])
#     print(article['description'])
#     print("--------------------------------------------------")

##Json module:
##json-->javascript object notation.. it is common way to represent data in webD
# ##Json is used to encode python objects into JSON strings andvice versa
# ##json.loads()--> used to decode json formatted string into python
# ##json.dumps():--> used to encode Python object into json formatted string
# import json
# data={"name":"John","age":30,"city":"New York"} ##dictionary
# json_string=json.dumps(data)
# print(json_string)
# print(type(json_string)) ##string
# decoded_data=json.loads(json_string)
# print(decoded_data)
# print(type(decoded_data)) ##dictionary

##json not only return python dict but any python object
# import json
##1 dictionay
# json_string_dict='{"name":"Joihn","age":30}'
#                              ##Or
# # json_string="{'name':'Joihn','age':30}"
# decoded_dict=json.loads(json_string_dict)
# print(decoded_dict)
# print(type(decoded_dict))

##2 list
# json_string_list='[1,2,3,4]'
# decoded_list=json.loads(json_string_list)
# print(decoded_list)
# print(type(decoded_list))

##3 string
# json_string_str='"hello World"'
# decoded_str=json.loads(json_string_str)
# print(decoded_str)
# print(type(decoded_str))

##drinking water reminder:
# from plyer import notification
# import schedule
# import time
# def remind():
#     notification.notify(
#         title='Drink Water Reminder',
#         message='Remember to drink water now!',
#         app_icon=None,  # you can specify an icon path if you want
#         timeout=10  # notification will disappear after 10 seconds
    # )
# #schedule initial reminder
# remind()
# Schedule reminders every hour
# schedule.every().hour.do(remind)
# schedule.every(2).hour.do(remind) #for reminding after 2 hours

# Run the schedule
# while True:
#     schedule.run_pending() #responsible for running any pending jobs scheduled with schedule.every().<interval>.do(<function>)
#     #ple, schedule.run_pending() is called inside a loop, ensuring that any pending jobs are executed at their scheduled times while the script continues to run.
#     time.sleep(1)  # Sleep for a second to avoid consuming too much CPU

# Import the following modules 
import pytesseract 
from PIL import Image 
import os 
import pywhatkit as kit 
# os.chdir(r"C:\Users\Dell\Downloads") 
# # Set the Path of Tesseract 
# pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Dell\AppData\/
# Local\Tesseract-OCR\tesseract.exe" 
img = Image.open("GFG.png") 
text = pytesseract.image_to_string(img)
kit.text_to_handwriting(text, rgb=[0, 0, 250]) 



























