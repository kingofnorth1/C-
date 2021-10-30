# _*_ coding:utf-8 -*-
# 开发人员：&杜乾坤
# 开发工具：&pycharm
import seaborn as sns
import matplotlib.pyplot as plt

dia = sns.load_dataset("diamonds",data_home="seaborn-data",cache=True) #引用数据

sns.scatterplot(x=dia['x'],y=dia['y'],size=5) #绘制散点图
plt.show()