#n = number of significant figures

#and returns: Es = 0.5 × 102−n%

#Test: n = 3, 4, 5, 6

def accuracy(n):
    Es = 0.5 * 10**(2-n)
    return Es
for n in [3,4,5,6]:
    print("n = ",n,"Error = ",accuracy(n),"%")

#n =  3 Error =  0.05 %
#n =  4 Error =  0.005 %
#n =  5 Error =  0.0005 %
#n =  6 Error =  5e-05 %
