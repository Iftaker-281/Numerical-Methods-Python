function = input("Enter Function: ")

def f(x):
  return eval(function)
a = float(input("Enter a:"))
b = float(input("Enter b: "))
rounds = 20
tolerance = 0.005
mid_old = 0

for i in range(rounds):
  mid = (a+b)/2
  if i>0:
    error = abs(mid-mid_old)
    print("iteration: ",i,"a = ",a,"b = ",b,"mid = ",mid,"Error = ",error)
    Er = abs((mid-mid_old)/mid)*100
    if Er<tolerance:
      break
    if f(a) * f(mid)<0:
      b = mid
    else:
      a = mid
    mid_old = mid
print("Root = ",mid)


