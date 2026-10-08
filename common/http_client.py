import requests #导入 requests 库

class HttpClient: #定义HttpClient的类
    def __init__(self,base_url): #初始化方法
        self.base_url = base_url
        self.session = requests.Session() #创建会话对象 Session 自动保存 Cookie
        self.headers = {}  #全局请求头，所有请求默认带上

    def set_token(self,token): #设置token
        self.headers["Authorization"] = "Bearer " + token  #后续所有请求自动带上这个 token，不用每个接口重复传。

    def send_request(self,method,url,**kwargs):
        full_url = self.base_url + url
        req_headers = self.headers.copy()
        if 'headers' in kwargs:
            req_headers.update(kwargs['headers'])
        kwargs['headers'] = req_headers

        if'timeout' not in kwargs:
            kwargs['timeout'] = 10


        try:
            response = self.session.request(method=method,url=full_url,**kwargs) #发送请求
            response.raise_for_status() #检测状态码
            return response
        except requests.exceptions.RequestException as e:
            print(f'接口请求异常:{e}')
            raise

    def get(self,url,**kwargs):
        return self.send_request("GET",url,**kwargs)

    def post(self,url,**kwargs):
        return self.send_request("POST",url,**kwargs)

    def put(self,url,**kwargs):
        return self.send_request("PUT",url,**kwargs)

    def delete(self,url,**kwargs):
        return self.send_request("DELETE",url,**kwargs)
