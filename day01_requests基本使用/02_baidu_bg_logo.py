"""
    需求：爬取百度网站首页的图片
"""

import requests

# 图片url
url = 'http://www.baidu.com/img/bd_logo1.png'

response = requests.get(url)

# 上下文管理器
with open('baidu_bg_logo.png','wb') as f:
    # 写入二进制的图片
    f.write(response.content)