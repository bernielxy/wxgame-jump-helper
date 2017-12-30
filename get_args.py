# coding:utf-8

# 感谢 悠望南山 的代码 原文链接: https://www.cnblogs.com/NanShan2016/p/5493429.html

###最小二乘法试验###
import numpy as np
from scipy.optimize import leastsq

data = np.loadtxt('output.txt', delimiter=',')

distance_list = [item[0] for item in data]

time_list = [item[1] for item in data]

###采样点(Xi,Yi)###

# Xi = np.array(distance_list) * 2  #  因为页面里用的图片是实际截图的 二分之一

# Yi = np.array(time_list)

Xi=np.array([96,84, 82, 115, 73, 89, 59, 87, 121, 96, 95, 77, 43, 73, 80]) * 3 / 2

Yi=np.array([550,600,600,660,600,700,350,650,900,650,640,450,250,450,600]) 

###需要拟合的函数func及误差error###
def func(p,x):
    k,b=p
    return k*x+b

def error(p,x,y,s):
    print s
    return func(p,x)-y #x、y都是列表，故返回值也是个列表

#TEST
p0=[100,2]
#print( error(p0,Xi,Yi) )

###主函数从此开始###
s="Test the number of iteration" #试验最小二乘法函数leastsq得调用几次error函数才能找到使得均方误差之和最小的k、b
Para=leastsq(error,p0,args=(Xi,Yi,s)) #把error函数中除了p以外的参数打包到args中
k,b=Para[0]
print"k=",k,'\n',"b=",b

###绘图，看拟合效果###
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
plt.scatter(Xi,Yi,color="red",label="Sample Point",linewidth=3) #画样本点
x=np.linspace(0,10,1000)
y=k*x+b
plt.plot(x,y,color="orange",label="Fitting Line",linewidth=2) #画拟合直线
plt.legend()
plt.show()
