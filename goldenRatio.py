phi = ((5**0.5)/2)-0.5
epsilon = 0.001

def function(x):
    return x*x


def goldenRatio(a, b):
    if (b - a) > epsilon:
        xl = b-(phi*(b-a))
        xp = a+(phi*(b-a))
        if function(xl) > function(xp):
            goldenRatio(xl, b)
        else:
            goldenRatio(a, xp)
    elif (b - a) <= epsilon:
        print("Minimum: ", a)

goldenRatio(-2, 2)