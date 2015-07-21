# -*- coding: utf-8 -*-

import http_request

def login():
    params = http_request.request.params
    return "HELLO! {}".format(params.get('name', ''))
