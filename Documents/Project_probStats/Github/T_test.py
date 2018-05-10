import numpy as np
import operator
import math
import scipy.stats as stats
import itertools
import scipy.special as scsp

def paired_t(X,Y):

	D = map(operator.sub, X, Y)
	mean_D = np.mean(D)
	var_D = np.var(D)
	sd_D = var_D**0.5

	T = mean_D * (len(X)**0.5) / sd_D

	print "T stat ",abs(T) 
	print "p value ", 1 - 0.5 * (1 + scsp.erf(abs(T)))


X = np.genfromtxt('/Users/shrinand/Documents/Project_probStats/white_poverty.csv',delimiter='\n')
Y = np.genfromtxt('/Users/shrinand/Documents/Project_probStats/black_poverty.csv',delimiter='\n')


# paired_t(X,Y)




