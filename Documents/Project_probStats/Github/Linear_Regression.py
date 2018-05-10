import numpy as np
import csv
import matplotlib.pyplot as plt
import stat
import math
import statsmodels.api as sm

Data = np.genfromtxt('/Users/shrinand/Documents/Project_probStats/lreg.csv',delimiter=',')
X=[]
pX=[]
Y=[]
for tuple_ in Data:
	X.append(tuple_[0])
	Y.append(tuple_[1])
	pX.append(tuple_[0])						


X = sm.add_constant(X)

results=sm.OLS(Y,X).fit()
# print X
res= results.params

SSE=0
MAPE=0

Y_hat=[]

for tuple_ in Data:
	y_hat=res[0]+res[1]*tuple_[0]
	Y_hat.append(y_hat)
	
	SSE+=(y_hat-tuple_[1])**2
	MAPE+= abs((y_hat-tuple_[1])/float(tuple_[1]))*100
MAPE/=len(Data)
print "SSE: ",SSE,"MAPE: ",MAPE

plt.plot(pX,Y_hat)
# plt.plot(X,Y)
plt.scatter(pX,Y)

plt.show()
