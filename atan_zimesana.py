# -*- coding: utf-8 -*-
#include<math.h>

import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import tan, linspace

x = linspace(0,4,101)
y=tan(x)*-tan(x)

from matplotlib import pyplot as plt
plt.grid()
plt.plot(x,y,'go')
plt.show()
