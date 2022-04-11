import math
from matplotlib import pyplot as plt

def function(x, y):
    return x+y

def analyticSolution(x):
    return math.exp(x)-x-1

def plotAnalyticSolution(x0, h, b):
    xs = [x0]
    N = round((b - x0) / h)
    for i in range(N):
        xs.append(xs[i] + h)
    ys = []
    for i in xs:
        ys.append(analyticSolution(i))
    plt.plot(xs, ys, label="exact")

def eulerMethod(x0, y0, h, b):
    N = round((b - x0) / h)
    x = [x0]
    y = [y0]
    for i in range(0, N):
        x.append(x[i] + h)
        y.append(y[i] + (h * function(x[i], y[i])))

    return x, y

def heunMethod(x0,y0, h, b):
    N = round((b - x0) / h)
    x = [x0]
    y = [y0]
    for i in range(0, N):
        x.append(x[i] + h)
        value = function(x[i], y[i])
        y.append(y[i] + ((h/2) * ((value)+function(x[i+1], y[i]+h*value))))

    return x, y

def rungeKutta4Method(x0,y0,h,b):
    N = round((b - x0) / h)
    x = [x0]
    y = [y0]
    for i in range(0,N):
        x.append(x[i]+h)
        k1 = h*function(x[i],y[i])
        k2 = h*function(x[i]+(0.5*h), y[i]+(0.5*k1))
        k3 = h*function(x[i]+(0.5*h), y[i]+(0.5*k2))
        k4 = h*function(x[i]+h, y[i]+k3)
        y.append(y[i]+(k1+2*k2+2*k3+k4)/6)

    return x,y

x0 = 0
y0 = 0
h = 0.5
b = 2

x, y = eulerMethod(x0,y0,h,b)
plt.plot(x, y, label="euler")
x, y = heunMethod(x0,y0,h,b)
plt.plot(x, y, label="heun")
x, y = rungeKutta4Method(x0,y0,h,b)
plt.plot(x, y, label="R-K 4")
plotAnalyticSolution(x0, h/10, b)
plt.legend(loc="upper left")
plt.show()
