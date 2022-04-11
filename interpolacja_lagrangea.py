import math

points_x = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
points_y = [1/26,1/17,0.1,0.2,0.5,1,0.5,0.2,0.1,1/17,1/26]
argument = 0.5

def lagrange_int(x,y,arg):
    value = 0
    for i in range(len(x)):
        multiplicator=1
        for j in range(len(x)):
            if i!=j:
                multiplicator=multiplicator*(arg-x[j])/(x[i]-x[j])
        value=value+y[i]*multiplicator
    return value

for i in range(len(points_x)):
    print(i,": ","x = %.5f" % points_x[i],"y =%.5f" % points_y[i])
print("L(",argument,") = %.5f" % lagrange_int(points_x, points_y, argument))
print("f(0.5)=%.5f"%(1/(1+math.pow(0.5,2))))
print("L(",1.5,") = %.5f" % lagrange_int(points_x, points_y, 1.5))
print("f(1.5)=%.5f"%(1/(1+math.pow(1.5,2))))
print("L(",2.5,") = %.5f" % lagrange_int(points_x, points_y, 2.5))
print("f(2.5)=%.5f"%(1/(1+math.pow(2.5,2))))
print("L(",3.5,") = %.5f" % lagrange_int(points_x, points_y, 3.5))
print("f(3.5)=%.5f"%(1/(1+math.pow(3.5,2))))
print("L(",4.5,") = %.5f" % lagrange_int(points_x, points_y, 4.5))
print("f(4.5)=%.5f"%(1/(1+math.pow(4.5,2))))


