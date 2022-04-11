import SolverSystemOfLinearEquations as solver
from matplotlib import pyplot as plt
import math
import newton_int as newton
import interpolacja_lagrangea as lagrange

def cubic_splines(x, y):
    eta = []
    h = []
    a = []
    c = []
    d = []
    array = []
    for i in range(len(x)-1):
        h.append(x[i + 1] - x[i])
        eta.append(y[i + 1] - y[i])
        d.append(y[i])
    d.append(y[len(y)-1])

    for i in range(len(x) - 1):
        row = []
        #first row
        if i == 0:
            row.append(h[1])
            row.append(-h[0] - h[1])
            row.append(h[0])
            for j in range(i + 2, len(x)):
                row.append(0)
        # middle rows
        else:
            for j in range(0, i - 1):
                row.append(0)
            row.append((1 / 3) * h[i - 1])
            row.append((2 / 3) * (h[i - 1] + h[i]))
            row.append((1 / 3) * h[i])
            for j in range(i + 1, len(x) - 1):
                row.append(0)
            row.append((eta[i] / h[i]) - (eta[i - 1] / h[i - 1]))
        array.append(row)
    #last row
    row = []

    for i in range(0, len(x) - 3):
        row.append(0)
    row.append(h[len(h)-1])
    row.append(-h[len(h) - 2] - h[len(h)-1])
    row.append(h[len(h) - 2])
    row.append(0)
    array.append(row)

    b = solver.gaussMethod(array)
    for i in range(len(d)-1):
        a.append((1 / (3 * h[i])) * (b[i + 1] - b[i]))
        c.append((eta[i] / h[i]) - ((1 / 3) * h[i] * (b[i + 1] + 2 * b[i])))
    printResult(a, b, c, d, x, y)
    '''a = [0.04,-0.08,0]
    b = [0, 0.25, -0.24]
    c = [0.84, 1.33,1.35]
    d = [2,4,7]
    printResult(a, b, c, d, x, y)'''

def printResult(a, b, c, d, x, y):
    for i in range(len(a)):
        print("g %d (x) = %.3f (x - %.3f)^3 + %.3f(x - %.3f)^2 + %.3f(x - %.3f) + %.3f" % (
        i, a[i], x[i], b[i], x[i], c[i], x[i], d[i]))

    plt.plot(x,y)
    pointsx, pointsy = [], []
    for i in range(int(x[0]*100), int(x[len(x)-1]*100)):
        j = i/100
        for k in range(len(x)-1):
            if x[k]*100 <= i <= x[k+1]*100:
                pointsx.append(j)
                pointsy.append((a[k]*math.pow(j-x[k],3))+(b[k]*math.pow(j-x[k],2))+(c[k]*(j-x[k]))+d[k])
    plt.plot(pointsx, pointsy, color='red', label='cubic')
    plt.show()

def plotLagrangeAndNewton(x,y):
    pointsx, pointsy, pointsy_newton = [], [], []
    for i in range(int(x[0]*100), int(x[len(x)-1]*100)):
        j = i/100
        for k in range(len(x)-1):
            if x[k]*100 <= i <= x[k+1]*100:
                pointsx.append(j)
                pointsy.append(lagrange.lagrange_int(x,y,j))
                pointsy_newton.append(newton.newton_int(x, y, j))
    #plt.plot(pointsx, pointsy, label='lagrange', color='blue')
    #plt.plot(pointsx, pointsy, label='newton', color='green')
    plt.legend(loc='upper left')
    plt.show()

#xs = [0,0.02,0.036,0.06,0.094,0.133,0.164,0.196,0.234,0.264,0.285,0.3]
#ys = [0,4.7,7.7,10.5,11.5,10,7,6,8,12,16,19]

#xs = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
#ys = [1/26,1/17,0.1,0.2,0.5,1,0.5,0.2,0.1,1/17,1/26]

xs = [-5,-3,-2,-1,0,1,2,3,4]
ys = [2,4,-2,-3,5,6,7,1.5,0]

cubic_splines(xs, ys)
#plotLagrangeAndNewton(xs,ys)