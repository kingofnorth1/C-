# _*_ coding:utf-8 -*-
# 开发人员：杜乾坤
# 开发工552具：&pycharm
import requests,os
base_url = 'https://www.baidu.com/more/'
response = requests.get(base_url)# 获取连接
print(response.text)
print(response.encoding)

response.encoding='utf-8'
print(response.text)

dirname = './案例集合/01/'
if not os.path.exists(dirname):
    os.makedirs(dirname)

with open(dirname+'index.html','w',encoding='utf-8') as fp:# 写入一个html文件
    fp.write(response.content.decode('utf-8'))

print(response.status_code)# http请求的返回状态
print(response.headers)# http响应内容的头部内容
print(type(response.text))# http相应内容的字符串形式
print(type(response.content))# http响应内容的二进制形式