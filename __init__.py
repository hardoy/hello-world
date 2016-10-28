# -*- coding: utf-8 -*-
"""
    __init__.py

    :copyright: (c) 2016 by toni
    :license: see LICENSE for details.
"""
from trytond.pool import Pool

from helloworld import HelloWorld

def register():
    Pool.register(
        HelloWorld,
        module='helloworld', type_='model'
    )
