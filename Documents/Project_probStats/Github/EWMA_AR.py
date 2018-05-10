import numpy as np
import csv
import copy
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

def EWMA(Data,alpha,year):
	actual_Data = Data
	error=0
	predicted_Data=[0 for i in range(5)]
	for i in range(21,26):
		# print i
		if i==21:
			predicted_Data[i+1-22] = alpha*(float(actual_Data[i])) + (1-alpha)*(float(actual_Data[i]))
		else:
			predicted_Data[i+1-22] = alpha*(float(actual_Data[i])) + (1-alpha)*(float(predicted_Data[i-22]))
		error+=100.0*abs(predicted_Data[i+1-22]-float(actual_Data[i+1]))/(1.0*float(actual_Data[i+1]))
		# print actual_Data
	# print error
	error/=5.0
	print actual_Data[25]
	print (predicted_Data)
	print error
	plt.xlabel('Years', fontsize=10)
	plt.ylabel('Population (in hundred-millions)', fontsize=10)
	plt.plot(year[len(year)-5:],map(float,actual_Data[22:]),label="Actual")
	plt.plot(year[len(year)-5:],predicted_Data,label="Predicted")
	plt.legend(loc='upper left', prop={'size': 10})
	plt.show()

def Seasonal(Data,season):
	actual_Data = Data
	error=0
	predicted_Data=[0 for i in range(5)]
	for i in range(21,26):
		predicted_Data[i+1-22] = actual_Data[i-4]
		error+=100.0*abs(predicted_Data[i+1-22]-actual_Data[i+1])/(1.0*actual_Data[i+1])
	error/=5.0
	print error
	plt.plot(actual_Data[22:])
	plt.plot(predicted_Data)
	plt.show()

def AR(Data,p,year):
	actual_Data=Data
	error=0
	predicted_Data=[]
	p-=1
	for j in range(5):
		M = []
		X=[]
		Y=[]
		for i in range(len(Data)-5-p+j):
			x=copy.deepcopy(actual_Data[i:p+i])
			#X=X[::-1]
			y=actual_Data[p+i]
			X.append(x)
			Y.append(y)
		# X = sm.add_constant(X)
		results=sm.OLS(Y,X).fit()
		xx=[a*b for a,b in zip(results.params,actual_Data[len(Data)-5-p+j:len(Data)-5+j])]
		# print sum(xx)
		predicted_Data.append(sum(xx))
		error+=100.0*abs(sum(xx)-actual_Data[len(Data)-5+j])/(1.0*actual_Data[len(Data)-5+j])
	
	#plt.figure('Cumulative Distribution')
	plt.xlabel('Years', fontsize=10)
	plt.ylabel('Population (in hundred-millions)', fontsize=10)
	plt.plot(year[len(year)-5:],predicted_Data,label="Predicted")
	plt.plot(year[len(year)-5:],actual_Data[len(Data)-5:],label="Actual")
	plt.legend(loc='upper left', prop={'size': 10})

	#plt.plot(actual_Data[len(Data)-5:])

	print "error.....",error/5.0
	# plt.title('AR, Order p = %s, Error = %s'%(p,error/5.0))
	plt.show()
	print year[len(year)-5:], len(year[len(year)-5:])
	print predicted_Data, len(predicted_Data)
	# print len(Y)
	# print predicted_Data
	year.append(2017)
	year.append(2018)
	year.append(2019)
	year.append(2020)
	new_data = list(actual_Data)
	for j in range(4):
		xx=[a*b for a,b in zip(results.params,new_data[len(Data)-p+j:len(Data)+j])]
		new_data.append(sum(xx))
	print new_data,len(new_data),len(year)
	plt.plot(year,new_data,label="Predicted")
	plt.xlabel('Years', fontsize=10)
	plt.ylabel('Population (in hundred-millions)', fontsize=10)
	plt.ylim(0,1.5*max(new_data))
	plt.legend(loc='upper left', prop={'size': 10})	
	plt.show()

X = '/Users/shrinand/Documents/Project_probStats/probs-time_data_year.csv'
data = list(csv.reader(open(X)))
# print len(data),len(data[0])

new_data=data[1:]
# print new_data

zipped = zip(*new_data)
# print map(int,zipped[0])
column=4
alpha=0.8

EWMA(zipped[column],alpha,map(int,zipped[0]))	
AR(map(int,zipped[column]),3,map(int,zipped[0]))


