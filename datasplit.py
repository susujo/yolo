# -*- coding:utf-8 -*-
# 将一个文件夹下图片按比例分在两个文件夹下，比例改0.7这个值即可
import os
import random
import shutil
from shutil import copy2

# 原图片位置
trainfiles = os.listdir('F:/研究生/images/train')  # （图片文件夹）
labelfiles = os.listdir('F:/研究生/labels/train')  # （标签文件夹）
num_train = len(labelfiles)
print("num_train: " + str(num_train))
# 获取列表
index_list1 = list(range(num_train))
index_list2 = list(range(num_train))
print(index_list1)
print(index_list2)
# 设置相同的随机数种子，打乱图片顺序
randnum = random.randint(0, 20000)
random.seed(randnum)
random.shuffle(index_list1)
random.seed(randnum)
random.shuffle(index_list2)
num = 0
trainDir = 'F:/数据集/valid/images'  # （将图片文件夹中的8份放在这个文件夹下）
#validDir = 'F:/数据集/valid/images'  # （将图片文件夹中的2份放在这个文件夹下）

trainlabelDir = 'F:/数据集/valid/labels'
#validlabelDir = 'F:/数据集/valid/labels'

# 随机放入
for i in index_list1:
    fileName1 = os.path.join('F:/研究生/images/train', trainfiles[i])
    fileName2 = os.path.join('F:/研究生/labels/train', labelfiles[i])

    if num < num_train * 0.4:
        print(str(fileName2))
        copy2(fileName2, trainlabelDir)
        copy2(fileName1, trainDir)
    #else:
        #copy2(fileName2, validlabelDir)
        #copy2(fileName1, validDir)
    num += 1
