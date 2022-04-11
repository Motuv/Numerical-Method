import math
import random as rd

x1 = 0
x2 = math.pi
n = 10

def function(x):
    #here code your function
    return x*math.sin(x)

def rightRectangleMethod(x1, x2, n):
    dx = (x2-x1)/n
    i = 0
    x = x1
    result = 0
    while i < n:
        x += dx
        result += function(x)
        i += 1
    result *= dx
    return result

def leftRectangleMethod(x1, x2, n):
    dx = (x2-x1)/n
    i = 0
    x = x1
    result = 0
    while i < n:
        result += function(x)
        x += dx
        i += 1
    result *= dx
    return result

def midRectangleMethod(x1, x2, n):
    dx = (x2-x1)/n
    i = 0
    x = x1
    x += dx/2
    result = 0
    while i < n:
        result += function(x)
        x += dx
        i += 1
    result *= dx
    return result

def trapezeMethod(x1, x2, n):
    dx = (x2-x1)/n
    i = 0
    x = x1
    result = 0
    while i < n:
        result += (function(x) + function(x+dx))
        i += 1
        x += dx
    result *= dx/2
    return result

def simpsonMethod(x1, x2, n):
    dx = (x2-x1)/n
    x = x1
    result = 0
    for i in range(n):
        result += (function(x)+4*function(x+(dx/2))+function(x+dx))
        x += dx
    return result*(dx/6)

def monteCarloMethod(x1,x2,n):
    sum = 0
    for i in range(n):
        sum += function(rd.random()*(x2-x1)+x1)
    average = sum/n
    return average*(x2-x1)

"""print("Metoda prawych prostokątów: %.4f"% rightRectangleMethod(x1, x2, n))
print("Metoda lewych prostokątów: %.4f"% leftRectangleMethod(x1, x2, n))
print("Metoda średnich prostokątów: %.4f"% midRectangleMethod(x1, x2, n))
print("Metoda trapezów: %.4f"% trapezeMethod(x1, x2, n))"""
print("Metoda Simpsona: %.4f"%simpsonMethod(x1,x2,n))
print("Metoda Monte Carlo: %.4f"%monteCarloMethod(x1,x2,n))
