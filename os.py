# import os #creating folders,files in folders,renaming files or folders,can print files in folders,location of directory
# if  not os.path.exists("data"):#checkpoint
#     os.mkdir("data")#data name ki directory/folder bn jaayega
# # for i in range(0,10):
# #     os.mkdir(f"data/Day{i+1}")#data folder mein 10 files bn jaayengi #give error ki data is already made so we need to give a checkpoint
# # for i in range(0,10):
# #     os.rename(f"data/Day{i+1}",f"data/Tutorial{i+1}") #rename("source","destination")
# # folders=os.listdir("data") ##gives directories in data
# # print(folders)
# #                                    ##Or
# # for folder in folders:
# #     print(folder)
# #     print(os.listdir(f"data/{folder}")) ##will print folder in data --> tutorial-->andr ki files
# print(os.getcwd()) ##to know about location of ur directory
# os.chdir("/Users") ##change the location of directory
# print(os.getcwd()) ##to know about location of ur directory
