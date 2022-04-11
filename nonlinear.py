import math

epsilon = 1.0e-10
a = -1
b = 1.2

def bisectionMethod(a, b):
    if function(a) * function(b) >= 0:
        print("Bisection method fails")
        return None
    x1 = (a + b) / 2
    if function(x1) == 0:
        return x1

    if math.fabs(b - a) > epsilon:
        if function(x1) * function(a) < 0:
            return bisectionMethod(a, x1)
        elif function(x1) * function(b) < 0:
            return bisectionMethod(x1, b)
    return x1


def newtonRaphsonMethod(a):
    x1 = a
    x2 = x1 - function(x1)/derivative(x1)
    if math.fabs(function(x2)) <= epsilon or math.fabs(x2-x1) <= epsilon:
        return x2
    else:
        return newtonRaphsonMethod(x2)

def function(x):
    return -math.pow(x,2)+5

def derivative(x):
    return -2*x

print("N-R method: %.5f" % newtonRaphsonMethod(a))
print("Bisection method: %.5f" % bisectionMethod(a, b))
