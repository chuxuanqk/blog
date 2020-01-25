# -*- coding:utf-8 -*-

import numpy as np
import sys, os

sys.path.append(os.pardir)             # 为导入父目录中的文件而进行的设定


# 激活函数
class Activation(object):
    def __init__(self):
        pass

    def step_function(self, x):
        y = x > 0
        return y.astype(np.int)

    def sigmoid(self, x):
        return 1/(1 + np.exp)

    def relu(self, x):
        return np.maximum(0, x)

    def softmax(self, a):
        c = np.max(a)
        exp_a = np.exp(a - c)
        sum_exp_a = np.sum(exp_a)
        y = exp_a / sum_exp_a

        return y
