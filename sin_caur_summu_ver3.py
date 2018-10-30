from math import sin

x = float(input("ievad argument x:"))

y = sin(x)
print("sin(%.2f) = %.2f"%(x,y))

a = (-1)**0*x**1/(1)
S = a
print("a = %.2f S0 = %.2f"%(a,S))

a = (-1)**0*x**3/(1*2*3)
S = S + a
print("a = %.2f S1 = %.2f"%(a,S))

a = (-1)**0*x**5/(1*2*3*4*5)
S = S + a
print("a = %.2f S2 = %.2f"%(a,S))
