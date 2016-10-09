#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

import logging
import sys
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

logger = logging.getLogger(__name__)

def cos_demo():
    # 设置用户属性, 包括appid, secret_id和secret_key
    # 这些属性可以在cos控制台获取(https://console.qcloud.com/cos)
    appid = 111               # 替换为用户的appid
    secret_id = u''         # 替换为用户的secret_id
    secret_key = u''         # 替换为用户的secret_key
    region = "shanghai" #           # 替换为用户的region，目前可以为 shanghai/guangzhou
    cos_client = CosClient(appid, secret_id, secret_key, region)

    # 设置要操作的bucket
    bucket = u''

    ############################################################################
    # 文件操作                                                                 #
    ############################################################################
    # 1. 上传文件(默认不覆盖)
    #    将本地的local_file_1.txt上传到bucket的根分区下,并命名为sample_file.txt
    #    默认不覆盖, 如果cos上文件存在,则会返回错误

    request = UploadFileRequest(bucket, u'/sample_file.txt', u'local_file_1.txt')
    upload_file_ret = cos_client.upload_file(request)

    logger.info("upload file, return message: " + str(upload_file_ret))

    #  分片上传大文件

    request = UploadSliceFileRequest(bucket, u'/sample_bigfile.txt', u'local_bigfile.txt')
    ret = cos_client.upload_slice_file(request)
    logger.info("slice upload, return message: " + str(ret))

    # 2. 上传文件(覆盖文件)
    #    将本地的local_file_2.txt上传到bucket的根分区下,覆盖已上传的sample_file.txt
    with open('local_file_2.txt', 'w') as f:
        f.write("hello world2")
    request = UploadFileRequest(bucket, u'/sample_file.txt', u'local_file_2.txt')
    request.set_insert_only(0)  # 设置允许覆盖
    upload_file_ret = cos_client.upload_file(request)
    logger.info('overwrite file, return message:' + str(upload_file_ret))

    # 3. 获取文件属性
    request = StatFileRequest(bucket, u'/sample_file.txt')
    stat_file_ret = cos_client.stat_file(request)
    logger.info('stat file, return message: ' + str(stat_file_ret))

    # 4. 更新文件属性
    request = UpdateFileRequest(bucket, u'/sample_file.txt')

    request.set_biz_attr(u'这是个demo文件')           # 设置文件biz_attr属性
    request.set_authority(u'eWRPrivate')              # 设置文件的权限
    request.set_cache_control(u'cache_xxx')           # 设置Cache-Control
    request.set_content_type(u'application/text')     # 设置Content-Type
    request.set_content_disposition(u'ccccxxx.txt')   # 设置Content-Disposition
    request.set_content_language(u'english')          # 设置Content-Language
    request.set_x_cos_meta(u'x-cos-meta-xxx', u'xxx')  # 设置自定义的x-cos-meta-属性
    request.set_x_cos_meta(u'x-cos-meta-yyy', u'yyy')  # 设置自定义的x-cos-meta-属性

    update_file_ret = cos_client.update_file(request)
    logger.info('update file,  return message: ' + str(update_file_ret))

    # 5. 更新后再次获取文件属性
    request = StatFileRequest(bucket, u'/sample_file.txt')
    stat_file_ret = cos_client.stat_file(request)
    logger.info('stat file, return message: ' + str(stat_file_ret))

    ############################################################################
    # 目录操作                                                                 #
    ############################################################################
    # 1. 生成目录, 目录名为sample_folder
    request = CreateFolderRequest(bucket, u'/sample_folder/')
    create_folder_ret = cos_client.create_folder(request)
    logger.info('create folder ret:' + str(create_folder_ret))

    # 2. 更新目录的biz_attr属性
    request = UpdateFolderRequest(bucket, u'/sample_folder/', u'这是一个测试目录')
    update_folder_ret = cos_client.update_folder(request)
    logger.info('update folder ret:' + str(update_folder_ret))

    # 3. 获取目录属性
    request = StatFolderRequest(bucket, u'/sample_folder/')
    stat_folder_ret = cos_client.stat_folder(request)
    logger.info("stat folder, return message: " + str(stat_folder_ret))

    # 4. list目录, 获取目录下的成员
    request = ListFolderRequest(bucket, u'/sample_folder/')
    list_folder_ret = cos_client.list_folder(request)
    logger.info("list folder, return message: " + str(list_folder_ret))
    # 5. 删除目录
    request = DelFolderRequest(bucket, u'/sample_folder/')
    delete_folder_ret = cos_client.del_folder(request)
    logger.info("delete folder, return message: " + str(delete_folder_ret))

if __name__ == '__main__':
    cos_demo()
