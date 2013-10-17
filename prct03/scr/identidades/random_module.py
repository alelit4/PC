#! /usr/bin/python

import sys
import random

# print "This is the name of the script: ", sys.argv[0]
# print "Number of arguments: ", len(sys.argv)
# print "The arguments are: " , str(sys.argv)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


A = -100
B = 100



if  len(sys.argv) == 2:
    for i in range(0,int(sys.argv[1])):
        a = random.uniform(A, B)
        b = random.uniform(A, B)
        print bcolors.HEADER + '--------- i = ', i+1, '---------'
       
        print  bcolors.OKBLUE + 'a = ', a
        print bcolors.OKGREEN + 'b = ', b, bcolors.ENDC
else:
    print bcolors.FAIL + "FAIL: No arguments. Try again!" + bcolors.ENDC