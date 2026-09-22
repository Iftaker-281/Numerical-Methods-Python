#Derivative Based Solver
#f(x) = x**3 − x − 1
def f(x):
    return x**3 - x - 1
def df(x):
    return 3*x**2-1
x0 = 1
x1 = 2
print(f(x0),f(x1))
mid = (x0+x1)/2
Es = 0.0001

for i in range (20):
    mid_new = mid - f(mid)/df(mid)
    error = abs(mid_new - mid_old)

    print("Iteration = ",i+1,"Error = ",error,"x_new = ",mid_new)

    Er = abs((mid_new-mid)/mid_new)*100

    if Er<Es:
        break
    mid = mid_new
print("Root: ",round(mid_new,4))
print("total iteration: ",i+1)
