# -*- coding: utf-8 -*-
"""
Created on Wed May 19 17:00:49 2021
@author: Guoji
"""

'''
机器学习的第一步，看懂了感知器的原理，自己写一个感知器
https://www.zybuluo.com/hanbingtao/note/433855
'''

import numpy as np
np.seterr(invalid='ignore')

#现在有一个学生
#对他的平时表现和考试成绩打分（5分制）
#学生1（3，3） 学生2（0，2） 学生3（1，2）
#其中学生1通过，打算输出 1
#学生2,3未通过，输出0
# （输出1和输出0可以用分段函数实现）

input_vector = np.array([[3,3],[0,2],[1,2]])
output_result = np.array([1,0,0])

#现在需要一个函数来计算我们对学生打的分
#譬如 y_1 = w*[3,3] + b
#我们把y_1值代入进我们设置的一个分段函数里面
#比如分段函数是 f(y_1>0) = 1 ； f(y_1<0) = 0
#现在的问题是y = w*x + b 如何设置w,b让它在不同分数时大于0，小于0

#初始化w,b
w = np.array([0,0],np.int64)
b = 0

#算出第一波的y值
x,y = input_vector.shape
label = np.zeros([3],np.int64)
for i in range(x) :
    label[i] = np.dot(input_vector[i,:] , w) + b

#定义分段函数
def judgement(x) :
    if x > 0 :
        return 1
    else :
        return 0

rate = 0.5 #学习速率
#这个rate非常非常重要，重要到你取不同的值，会不会有解，解的具体个数是多少
#但我仍然不知道这个rate怎么取
#rate应该也是需要迭代的，不断改变才对


#不满足条件就开始迭代
cor = 1
while cor == 1 :
    if judgement(label[0]) != 1 :
        w = w + rate * ( output_result[0] - label[0]) * input_vector[0,:]
        b = b + rate * ( output_result[0] - label[0])

    elif judgement(label[1]) != 0 :
         w = w + rate * ( output_result[1] - label[1]) * input_vector[1,:]
         b = b + rate * ( output_result[1] - label[1])

    elif judgement(label[2]) != 0 :
        w = w + rate * ( output_result[1] - label[1]) * input_vector[1,:]
        b = b + rate * ( output_result[1] - label[1])

    else:
        cor = 0
        continue
    for o in range(x) :
            label[o] =  np.dot(input_vector[o,:] , w) + b

else:
    print('权重w的值是')
    print(w)
    print('常量b的值是{:.2f}'.format(b))
