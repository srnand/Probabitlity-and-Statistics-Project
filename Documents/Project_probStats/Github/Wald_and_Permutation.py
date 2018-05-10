import numpy as np
import operator
import math
import scipy.stats
import scipy.special as scsp

l=[]
ans=[]
counter=1000000
left=[]
right=[]

def wald(X,Y):
	sample_mean_X = np.mean(X)
	sample_mean_Y = np.mean(Y)

	sample_var_X = np.var(X)
	sample_var_Y = np.var(Y)

	#print mean_D/(sd_D)

	print sample_var_Y

	standard_error = ((sample_var_X+sample_var_Y)/len(X))**0.5

	W = ( sample_mean_X - sample_mean_Y ) / standard_error
	print standard_error
	print "W stat ",abs(W)
	print "p value ", 1 - 0.5 * (1 + scsp.erf(abs(W) / np.sqrt(2)))

	print "95 % CI ",sample_mean_X - sample_mean_Y - 1.96*(standard_error), sample_mean_X - sample_mean_Y + 1.96*(standard_error)

def permute(a):
	global l
	global ans
	global left
	global right
	if len(ans)>=counter:
 		return
	if len(a)==1:
 		l.append(a[0])
 		inte = left + l +right
	 	ans.append(inte)
 		#ans.append(l)
 		l = l[:-1]
 		return
	for i in range(len(a)):
		l.append(a[i])
		permute(a[:i]+a[i+1:])
 		l = l[:-1]

def mid_permute(a):
	global left
	global right
	if len(ans)>=counter:
 		return
	for i in range(len(a)/2):
		left = a[:len(a)/2 - i -1]
		right = a[-len(a)/2 +i +1: ]

		permute (a[len(a)/2 - i -1:-len(a)/2 +i +1 ])

def cal_p(T_obs):
	count =0

	for i in ans:
		x = list(i[:len(i)/2 ])
		y = list(i[len(i)/2 :])
		#print x,y
		T_i = abs(np.mean(x) - np.mean(y))
		#print T_i
		if T_i > T_obs : 
			#print "yo"
			count+=1
	print "total count : " ,count
	count = count / float(len(ans))
	print "p value : " , count

def permute_test():
	sample_mean_X = np.mean(X)
	sample_mean_Y = np.mean(Y)
	T_obs = math.fabs(sample_mean_X - sample_mean_Y)
	Z = sorted(X+Y,reverse=True)
	mid_permute(Z)
	cal_p(T_obs)

# X = [.225, .262, .217, .240, .230, .229, .235, .217, .231, .250]
# Y = [.209, .205, .196, .210, .202, .207, .224, .223, .220, .201]

X1 = np.genfromtxt('/Users/shrinand/Documents/Project_probStats/white_poverty.csv',delimiter='\n')
Y1 = np.genfromtxt('/Users/shrinand/Documents/Project_probStats/black_poverty.csv',delimiter='\n')


X = np.random.choice(X1,10)

mean = 14.59
sd = 5.484287

normal_data = np.random.normal(mean,sd,2819)

Y = np.random.choice(normal_data,10)

# wald(X,Y)

permute_test()


