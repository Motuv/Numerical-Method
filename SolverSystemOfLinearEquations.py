import math
import random as rd
import sys
import numpy as np
import time

def gaussMethod(array):
    x = np.zeros(len(array))
    # elimination
    for i in range(len(array)):
        if array[i][i] == 0.0:
            sys.exit('Dzielenie przez zero!')
        for j in range(i + 1, len(array)):
            coef = array[j][i] / array[i][i]
            for k in range(len(array[i])):
                array[j][k] -= coef * array[i][k]
    # solution
    x[len(array) - 1] = array[len(array) - 1][len(array)] / array[len(array) - 1][len(array) - 1]

    for i in range(len(array) - 2, -1, -1):
        x[i] = array[i][len(array)]
        for j in range(i + 1, len(array)):
            x[i] = x[i] - array[i][j] * x[j]
        x[i] = x[i] / array[i][i]

    # show results
    #print('\nRozwiazanie: ')
    #for i in range(len(array)):
    #    print('X%d = %0.2f' % (i, x[i]))
    return x


def generateSoLE(n):
    t = []
    for i in range(n):
        temp = []
        temp.clear()
        j = 0
        for j in range(n + 1):
            temp.insert(j, round((rd.random() - 0.5) * 100, 2))
        t.insert(i, temp)
    return t


def checkCorrection(array, x, tolerance):
    for i in range(len(array)):
        result = 0
        for j in range(len(array)):
            result += array[i][j] * x[j]
        if array[i][j + 1] + tolerance <= result <= array[i][j + 1] - tolerance:
            return False
    return True

#sole = [[10,-7,0,6],[-3,2,6,4],[5,-1,5,3]]
#sole = generateSoLE(16)
#array = sole

correct = 0
incorrect = 0
tol = 0
for i in range(10):
    tol = math.pow(10, -(i * 5))
    correct = 0
    incorrect = 0
    for k in range(30):
        for j in range(8, -1, -1):
            sole = generateSoLE(pow(2,j))
            array = sole
            results = gaussMethod(sole)
            if checkCorrection(array, results, tol):
                correct+=1
            else:
                incorrect+=1
    print("Tolerance: ",tol)
    print("Poprawne: ", ((correct / 270) * 100), "%, niepoprawne: ", ((incorrect / 270) * 100), "%")


#sole = generateSoLE(16)
#array = sole
'''for i in range(len(sole)):
    print("[",end="")
    for j in range(len(sole)):
        print("%.2f"%sole[i][j], ",",end=""),
    print("]",end="")
    j += 1
    print("[x]","=[",sole[i][j],"]\n")'''
#start = time.time()
#results = gaussMethod(sole)
#end = time.time()
#print("Rozmiar: 16, Czas: %.4f"% (float)(end - start))
'''for i in range(len(sole)):
    print("[",end="")
    for j in range(len(sole)):
        print("%.2f"%sole[i][j], ",",end=""),
    print("]",end="")
    j += 1
    print("[","%.2f"%results[i],"]","=[","%.2f"%sole[i][j],"]\n")'''
