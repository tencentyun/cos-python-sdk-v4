#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CosConfig(object):
    """CosConfig 有关cos的配置"""

    def __init__(self):
        self._end_point = 'http://sh.file.myqcloud.com/files/v2'
        self._user_agent = 'cos-python-sdk-v4'
        self._timeout = 3
        self._sign_expired = 300

    def set_end_point(self, end_point):
        """设置COS的域名地址

        :param end_point:
        :return:
        """
        self._end_point = end_point

    def get_end_point(self):
        """获取域名地址

        :return:
        """
        return self._end_point

    def get_user_agent(self):
        """获取HTTP头中的user_agent

        :return:
        """
        return self._user_agent

    def set_timeout(self, time_out):
        """设置连接超时, 单位秒

        :param time_out:
        :return:
        """
        assert isinstance(time_out, int)
        self._timeout = time_out

    def get_timeout(self):
        """获取连接超时，单位秒

        :return:
        """
        return self._timeout

    def set_sign_expired(self, expired):
        """设置签名过期时间, 单位秒

        :param expired:
        :return:
        """
        assert isinstance(expired, int)
        self._sign_expired = expired

    def get_sign_expired(self):
        """获取签名过期时间, 单位秒

        :return:
        """
        return self._sign_expired

    def enable_https(self):
        """打开https

        TODO(lc): There is a bug if use had invoked SetEndpoint
        :return:
        """
        self._end_point = 'https://sh.file.myqcloud.com/files/v2'
