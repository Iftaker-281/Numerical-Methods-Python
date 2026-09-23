#f(x) = x**3 − 6x**2 + 11x − 6
#Run the program with different starting values:
#x0 = 0.5, 2.5, 4

#Record:• Obtained root • Number of iterations • Final error


def f(x):
    return x**3-6*x**2+11*x-6
def df(x):
    return 3*x**2-12*x+11
tolerance = 0.005
for start in [0.5,2.5,4]:
    x_old = start
    for i in range(20):
        x_new = x_old -f(x_old)/df(x_old)
        error = abs(x_new - x_old)
        if error<tolerance:
            break
        x_old = x_new
    print("Starting value: ",start)
    print("Itertion: ",i+1)
    print("Root: ",x_new)
    print("Final: ",error)
    print()
