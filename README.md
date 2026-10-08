# GoRest 接口自动化测试项目

## 技术栈
- Python3
- pytest
- requests
- pytest-html

## 项目简介
本项目基于GoRest公开接口，完成用户模块的接口自动化测试。
封装了HttpClient请求类统一管理请求会话、请求头；
使用pytest编写测试用例，读取外部json文件存放测试数据，运行脚本自动生成HTML测试报告。


## 项目目录结构
 ```
Project_api/
├─ cases/ # 测试用例文件夹
│ ├─ test_user_boundary.py # 边界、异常用例
│ └─ test_user_crud.py # CRUD 业务用例
├─ common/
│ └─ http_client.py # http 请求封装类
├─ data/
│ └─ test_data.json # 测试数据
├─ reports/
│ └─ report.html # 生成的测试报告
├─ conftest.py # pytest 前置 fixture
├─ pytest.ini # pytest 配置
├─ requirements.txt # 依赖清单
└─ README.md
 ```


## 环境部署
1. 创建虚拟环境
```cmd
python -m venv .venv
```

2. 激活虚拟环境
```cmd
.venv\Scripts\activate
```

3. 安装依赖
```cmd
pip install -r requirements.txt
```
## 运行测试
1. 运行全部用例
```cmd
pytest cases/ -v -s
```

2. 运行并生成html报告
```cmd
pytest cases/ -v -s --html=reports/report.html
```


## 测试用例说明
### test_user_crud.py（正向 CRUD 业务用例，共 5 条）
1. `test_get_user_list：参数化分页查询用户列表，验证分页返回列表长度、状态码
2. `test_get_single_user：查询单个用户详情，校验返回用户 id、name、email 字段
3. `test_get_user：新增用户，随机生成唯一邮箱，校验创建成功返回 201
4. `test_update_user：先创建用户，再 PUT 全量修改用户信息，校验修改后数据
5. `test_delete_user：先创建用户，再执行删除，校验删除返回 204

### test_user_boundary.py（边界值测试用例，共 2 条）
1. `test_create_user_name_max_50：姓名边界，传入最大长度 50 个字符，验证可正常创建
2. `test_create_user_age_min_18：年龄边界，传入最小合法年龄 18，验证创建成功

## 备注
项目源码保存在U盘，可直接运行脚本，查看测试报告。