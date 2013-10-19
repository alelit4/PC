#!/usr/bin/python

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

print bcolors.HEADER + "************************************************************"
print "***    PRACTICA 03     -      PROGRAMACION CIENTIFICA   ****"
print "************************************************************" + bcolors.ENDC


if  len(sys.argv) == 2:
    error = 0
    for i in range(0,int(sys.argv[1])):
        a = random.uniform(A, B)
        b = random.uniform(A, B)
        if ((a * b)**3) != (a**3 * b**3):
           error += 1
           
    print "************************************************************"
    print "***   Se cumple ((a * b)**3) == (a **3 * b **3) ?       ****" 
    print "************************************************************"
    print "***          RESULTADOS DE LAS PRUEBAS                  **** "
    print "************************************************************"
    print "***" + bcolors.OKBLUE +"   Pruebas realizadas = ", sys.argv[1], bcolors.ENDC, "                       ****"
    print "***" + bcolors.OKGREEN +"   Porcentaje de errores = ", error*100/float(sys.argv[1]), "%", bcolors.ENDC ,"                 ****"
    print "************************************************************"
else:
    print bcolors.FAIL +  "************************************************************"
    print "***      FAIL: No arguments. Try again!                 ****" 
    print  "************************************************************" + bcolors.ENDC
    
