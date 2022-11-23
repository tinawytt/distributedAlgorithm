#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis
import json


class Redis:
    """

    """

    settings = {
        "host": "localhost",
        "port": 6379,
        "db": 0
    }

    def __init__(self, config=None):
        self.config = config if config else self.settings

        self.rds = redis.StrictRedis(**self.config)

    def get(self, key):
        return self.rds.get(key)

    def set(self, key, value):
        self.rds.set(key, value)
        # print(value)
        # print('------')


    def remove(self, key):
        self.rds.delete(key)

    def keys(self):
        return self.rds.keys()

    @property
    def empty(self):
        return self.rds.dbsize() == 0
