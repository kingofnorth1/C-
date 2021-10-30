# _*_ coding:utf-8 -*-
# 开发人员：&杜乾坤
# 开发工具：&pycharm
import seaborn as sns
import matplotlib.pyplot as plt
dia = sns.load_dataset("diamonds",data_home="seaborn-data",cache=True)
sns.jointplot(data=dia,x="carat",y="price",xlim=(0,3),ylim=(0,17500),ratio=10,kind='hex',color="#4CB391")
sns.jointplot(data=dia,x="carat",y="price",hue='cut',xlim=(0,3),ylim=(0,17500),ratio=10,marker='.')# 绘制双变量关系图-jointplot
plt.show()