import sys
sys.path.append("/usr/local/anaconda3/lib/python3.6/site-packages")
import numpy

from numpy import *     # Importē skaitlisko metožu bibliotēkas funkcijas
x = linspace(0, 4, 70)  # Trešais arguments ir ģenerējamo elementu skaits
y = sin(x)



from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $cos(x)$')
plt.plot(x, y, color = "#000080")  
y1 = x
plt.plot(x, y1, color = "#FFFF00")  
y2 = y1 - x*x*x/(1*2*3)
plt.plot(x, y2, color = "#00FFFF")  
y3 = y2 + x*x*x*x*x/(1*2*3*4*5)
plt.plot(x, y3, color = "#800080")  
y4 = y3 + x*x*x*x*x*x*x/(1*2*3*4*5*6*7)
plt.plot(x, y4, color = "#000000")  
plt.show()
