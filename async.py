# ###Synchronous Code
# # import time
# # def brewCoffee():
# #     print("Start brewCoffee()")
# #     time.sleep(3)
# #     print("End brewCoffee()")
# #     return "Coffee Ready"
# # def toastBage1():
# #     print("Start toastBage1()")
# #     time.sleep(2)
# #     print("End toastBage1()")
# #     return "Bage1 toasted"
# # def main():
# #     start_time=time.time()
# #     result_coffee=brewCoffee()
# #     result_bage1=toastBage1()
# #     end_time=time.time()
# #     elapsed_time=end_time-start_time
# #     print(f"Result of brewCoffee:{result_coffee}")
# #     print(f"Result of toastBage:{result_bage1}")
# #     print(f"Total execution time:{elapsed_time}")
# #     if __name__=="__main__":
# #         main()

# ##ASynchronous Code
# # asyncio is module. await and async are keyword. function using await shoulld be written as async fun()
# # elapsed time in case of asynchronous comes less as compared to synchronous
# # summary:Even in Asynchronous gather function is more preferable as it consumes least time
# import asyncio
# import time
# async def brewCoffee():
#     print("Start brewCoffee()")
#     await asyncio.sleep(3)
#     print("End brewCoffee()")
#     return "Coffee Ready"
# async def toastBage1():
#     print("Start toastBage1()")
#     await asyncio.sleep(2)
#     print("End toastBage1()")
#     return "Bage1 toasted"
# async def main():
#     start_time=time.time()
#     ##use of gather function
#     # batch=asyncio.gather(brewCoffee(),toastBage1()) ##calling of coroutines in batch for concurrent execution. returns coroutine object
#     # result_coffee,result_bage1=await batch
#     #to get return values we need to await them
#                                    ##alternative for gather function i.e. using create_task function in asyncio module
#     coffee_task=asyncio.create_task(brewCoffee())
#     toast_task=asyncio.create_task(toastBage1())
#     result_coffee=await coffee_task
#     result_bage1=await toast_task
#     end_time=time.time()
#     elapsed_time=end_time-start_time
#     print(f"Result of brewCoffee:{result_coffee}")
#     print(f"Result of toastBage:{result_bage1}")
#     print(f"Total execution time:{elapsed_time}")
#     if __name__=="_main_":
#         # main()
#         asyncio.run(main())

##Multithreading: To download many things simultaneously.
# It allows multiple threads of execution to run concurrently within a single process.
# import threading
# import time
# from concurrent.futures import ThreadPoolExecutor ##!important
# def func(seconds):
#     print(f"Sleeping for {seconds}")
#     time.sleep(seconds)
#     return seconds
#Normal code
# time1=time.perf_counter()
# func(4)
# func(2)
# func(1)
# time2=time.perf_counter()
# print(time2-time1)
#code using threads
# time1=time.perf_counter() #calculates time in float in seconds
# t1=threading.Thread(target=func,args=[4])
# t2=threading.Thread(target=func,args=[2])
# t3=threading.Thread(target=func,args=[1])
# t1.start() #will just start execution but not wait for getting executed
# t2.start()
# t3.start()

# t1.join()#though output will come faster but wait for complete execution
# t2.join()
# t3.join()
# time2=time.perf_counter()
# print(time2-time1)

# def poolingDemo():#this will also complete execution and then print time
#     with ThreadPoolExecutor() as executor:
#         time1=time.perf_counter()
#         future1=executor.submit(func,3)
#         future2=executor.submit(func,2)
#         future3=executor.submit(func,4)
#         print(future1.result())
#         print(future2.result())
#         print(future3.result())
#         time2=time.perf_counter()
#         print(time2-time1)
# poolingDemo()
# def poolingDemo():
#     with ThreadPoolExecutor() as executor:
#         time1=time.perf_counter()
#         l=[3,5,2,1]
#         results=executor.map(func,l) #map function in ThreadPoolExecutor of concurrent.futures
#         for result in results:
#            print(result)
#         time2=time.perf_counter()
#         print(time2-time1)
# poolingDemo()

###Multiprocessing:multiple processes through same program.
# import multiprocessing
# import requests
#code snippet used when downloading images or binary files from web and saving them to local file system
# def downloadFile(url,name):
#     response=requests.get(url)
#     open(f"{name}.jpg","wb").write(response.content)#wb stands for write binary. this code opens the file  in write binary mode. if file donot exist it will be created otherwise its content will be overwritten. 
#     # .write--> writes the binary content of response object to file. response.content-->contains raw binary data obtained from HTTP requests
# url="https://picsum.photos/200/300" #link providing random pics
# for i in range(5):
#     downloadFile(url,i)
                       ###OR
import multiprocessing
import requests
from concurrent.futures import ProcessPoolExecutor
def downloadFile(url,name):
    print(f"Started Downloading {name}")
    response=requests.get(url)
    open(f"{name}.jpg","wb").write(response.content)
    print(f"Finished Downloading {name}")
if __name__=="__main__": 
 url="https://picsum.photos/200/300" #link providing random pics
 pros=[]
#  for i in range (5):
#     p=multiprocessing.Process(target=downloadFile,args=[url,i])
#     p.start()
#     pros.append(p)
#  for p in pros:
#     p.join()
                         ##or
 with ProcessPoolExecutor() as process:
    l1=[i for i in range(5)]
    l2=[url for i in range(5)]
    results=process.map(downloadFile,l2,l1)
    for r in results:
        print(r)


##when you run a Python script directly from command line, that script is considered the main Program.
# When you import Python script into another script it is treated as module
# __name__ variable: in python, each scriot has a built-in variable called __name__.
# For script being directly executed, __name__ is set to __main__.abs
# #but for modules,__name__ is set to module name
# if __name__="__main__"--> This conditional block allows you to include code that should only run when script is executed directly, not when imported as amodule
# It helps to distinguish the code from code that is meant for module functionlity.
# when script is imported the code inside this block is prevented. It is only executed when script is directly executed. 

















