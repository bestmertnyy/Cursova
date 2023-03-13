import matplotlib.pyplot as plt
from pprint import pprint
from math import log, exp, gamma, floor
import numpy as np

n = int(input(('n:')))
matr = [[] for i in range(n)]
with open('1.txt') as file:
    for i in range(n):
        matr[i] = [float(t) for t in file.readline().split()]


#yy
yy= [[] for i in range(n)]
for i in range(n):
    yy[i]=matr[i][1]

#сума у
Ysum = 0
for i in range(n):
    Ysum = Ysum + matr[i][1]

#сума х
Xsum = 0
for i in range(n):
    Xsum = Xsum + matr[i][0]

#x^2
x2= [[] for i in range(n)]
for i in range(n):
    x2[i]=matr[i][0]**2

#сума x^2
x2sum=0
for i in range(n):
    x2sum = x2sum + x2[i]

#xiyi
xiyi= [[] for i in range(n)]
for i in range(n):
    xiyi[i]=matr[i][0]*matr[i][1]

#сумаxiyi
xiyisum = 0
for i in range(n):
    xiyisum = xiyisum + xiyi[i]


a= (n*xiyisum-Xsum*Ysum)/(n*x2sum-Xsum*Xsum)

b=(Ysum*x2sum-Xsum*xiyisum)/(n*x2sum-Xsum*Xsum)

y= [[] for i in range(n)]
for i in range(n):
    y[i]=b+a*matr[i][0]

plt.plot(yy,label='Середньорічна температура')
plt.plot(y,label='Лінія регресії')

plt.grid()
plt.legend()
plt.show()

print(matr)
print(Ysum)
print(Xsum)
print(x2)
print(x2sum)
print(xiyi)
print(xiyisum)
print(a)
print(b)
print(y)