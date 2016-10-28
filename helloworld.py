#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    helloworld.py

    :copyright: (c) 2016 by toni
    :license: see LICENSE for more details.
"""
from tryton.model import ModelSQL, ModelView, fields

__all__ = ['HelloWorld']


class HelloWorld(ModelSQL, ModelView):
    "Hello World"

    __name__ = "hello.world"

    name = fields.char("Name", required=True)
        