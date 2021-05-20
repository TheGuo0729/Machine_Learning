# -*- coding: utf-8 -*-
# @Time    : 2021/5/20 14:16
# @Author  : Guoji
# @Email   : Guojinjia0729@Gmail.com
# @File    : xianxingdanyuan.py


#线性单元 ————直线拟合（平面拟合）——回归
#https://cloud.tencent.com/developer/article/1056098

import numpy as np
np.seterr(invalid='ignore')

"""
我们假设有一个员工，在一个公司上班
现在的他想知道 在这里干多少年可以年薪百万成为人生赢家？
于是他统计了一个数据
分别是 工作时长  头秃数据 （1-10  10表示头发最少） 和 年薪
现在来预测一下
（其实就是一种线性回归的求法，只是交给计算机做了（迭代过程不用人去算了））
年薪数据 单位是 w
"""

input_vector = np.array([[15, 10], [17, 8], [25, 1]])
output_result = np.array([130, 180, 80])

"""
现在开始用预测
"""

#初始化w,b
w = np.array([0, 0], np.int64)
b = 0

#算出第一波的y值
x, y = input_vector.shape
label = np.zeros([3], np.int64)
for i in range(x):
    label[i] = np.dot(input_vector[i], w) + b
#print(label)

rate = 0.0001
"""
在线性单元中，rate就是每次朝梯度方向步进的大小
如果过大 将得不到很好的收敛，会非常离谱的大小摇摆
如果过小 迭代次数会无限延长
"""

#在线性单元中，需要我们自己设置 迭代次数
iteration = 50
times = 1
sum_1 = np.array([[0, 0], [0, 0], [0, 0]])
sum_2 = np.array([[0, 0], [0, 0], [0, 0]])
while times < iteration:
    for k in range (3):
        sum_1[k] = (output_result[k] - label[k]) * input_vector[k,:]
        sum_2[k] = output_result[k] - label[k]
    w = w + rate * np.sum(sum_1)
    b = b + rate * np.sum(sum_2)
    #print(w)
    #print(b)
    for j in range(3):
        label[j] = np.dot(input_vector[j], w) + b
    times = times + 1
    #print(label)

years = eval(input('你打算干几年？'))
hairs = eval(input('想不想要头发？(1：全在 10：全秃)'))

your_vec = np.array([years, hairs])
your_money = np.dot(your_vec, w) + b
print('看好了，这是你一年能拿的钱：{:.3f}W'.format(your_money))