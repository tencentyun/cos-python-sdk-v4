#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import random
import time
import hmac
import hashlib
import binascii
import base64

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

from qcloud_cos.helper import smart_str, smart_bytes


class Auth(object):

    def __init__(self, cred):
        self.cred = cred

    def app_sign(self, bucket, cos_path, expired, upload_sign=True):
        appid = self.cred.get_appid()
        bucket = smart_str(bucket)
        secret_id = smart_str(self.cred.get_secret_id())
        now = int(time.time())
        rdm = random.randint(0, 999999999)
        cos_path = quote(smart_str(cos_path), '~/')
        if upload_sign:
            fileid = '/%s/%s%s' % (appid, bucket, cos_path)
        else:
            fileid = cos_path

        if expired != 0 and expired < now:
            expired = now + expired

        sign_tuple = (appid, secret_id, expired, now, rdm, fileid, bucket)

        plain_text = 'a=%s&k=%s&e=%d&t=%d&r=%d&f=%s&b=%s' % sign_tuple
        secret_key = smart_str(self.cred.get_secret_key())
        sha1_hmac = hmac.new(smart_bytes(secret_key),
                             smart_bytes(plain_text),
                             hashlib.sha1)
        hmac_digest = sha1_hmac.hexdigest()
        hmac_digest = binascii.unhexlify(hmac_digest)
        sign_hex = hmac_digest + smart_bytes(plain_text)
        sign_base64 = base64.b64encode(sign_hex)
        return sign_base64

    def sign_once(self, bucket, cos_path):
        """单次签名(针对删除和更新操作)

        :param bucket: bucket名称
        :param cos_path: 要操作的cos路径, 以'/'开始
        :return: 签名字符串
        """
        return self.app_sign(bucket, cos_path, 0)

    def sign_more(self, bucket, cos_path, expired):
        """多次签名(针对上传文件，创建目录, 获取文件目录属性, 拉取目录列表)

        :param bucket: bucket名称
        :param cos_path: 要操作的cos路径, 以'/'开始
        :param expired: 签名过期时间, UNIX时间戳, 如想让签名在30秒后过期, 即可将expired设成当前时间加上30秒
        :return: 签名字符串
        """
        return self.app_sign(bucket, cos_path, expired)

    def sign_download(self, bucket, cos_path, expired):
        """下载签名(用于获取后拼接成下载链接，下载私有bucket的文件)

        :param bucket: bucket名称
        :param cos_path: 要下载的cos文件路径, 以'/'开始
        :param expired:  签名过期时间, UNIX时间戳, 如想让签名在30秒后过期, 即可将expired设成当前时间加上30秒
        :return: 签名字符串
        """
        return self.app_sign(bucket, cos_path, expired, False)
