# -*- coding: utf-8 -*-

import json
import importlib
import http_request


class HttpResponse(object):
    http_header = '''\
HTTP/1.1 200 OK
Server: snower version 1.0
Content-Type: {context_type}; charset=UTF-8
Context-Length: {context_length} \n\n {context}\n\n'''
    def __init__(self):
        self.routes = {}
        self.init_routes()

    def init_routes(self):
        from urls import routes
        for route, func_path, methods in routes:
            if not isinstance(methods, list):
                methods = [methods] 
            print func_path
            modual, func_name = func_path.rsplit('.', 1)
            func = getattr(importlib.import_module(modual), func_name)
            self.routes[route] = {
                'func': func,
                'methods': methods, 
            }

    def get_response(self, context_type='text/html'):
        path = http_request.request.path
        method = http_request.request.method.lower()
        print "this method", method, "usable methods", self.routes 
        if path not in self.routes:
            return "can't find suited function"
        if method not in self.routes[path]['methods']:
            return "function cannot support this method"
        return_data = self.routes[path]['func']()
        if isinstance(return_data, dict):
            return_data = json.dumps(return_data)
        elif isinstance(return_data, int):
            return_data = str(return_data)
        # how to do with unicode?
        # elif instance(return_data, [str, unicode])
        elif isinstance(return_data, (tuple, list)):
            return_data.dumps(list(return_data))
        print ">>> this response", return_data
        return self.http_header.format(**{
            'context_type': context_type,
            'context_length': len(return_data),
            'context': return_data,
        })
        
