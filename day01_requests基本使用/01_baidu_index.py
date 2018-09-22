"""
    需求：通过requests向百度首页发送请求，获取百度首页的数据
"""

import requests

# 目标url
url = 'http://www.baidu.com'

# 发起请求获得响应结果
response = requests.get(url)
response.encoding = 'utf-8'
# # 打印响应内容
# print(response.text)
# print(response.encoding)

print(len(response.text))
with open('baidu_index_with_no_requests_header.html','w') as f:
    f.write(response.text)



