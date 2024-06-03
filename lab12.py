##1.
# dict_={"facebook":4,"instagram":4.5,"linkedin":4.9}
# a=max(dict_.values())
# print(a)
# print(dict_.values())
# print(dict_.keys())
# dict_.pop("linkedin")
# dict_.setdefault("intershala",4.8)
# dict_["facebook"]=3
# print(dict_)
# for key in dict_.keys():
#     a=int(input())
#     dict_[key]=a
# print (dict_)

##2:
# dict_={"India":{"capital":"Delhi","language":"hindi"},"USA":{"capital":"washington","language":"english"}}
# country=input("enter country=")
# if country not in dict_.keys():
#     print("country data not there")
# else:
#  print(dict_[country]["capital"])
#  print(dict_[country]["language"])

##3:
# def vowel(list_):
#     new_list=[]
#     for name in list_:
#         if name[0]=='a'or name[0]=='e' or name[0]=='i' or name[0]=='o' or name[0]=='u':
#             new_list.append(name)
#         else:
#             continue
#     return new_list
# list_=["diya","baani","saanvi","arvind","manan"]
# new=vowel(list_)
# print(f"original list={list_}")
# print(f"new list={new}")

##3b
# list_=[("Diya",19),("Baani",18),("mumma",40)]
# new_list=[person  for (person,age) in list_ if age>30 ]
# print(new_list)

#4:
# list_=[1,2,3,4,5]
# list_=[number for number in list_ if number%2==0]
# print(list_)

##4b:
# list_=[1,2,3,4,5]
# list_2=[number for number in list_ if number%2==0]
# print(list_)
# print(list_2)

##5.
# list_=["diya","baani","saanvi"]
# new_list=[len(name) for name in list_]
# print(new_list)

##5b:
# list_=["diya","baani","saanvi"]
# new_list=list_.copy()
# list_=[len(name) for name in list_]
# new_list=[len(name) for name in new_list]
# print(new_list)
# print(list_)

##6.
def max_book(list_):
    max=0
    # tile_of_max=""
    for book in list_:
        if book["pages"]>max:
            max=book["pages"]
            break
            # tile_of_max=book["title"]
    return book["title"]
# list_=[{"title":"wings of fire","author":"apj","pages":200},{"title":"rich and poor dad","author":"kiyosaki","pages":300}]

list_ = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "pages": 180},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "pages": 281},
    {"title": "1984", "author": "George Orwell", "pages": 328},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "pages": 279}
]
x=max_book(list_)
print(x)






