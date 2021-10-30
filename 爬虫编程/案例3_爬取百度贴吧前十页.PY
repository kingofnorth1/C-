# _*_ coding:utf-8 -*-
# 开发人员：&杜乾坤
# 开发工具：&pycharm
import requests, os

base_url = 'https://tieba.baidu.com/f?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
}
dirname = './案例集合/03/'
if not os.path.exists(dirname):#判断文件是否存在
    os.makedirs(dirname)#创建文件目录
for i in range(0, 10):
    params = {
        'kw': '美女吧',
        'ie': 'utf-8',
        'pn': str(i * 50)
    }
    response = requests.get(url=base_url, headers=headers, params=params)
    with open(dirname + '美女第%s页.html' % (i+1), 'w', encoding='utf-8') as file:
        file.write(response.content.decode('utf-8'))