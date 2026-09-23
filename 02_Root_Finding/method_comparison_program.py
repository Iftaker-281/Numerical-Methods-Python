def f(x):
    return x**3 - x - 2
def df(x):
    return 3*x**2-1
    
def bisection(a,b):
    for i in range(20):
        mid = (a+b)/2
        if abs(f(mid))<0.005:
            return i+1,mid
        if f(a) * f(mid)<0:
            b = mid
        else:
            a = mid
    return i+1,mid
def newton_rapshon(x):
    for i in range(20):
        x_new = x - f(x)/df(x)
        if abs(x_new - x)<0.005:
            return i+1,x_new
        x = x_new
    return i+1,x_new

def secant(x0,x1):
    for i in range(20):
        x_new = x1 - f(x1) * (x1 - x0)/(f(x1)-f(x0))
        if abs(x_new - x1)<0.005:
            return i+1,x_new
        x0 = x1
        x1 = x_new
    return i+1,x_new
print("Bisection = ",bisection(1,2))
print("Newton = ",newton_rapshon(1))
print("Secant = ",secant(1,2))
