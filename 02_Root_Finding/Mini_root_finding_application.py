#Mini Root Finding Application
#Develop a menu driven Python program.
#Menu:

#1. Interval based solver
#2. Boundary estimation solver
#3. Derivative based solver
#4. Two guess solver
#5. Fixed point solver

#User enters:
#• Equation
#• Required accuracy
#• Initial information
#The program must print a complete iteration table and final result.

def f(x):
    return x**3 - 4*x - 9

def df(x):
    return 3*x**2-4

def g(x):
    return (4*x+9)**(1/3)


def bisection(a,b,tolerance):
    mid_old = 0

    for i in range(20):
        mid = (a+b)/2

        if i > 0:
            error = abs((mid-mid_old)/mid)*100

            print("Iteration: ",i+1,"a: ",a,"b: ",b,
                  "Mid: ",mid,"Error: ",error)

            if error < tolerance:
                return i+1,mid,error

        if f(a)*f(mid)<0:
            b = mid
        else:
            a = mid

        mid_old = mid


def falseposition(a,b,tolerance):
    mid_old = 0

    for i in range(20):
        mid = (a*f(b)-b*f(a))/(f(b)-f(a))

        if i > 0:
            error = abs((mid-mid_old)/mid)*100

            print("Iteration: ",i+1,"a: ",a,"b: ",b,
                  "Mid: ",mid,"Error: ",error)

            if error < tolerance:
                return i+1,mid,error

        if f(a)*f(mid)<0:
            b = mid
        else:
            a = mid

        mid_old = mid


def newton(x,tolerance):
    for i in range(20):
        x_new = x-f(x)/df(x)
        error = abs(x_new-x)

        print("Iteration: ",i+1,
              "x_new: ",x_new,"Error: ",error)

        if error<tolerance:
            return i+1,x_new,error

        x = x_new


def secant(x0,x1,tolerance):
    for i in range(20):
        x_new = x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
        error = abs((x_new-x1)/x_new)*100

        print("Iteration: ",i+1,
              "x_new: ",x_new,"Error: ",error)

        if error<tolerance:
            return i+1,x_new,error

        x0 = x1
        x1 = x_new


def fixedpoint(x,tolerance):
    for i in range(20):
        x_new = g(x)
        error = abs(x_new-x)

        print("Iteration: ",i+1,
              "x_new: ",x_new,"Error: ",error)

        if error<tolerance:
            return i+1,x_new,error

        x = x_new


print("1.Interval Based Solver")
print("2.Boundary Esimation Solver")
print("3.Derivative Based Solver")
print("4.Two gusses Solver")
print("5.Fixed point Solver")

n = int(input("Enter n: "))

tolerance = 0.5*10**(2-n)

print("Tolerance: ",tolerance)

choice = int(input("Enter your choice: "))


if choice == 1:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    iteration,root,error = bisection(a,b,tolerance)

elif choice == 2:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    iteration,root,error = falseposition(a,b,tolerance)

elif choice == 3:
    x = float(input("Enter initial value: "))
    iteration,root,error = newton(x,tolerance)

elif choice == 4:
    x0 = float(input("Enter x0: "))
    x1 = float(input("Enter x1: "))
    iteration,root,error = secant(x0,x1,tolerance)

elif choice == 5:
    x = float(input("Enter initial value: "))
    iteration,root,error = fixedpoint(x,tolerance)


print("Final result")
print("Root = ",root)
print("Iteration = ",iteration)
print("Final error = ",error)
