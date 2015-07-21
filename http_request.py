# -*- coding: utf-8 -*-
"""
get 的数据格式:
GET / HTTP/1.1
Host: 127.0.0.1:8010
Connection: keep-alive
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36
Accept-Encoding: gzip, deflate, sdch
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6
Cookie: csrftoken=LMnRuDgJQ5Brni74JWdDDNyPABwp0QUn

post 的数据格式
"""

# 全局单例变量  每次请求的 HttpRequest实例
request = None

class HttpRequest(object):
    """ 解析请求
    """
    def __init__(self, request_str):
        self.request_info = request_str.split('\n')
        self.method, self.path, self.httpVersion = self.method_path_httpVersion()
       
    def method_path_httpVersion(self):
        return self.request_info[0].split(' ')
        
        

    

