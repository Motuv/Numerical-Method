import math

points_x = [-5,-3,-2,-1,0,1,2,3,4]
points_y = [2,4,-2,-3,5,6,7,1.5,0]
argument = 1

def newton_int(x, y, arg):
    value = y[0]
    multiplicator = 1
    y_indicator = 1
    x_indicator = 1
    for i in range(1, len(x)):
        multiplicator = multiplicator * (arg - x[i - 1])
        for j in range(len(x) - i):
            y.append((y[y_indicator] - y[y_indicator - 1]) / (x[y_indicator - x_indicator + i] - x[y_indicator - x_indicator]))
            y_indicator += 1
            if j == 0:
                value += y[-1] * multiplicator
        y_indicator += 1
        x_indicator = x_indicator + len(x) - i + 1
    return value

for i in range(len(points_x)):
    print("x: ",points_x[i]," y: ",points_y[i])
print("W(x): ",-4," y: %.3f" % newton_int(points_x, points_y, -4))
print("W(x): ",-1.5," y: %.3f"% newton_int(points_x, points_y, -1.5))
print("W(x): ",0.5," y: %.3f"% newton_int(points_x, points_y, 0.5))
print("W(x): ",2.4," y: %.3f"% newton_int(points_x, points_y, 2.4))
print("W(x): ",3.6," y: %.3f"% newton_int(points_x, points_y, 3.6))
