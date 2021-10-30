# _*_ coding:utf-8 -*-
# 开发人员：&杜乾坤
# 开发工具：&pycharm
import re,os
import requests

respose = requests.get('http://www.xiaohuar.com/v/')
#print(respose.status_code)# 响应的状态码
#print(respose.content)# 返回字节信息
#print(respose.text)# 返回文本信息
urls = re.findall(r'class="items".*?href="(.*?)"',respose.text,re.S)
#url = urls[0]
result = requests.get(urls)
mp4_url=re.findall(r'id="media".*?src="(.*?)"',result.text,re.S)[0]

video = requests.get(mp4_url)

dirname = './校花网/基础版/'
if not os.path.exists(dirname):
    os.makedirs(dirname)

with open(dirname+'校花.mp4','wb') as f:
    f.write(video.content)