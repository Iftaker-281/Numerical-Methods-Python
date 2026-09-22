#Two Guess Prediction Program
#f(x) = x**2 − 5

#Initial guesses: x0 = 2, x1 = 3

#Stop when: Er(%) < 0.05

#Output format: Iteration, x0, x1, xnew, Error

def f(x):
   return  x**2 - 5
a = 2
b = 3
print(f(a),f(b))

x_prev = a
x_old = b

Es = 0.05

for i in range(20):
    x_new = x_old - f(x_old) * (x_old-x_prev)/(f(x_old) - f(x_prev))
    error = abs((x_new - x_old)/abs(x_new) )* 100
    print("Iteration = ",i,"x0 = ",x_prev,"x1 = ",x_old,"x_new = ",x_new,"Error = ",error)
    if error<Es:
        break
    x_prev = x_old
    x_old = x_new
print("Root: ",round(x_new,4))
print("Total iteration: ",i+1)
