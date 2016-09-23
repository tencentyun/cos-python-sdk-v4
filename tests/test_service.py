# -*- coding: utf-8 -*-

from unittest import TestCase


from qcloud_cos import CosClient
from qcloud_cos import UploadFileRequest
from qcloud_cos import UploadSliceFileRequest
from qcloud_cos import UpdateFileRequest
from qcloud_cos import UpdateFolderRequest
from qcloud_cos import DelFileRequest
from qcloud_cos import DelFolderRequest
from qcloud_cos import CreateFolderRequest
from qcloud_cos import StatFileRequest
from qcloud_cos import StatFolderRequest
from qcloud_cos import ListFolderRequest

import json

class TestCosService(TestCase):

    def setUp(self):
        appid = 10055004  # 替换为用户的appid
        secret_id = u''  # 替换为用户的secret_id
        secret_key = u''  # 替换为用户的secret_key
        self.cos_client = CosClient(appid, secret_id, secret_key)

        self.bucket = u''


    def tearDown(self):
        pass

    def testUploadFile(self):
        # create local file
        with open('localfile.txt', 'w') as f:
            f.write("hello world")

        # upload local file
        request = UploadFileRequest(self.bucket, u'/sample_file_for_upload.txt', u'localfile.txt')
        ret = self.cos_client.upload_file(request)

        self.assertEqual(ret[u'code'], 0, str(ret))

        # clean environment
        import os
        os.remove('localfile.txt')
        request = DelFileRequest(self.bucket, u'/sample_file_for_upload.txt')
        ret = self.cos_client.del_file(request)

        self.assertEqual(ret[u'code'], 0, str(ret))


if __name__ == '__main__':
    import unittest
    unittest.main()
