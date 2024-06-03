 #command line :terminal/shell/command prompt:where commands are written
 #command line arguments: additional inputs provided to a program when it is executed from command line
 #myscript.py arg1 arg2 arg3 :arg1,arg2,arg3 are cmd line arguments that can be accessed by myscript.py

 #ways to deal with cmd line args:
 #1.using sys.argv
 #2.use getopt module
 #3. using argparse module

 ##eg: python abc.py 'hello' 'hi' 1 556 234
 #first arg: abc.py
 #secong arg: hello.....

#1
 # sys.argv
 # sys module: provides access to some variables used or maintained by python interpreter 
 # and functions that interact strongly with interpreter
  # sys.argv: access command line arguments + list structure 
  #len(sys.argv):number of cmd line arguments
  #sys.argv[0]:name of current python script

# import sys
# n=len(sys.argv)
# print(n)
# print(type(sys.argv)) ##list
# print(sys.argv[0])
# for i in range (1,n):
#     print(sys.argv[i],end=" ")
# sum=0
# for i in range(1,n):
#     sum+=int(sys.argv[i])
# print(sum)

#2
#getopt() method: function in getopt module
#getopt module:parse cmd line args in script. handles cmd line args in structured manner
#u can define short and long options for script and retrieve values spevcified by user on running script on cmd line
# import sys
# import getopt
# def usage():
#     print("...........")
# def main(argv):
#     input_file=''
#     output_file=''
#     try:
#         #option arguments stored in opts as tuples
#         #args mein non option arguments are stored
#         opts,args=getopt.getopt(argv,"hi:o:",["help","ifile=","ofile="])
#         #hi:o:-->h(short option ) means -h is accepted as option, no arg is req by it
#         #i::-->-i as an option and req arg to be provided to it. arg stored in input_file
#         #o::-->-o as an option and req arg to be provided to it. arg stored in output_file
#         #colon after i and o indicates-->arguments are required. 
#     except getopt.GetoptError:
#         usage()
#         sys.exit(2)###it is used to terminate the system with status code=2.
#         #convention in unix like OS where non zero exit status denotes error
#     print(opts)
#     print(args)
#     for opt,arg in opts:
#         if opt==('-h','--help'):
#             usage()
#             sys.exit()
#         elif opt in ("-i","--ifile"):
#             input_file=arg
#         elif opt in ("-o","--ofile"):
#             output_file=arg
#         print(input_file)  
#         print(output_file)
    
# if __name__=="__main__":
#     main(sys.argv[1:])  

#3:
#argparse module: simplifies process of parsing cmd line arg, handlling options and subcommands,generating help messages:
#better than sys.argv and getopt module
# import argparse
# parser=argparse.ArgumentParser(description='Program starts')
# print(parser)
# parser.add_argument('-i','--ifile',help='input file')
# parser.add_argument('-o','--ofile',help='output file')
# args=parser.parse_args()
# print(args)
# input_file=args.ifile
# output_file=args.ofile
# print(input_file)
# print(output_file)

##argparse is better than sys.argv and getopt() as:
#1.automatic generation of help messages
#2.support for positional arguments and optional
#3.argparse allows you to specify datatype and automatically converts string arg provided on command line to specified type
#4.we can set default values for args which will be used if user doenot give input
#5.more readable
#6.better error handling

# import argparse
# parser=argparse.ArgumentParser(description='Program starts')
# parser.add_argument('-i','--ifile',default='input.txt',help='input file')
# parser.add_argument('-o','--ofile',default='output.txt',help='output file')
# args=parser.parse_args()
# ##optional arguments:
# input_file=args.ifile
# output_file=args.ofile
# print(input_file)
# print(output_file)

##argparse automatically does type conversion:
# import argparse
# parser=argparse.ArgumentParser(description='Program starts')
# parser.add_argument('-n','--number',type=int,help='A number')
# args=parser.parse_args()
# # print(args)
# if args.number is not None:
#     print((args.number)**2)
# else:
#     print("none")

##sub-commands:
# import argparse
# parser=argparse.ArgumentParser(description='hello')
# subparser=parser.add_subparsers(title="subcommands",dest="command") #dest signifies attribute where subcommands will be stored
# run_parser=subparser.add_parser('run',help='Run Program')
# run_parser.add_argument('input_file',help='Input file path')
# run_parser.add_argument('output_file',help='Output file path')

# args=parser.parse_args()
# if args.command=='run':
#     print("input:",args.input_file,"and output:",args.output_file)
# else:
#     print("command not recognised")

















