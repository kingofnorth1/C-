# _*_ coding:utf-8 -*-
# 开发人员：&杜乾坤
# 开发工具：&pycharm
import requests,os

base_url = 'https://fanyi.baidu.com/sug'

kw = input('请输入要翻译的英文单词:')
data={
    'kw':kw
}
headers = {
    # 由于百度翻译没有反扒措施,因此可以不写请求头
    'content-length':str(len(data)),#在http协议中,content-length用于描述http消息实体的传输长度
    'content-type':'application/x-www-form-urlencoded;charset=UTF-8',#content-type的类型主要是application/json格式
    'refener':'https://fanyi.baidu.com/',#你在访问一个目标网站时，在访问前你的原网站的地址
    'x-requested-with':'XMLHttpRequest'#服务器做简单反爬手段之一,若为XMLHttpRequest,则为Ajax异步请求
}
response = requests.post(base_url,headers=headers,data=data)
result=''
for i in response.json()['data']:
    result+=i['v']+'\n'
print(kw+'的翻译结果为:')
print(result)