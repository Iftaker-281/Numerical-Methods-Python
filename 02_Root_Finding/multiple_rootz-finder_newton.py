def f(x):
    return x**3 - 6*x**2 + 11*x - 6

def df(x):
    return 3*x**2 - 12*x + 11


for start in [0.5, 2.5, 4]:

    x = start

    for i in range(20):
        x_new = x - f(x)/df(x)
        error = abs(x_new-x)

        if error < 0.0001:
            break

        x = x_new

    print("Starting value:",start)
    print("Root:",x_new)
    print("Iterations:",i+1)
    print("Final error:",error)
    
