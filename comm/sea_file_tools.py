"""
    封装 SeaFile 接口相关的函数
"""

import requests

from comm.sea_file_url_tools import *


# 登录函数
def sea_file_1_1(username, password):
    """
    输入用户名和密码，返回登录响应
    :param username: 用户名
    :param password: 密码
    :return response: 响应对象
    """
    # 登录接口
    url = host + login_path_1
    # 要传的登录头
    headers = {"content-type": "application/x-www-form-urlencoded"}
    # 要传的参数，用户名和密码
    body = {"username": username, "password": password}
    # 返回得到的响应对象
    response = requests.post(url=url, headers=headers, data=body)
    return response


# 获取用户信息
def sea_file_1_2(token):
    """
    输入获取到的token，获取用户信息
    :param token: 登录后获取的token值
    :return response: 响应对象
    """
    # 获取用户信息接口
    url = host + info_path_2
    # 要传的参数，token
    headers = {"authorization": "token " + token}
    # 返回响应对象
    response = requests.get(url=url, headers=headers)
    return response


# 新增资料库
def sea_file_1_3(token, repo_name):
    """
    输入获取到的token，和资料库的名字，新增资料库
    :param token: 登录后获取的token值
    :param repo_name: 资料库的名字
    :return response: 响应对象
    """
    # 新增资料库接口
    url = host + add_select_path_3_4
    # 要传的参数，token
    headers = {"authorization": "token " + token}
    body = {"name": repo_name}
    # 返回响应对象
    response = requests.post(url=url, headers=headers, data=body)
    return response


# 查询所有资料库
def sea_file_1_4(token):
    """
    输入获取到的token，查询所有资料库
    :param token: 登录后获取的token值
    :return response: 响应对象
    """
    # 查询所有资料库接口
    url = host + add_select_path_3_4
    # 要传的参数，token
    headers = {"authorization": "token " + token}
    # 返回响应对象
    response = requests.get(url=url, headers=headers)
    return response


# 修改资料库的名字
def sea_file_1_5(token, repo_id, repo_name):
    """
    输入获取到的token值，要修改的资料库的id值，和新的资料库名字
    :param token: 登录后获取的token值
    :param repo_id: 要修改的资料库id
    :param repo_name: 新的资料库名字
    :return response: 响应对象
    """
    # 修改资料库名字接口
    url = modify_delete_add_path_5_6_7_8(5, repo_id)
    # 要传的参数，token
    headers = {"authorization": "token " + token}
    # 要传的参数，新的资料库名字
    body = {"name": repo_name}
    # 返回响应对象
    response = requests.post(url=url, headers=headers, data=body)
    return response


# 删除指定的资料库
def sea_file_1_6(token, repo_id):
    """
    输入获取到的token值和要删除的资料库id，删除资料库
    :param token: 登录后获取的token值
    :param repo_id: 要删除的资料库id
    :return response: 响应对象
    """
    # 删除资料库接口
    url = modify_delete_add_path_5_6_7_8(6, repo_id)
    # 要传的参数，token
    headers = {"authorization": "token " + token}
    # 返回响应对象
    response = requests.delete(url=url, headers=headers)
    return response


# 在指定的资料库目录新建文件
def sea_file_1_7(token, repo_id, file_name):
    """
    输入获取到的token值，指定的资料库id，和要新建的文件名字
    :param token: 登录后获取的token值
    :param repo_id: 指定的资料库id
    :param file_name: 要新建的文件名字
    :return response: 响应对象
    """
    # 新建文件接口
    url = modify_delete_add_path_5_6_7_8(7, repo_id, file_name)
    # 要传的参数，token
    headers = {"authorization": "token " + token}
    # 要传的参数，新建文件的操作类型
    body = {"operation": "create"}
    # 返回响应对象
    response = requests.post(url=url, headers=headers, data=body)
    return response


# 在指定的资料库目录删除文件
def sea_file_1_8(token, repo_id, file_name):
    """
    输入获取到的token值，指定的资料库id，和要删除的文件名字
    :param token: 登录后获取的token值
    :param repo_id: 指定的资料库id
    :param file_name: 要删除的文件名字
    :return response: 响应对象
    """
    # 删除文件接口
    url = modify_delete_add_path_5_6_7_8(8, repo_id, file_name)
    # 要传的参数，token
    headers = {"authorization": "token " + token}
    # 返回响应对象
    response = requests.delete(url=url, headers=headers)
    return response
