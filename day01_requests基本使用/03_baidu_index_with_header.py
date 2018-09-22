"""
    需求:爬取百度首页时携带header数据

    为什么要携带header？
    模拟浏览器，欺骗服务器，获取与浏览器一样的内容。
"""
import requests

# 百度目标url
url ='http://www.baidu.com'

# 模拟浏览器携带user-agent请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

response = requests.get(url,headers=headers)

# 将编码设置为utf-8
response.encoding = 'utf-8'

print(len(response.text))

with open('baidu_index_with_requests_header.html','w') as f :
    f.write(response.text)


