#! /usr/bin/python

import sys
import random

# print "This is the name of the script: ", sys.argv[0]
# print "Number of arguments: ", len(sys.argv)
# print "The arguments are: " , str(sys.argv)

#A = float(sys.argv[1])
#B = float(sys.argv[2])
A = -100
B = 100

if  len(sys.argv) == 2:
    for i in range(0,int(sys.argv[1])):
        a = random.uniform(A, B)
        b = random.uniform(A, B)
        print '--------- i = ', i+1, '---------'
        print 'a = ', a
        print 'b = ', b 
else:
    print 'Debe introducir un dato en argv'