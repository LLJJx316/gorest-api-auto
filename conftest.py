import pytest
import json
import os
import uuid
from common.http_client import HttpClient

# 全局加载测试数据，整个测试会话只加载1次
@pytest.fixture(scope='session',autouse=True)  #scope="session"：整个 pytest 执行过程只执行一次
def test_data():
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data','test_data.json') ## __file__ 就是当前conftest.py文件
    with open(data_dir,'r',encoding='utf-8') as f:
        data = json.load(f) #读取token
    return data

# 全局HTTP客户端，复用连接
@pytest.fixture(scope='session',autouse=True)
def http_client(test_data:dict):
    client = HttpClient(test_data['base_url'])
    yield client

@pytest.fixture(scope='session',autouse=True)
def auth_headers(http_client,test_data,):
    token = test_data['access_token']
    http_client.set_token(token)
    headers = {"Authorization": f"Bearer {token}"}
    yield headers

@pytest.fixture(scope="class")
def create_user(http_client, auth_headers, test_data):
    payload =test_data['user']['create'].copy()
    # 生成随机邮箱，防止重复报错
    random_str = uuid.uuid4().hex[:8]
    payload['email'] = f'test_{random_str}@example.com'
    resp = http_client.post(url="/users", json=payload, headers=auth_headers)
    resp.raise_for_status()
    user_info = resp.json()
    yield user_info["id"]
    # 用例执行完自动删除用户，清理脏数据
    http_client.delete(url=f"/users/{user_info['id']}", headers=auth_headers)