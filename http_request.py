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


def paser_params(params_str):
    params = {}
    key_value_pairs = params_str.split('&')
    for key_value in key_value_pairs:
        key, value = key_value.split('=', 1)
        params[key] = value
    return params 


class HttpRequest(object):
    """ 解析请求
    """
    def __init__(self, request_str):
        self.params = {}

        self.request_info = request_str.split('\n')
        self.method_path_params_httpVersion()
       
    def method_path_params_httpVersion(self):
        method, path_params, self.httpVersion = self.request_info[0].split(' ')
        self.method = method.lower()
        path_params = path_params.split('?', 1)

        self.path = path_params[0]

        if len(path_params) == 2:
            self.path = path_params[0]
            self.params = paser_params(path_params[1])

        if self.method == 'post' and self.request_info[-1]:
            self.params.update(paser_params(self.request_info[-1]))
