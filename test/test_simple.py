from qcloud_cos.cos_request import UploadFileRequest

import unittest

class TestRequestCase(unittest.TestCase):

    def test_upload_file_request(self):
        req = UploadFileRequest('bucketname', '/a/b/c.jpg', '/tmp/a.jpg')
        self.assertEqual(req.get_local_path(), '/tmp/a.jpg')
        self.assertEqual(req.get_insert_only(), 1)

