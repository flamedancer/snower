# -*- coding: utf-8 -*-

routes = (
    ('/', 'views.user.login', 'get'),
    ('/admin/print', 'views.admin.printno', ['get', 'post']),
)
