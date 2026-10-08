import pytest
import uuid

@pytest.mark.usefixtures('auth_headers')
class TestUserBoundary:

    # 6. 用户姓名：最大允许长度 50 字符
    def test_create_user_name_max_50(self,http_client,test_data):
        user_data = test_data['user']['create'].copy()
        random_str = uuid.uuid4().hex[:8]
        user_data['email'] = f'test{random_str}@example.com'
        user_data['name'] = 'a'* 50
        resp = http_client.post('/users',json=user_data)
        res_json = resp.json()

        print("===== test_create_user_name_max_50 =====")
        print(f"name长度：{len(user_data['name'])}")

        assert resp.status_code == 201
        assert res_json["name"] == user_data["name"]

    # 7. 年龄边界：最小合法年龄18
    def test_create_user_age_min_18(self,http_client,test_data):
        user_data = test_data['user']['create'].copy()
        random_str = uuid.uuid4().hex[:8]
        user_data['email'] = f'test{random_str}@example.com'
        user_data['age'] = 18
        resp = http_client.post('/users',json=user_data)

        print("===== test_create_user_age_min_18 =====")
        print(f"响应状态码:{resp.status_code}")

        assert resp.status_code == 201


