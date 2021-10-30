# _*_ coding:utf-8 -*-
# 开发人员：&杜乾坤
# 开发工具：&pycharm
import requests,os
base_url = 'https://search.sina.com.cn/'
headers = {
    'user-agent':'Mozilla/5.0(Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
key = '孙悟空'
params = {
    'q':key,
    'c':'news',
    'from':'channel',
    'ie':'utf-8',
}
dirname = './案例集合/02/'
if not os.path.exists(dirname):
    os.makedirs(dirname)

response = requests.get(base_url,headers=headers,params=params)# url:需要抓取的url地址，headers:请求头，params:查询参数
with open(dirname+'sina_news.html','w',encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))