from tabulate import tabulate
from math import sqrt

result = []

for x in range(1, 21):
	x_sqrt = sqrt(x)
	x_cube = x ** (1. / 3.)
	result.append([x, x_sqrt, x_cube])

print(tabulate(result, headers=['x', '√x', '∛x']))
