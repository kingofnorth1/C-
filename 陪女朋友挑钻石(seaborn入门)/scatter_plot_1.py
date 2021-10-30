# _*_ coding:utf-8 -*-
# 开发人员：&杜乾坤
# 开发工具：&pycharm
import seaborn as sns
import matplotlib.pyplot as plt
dia = sns.load_dataset("diamonds",data_home="seaborn-data",cache=True)# 引用文件夹seaborn-data里面diamods数据
f,ax = plt.subplots(figsize=(6.5,6.5))# 这个简化版就是前面fig = plt.figure() ax = fig.add_subplot(111)
sns.set_theme(style="whitegrid")# 设置多个主题参数style
sns.despine(f,left=True,bottom=True)# 隐藏左和下的线条
clarity = ["I1","SI2","SI1","VS2","VS1","VVS2","VVS1","IF"]
sns.scatterplot(x="carat",y="price",hue="clarity",size="depth",palette="ch:rot=-.2,d=.3_r",style_order=clarity,sizes=(1,10),linewidth=0,data=dia,ax=ax)# 绘制散点图
plt.show()# 绘制图片