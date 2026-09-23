def f(x):
    return x**3+x-1
def g(x):
    return (1-x)**(1/3)

x0 = 0.5
Es = 0.005
x_old = x0
for i in range(20):
    x_new = g(x_old)
    error = abs(x_new - x_old)
    print("Iteration = ",i+1,"Error = ",error,"New x is: ",x_new)
    if error<Es:
        break
    x_old = x_new
print("Root = ",round(x_new,4))
