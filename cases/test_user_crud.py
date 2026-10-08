# -*- coding: utf-8 -*-

import pytest
import uuid

# 该类所有用例自动执行认证前置，等价于登录后操作
@pytest.mark.usefixtures('auth_headers')
class TestUserCrud:
    # 1. 参数化获取不同页码的用户列表（对应课程参数化知识点）
    @pytest.mark.parametrize('page',[1,2])
    def test_get_user_list(self,http_client,page):
        params = {'page':page,'per_page':10}
        response = http_client.get('/users',params=params)
        res_json = response.json()

        print('=====test_get_user_list=====')
        print(f'请求URL: /users')
        print(f'请求参数params: {params}')
        print(f'响应状态码:{response.status_code}')
        print(f'响应JSON:{res_json}')

        assert response.status_code == 200
        assert type(res_json) == list
        assert len(res_json) <= 10

    # 2. 查询单个用户详情
    def test_get_single_user(self,http_client,create_user):
        #create_user fixture返回动态生成的user_id
        user_id = create_user
        response = http_client.get(f'/users/{user_id}')
        res_json = response.json()

        print("===== test_get_single_user =====")
        print(f"请求URL: /users/{user_id}")
        print(f"响应状态码: {response.status_code}")
        print(f"响应JSON: {res_json}")

        assert response.status_code == 200
        assert res_json['id'] == user_id
        assert 'name' in res_json
        assert 'email' in res_json

    # 3. 新增用户
    def test_get_user(self,http_client,test_data):
        user_data = test_data['user']['create'].copy()

        # 生成随机邮箱，保证唯一，避免重复报错
        random_str = uuid.uuid4().hex[:8]
        user_data['email'] = f'test{random_str}@example.com'

        response = http_client.post('/users',json=user_data)
        res_json = response.json()

        print("===== test_get_user(新增用户) =====")
        print(f"请求URL: /users")
        print(f"请求BODY: {user_data}")
        print(f"响应状态码: {response.status_code}")
        print(f"响应JSON: {res_json}")

        assert response.status_code == 201 # 201 = 创建成功
        assert res_json['email'] == user_data['email']
        assert res_json['name'] == user_data['name']
        assert res_json['status'] == user_data['status']
        assert 'id' in res_json

    # 4. 修改用户信息
    def test_update_user(self,http_client,test_data):

        # 先创建用户再修改，保证用例独立可重复运行
        user_data = test_data['user']['create'].copy()
        random_str = uuid.uuid4().hex[:8]
        user_data['email'] = f'test{random_str}@example.com'
        created_resp = http_client.post('/users',json=user_data)
        user_id = created_resp.json()['id']

        # 执行修改
        updated_data = test_data['user']['update']
        response = http_client.put(f'/users/{user_id}',json=updated_data)
        res_json = response.json()

        print("===== test_update_user =====")
        print(f"新建用户请求BODY: {user_data}")
        print(f"待修改用户ID: {user_id}")
        print(f"PUT请求URL: /users/{user_id}")
        print(f"修改请求BODY: {updated_data}")
        print(f"响应状态码: {response.status_code}")
        print(f"响应JSON: {res_json}")

        assert response.status_code == 200
        assert res_json['name'] == updated_data['name']
        assert res_json['status'] == updated_data['status']


    # 5. 删除用户
    def test_delete_user(self,http_client,test_data):

        # 先创建用户再删除，保证用例独立
        user_data = test_data['user']['create'].copy()
        random_str = uuid.uuid4().hex[:8]
        user_data['email'] = f'test{random_str}@example.com'
        created_resp = http_client.post('/users',json=user_data)
        user_id = created_resp.json()['id']

        # 执行删除
        response = http_client.delete(f'/users/{user_id}')

        print("===== test_delete_user =====")
        print(f"新建用户请求BODY: {user_data}")
        print(f"待删除用户ID: {user_id}")
        print(f"DELETE请求URL: /users/{user_id}")
        print(f"响应状态码: {response.status_code}")

        assert response.status_code == 204  # 204 = 删除成功，无响应体




