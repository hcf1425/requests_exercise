"""
    需求：通过requests向百度首页发送请求，获取百度首页的数据
"""

import requests

# 目标url
url = 'http://www.baidu.com'

# 发起请求获得响应结果
response = requests.get(url)

# 打印响应内容
print(response.text)



