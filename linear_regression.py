import math

xs = [0,0.78,1.57,2.35,3.14,3.92,4.7,5.5,6.28]
ys = [0,1,0,-1,0,1,0,-1,0]


def linreg(x, y):
    xsum, ysum, xsquaresum, xyproduct, ysquaresum, n = 0, 0, 0, 0, 0, len(x)
    for i in range(len(x)):
        xsum += x[i]
        ysum += y[i]
        xsquaresum += x[i] * x[i]
        ysquaresum += y[i] * y[i]
        xyproduct += x[i] * y[i]
    a1 = ((n * xyproduct) - (xsum * ysum)) / ((n * xsquaresum) - (xsum * xsum))
    a0 = (ysum * xsquaresum - (xsum * xyproduct)) / (n * xsquaresum - (xsum * xsum))
    corellation = (n * xyproduct - (xsum * ysum)) / (
                math.sqrt(n * xsquaresum - (xsum * xsum)) * math.sqrt(n * ysquaresum - (ysum * ysum)))
    coef = [a0, a1, corellation]
    return coef


def printresult(coef):
    print("y = %.5f x + %.5f\nCorrelation: %.5f" % (coef[1], coef[0], coef[2]))


printresult(linreg(xs, ys))
