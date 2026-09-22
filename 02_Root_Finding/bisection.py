def f(x):
    return x**3-4*x-9
a = float(input("Enter lower limit: "))
b = float(input("Enter uper limit: "))
n = 4
Es = 0.5 * 10**(2-n)
rounds = 15
mid_old = 0
for i in range(rounds):
    mid = (a+b)/2
    if i>0:
      error = abs(mid - mid_old)
      print("Iteration = ",i,"xl = ",a,"xu = ",b,"xr = ",mid,"Error = ",error)
      Er = abs ((mid - mid_old)/mid)*100
      if Er<Es:
          break
    if f(a) * f(mid) < 0:
       b = mid
    else:
       a = mid
    mid_old = mid
    
