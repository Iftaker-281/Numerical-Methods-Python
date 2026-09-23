def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1


def bisection(a,b,tolerance):

    x_old = (a+b)/2

    for i in range(20):

        x_new = (a+b)/2

        error = abs(x_new-x_old)/abs(x_new)

        if f(a)*f(x_new) < 0:
            b = x_new
        else:
            a = x_new

        print("Bisection Iteration",i+1,"Error",error,"Root",x_new)

        if error < tolerance:
            return i+1,x_new,error

        x_old = x_new


def newton(x_old,tolerance):

    for i in range(20):

        x_new = x_old - f(x_old)/df(x_old)

        error = abs(x_new-x_old)/abs(x_new)

        print("Newton Iteration",i+1,"Error",error,"Root",x_new)

        if error < tolerance:
            return i+1,x_new,error

        x_old = x_new


def secant(x0,x1,tolerance):

    for i in range(20):

        x_new = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))

        error = abs(x_new-x1)/abs(x_new)

        print("Secant Iteration",i+1,"Error",error,"Root",x_new)

        if error < tolerance:
            return i+1,x_new,error

        x0 = x1
        x1 = x_new


tolerance = 0.0001

iteration1,root1,error1 = bisection(1,2,tolerance)

iteration2,root2,error2 = newton(1.5,tolerance)

iteration3,root3,error3 = secant(1,2,tolerance)


print()
print("Approach       Iteration       Final Root")
print("Bisection      ",iteration1,"          ",root1)
print("Newton         ",iteration2,"          ",root2)
print("Secant         ",iteration3,"          ",root3)
