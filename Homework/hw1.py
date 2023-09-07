import numpy as np
import numpy.linalg as la
import math
import matplotlib.pyplot as plt

def problem1():
	x = np.linspace(1.920,2.080,161)
	p1 = lambda x : (x-2)**9
	p2 = lambda x : x**9 - 18*x**8 + 144*x**7 - 672*x**6 + 2016*x**5 - 4032*x**4 + 5376*x**3 - 4608*x**2 + 2304*x - 512
	y = p1(x)
	z = p2(x)
	plt.plot(x,y)
	plt.plot(x,z)
	plt.show()

problem1()