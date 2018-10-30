from math import sin

x = 1. * float(input("ievad argument x"))

y = sin(x)
print("sin(%.2f) = %.2f"%(x,y))

a0 = (-1)**0*x**1/(1)
S0 = a0
print("a0 = %.2f S0 = %.2f"%(a0,S0))

a1 = (-1)**0*x**3/(1*2*3)
S1 = a0 + a1
print("a0 = %.2f S1 = %.2f"%(a1,S1))

a2 = (-1)**0*x**5/(1*2*3*4*5)
S2 = a0 + a1 + a2
print("a0 = %.2f S2 = %.2f"%(a1,S2))
