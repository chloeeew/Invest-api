"""
==================
Author:Chloeee
Time:2021/4/24 10:52
Contact:403505960@qq.com
==================
"""

# 实例为新版课堂派

import requests

# 登录请求地址
url_login = "https://openapiv5.ketangpai.com/UserApi/login"
# 登录的请求体  application/json
json_login = {
    "email": "leekchlo@icloud.com",
    "password": "admin123",
    "remember": "0",
    "code": "",
    "mobile": "",
    "type": "login"
}
# 发起请求
res_login = requests.post(url_login, json=json_login)
# 响应体是json格式，可以用json接收
res_login_json = res_login.json()
# 获取token值
login_token = res_login_json["data"]["token"]


############################################
# 发起第二次请求，带上token

url_sem = "https://openapiv5.ketangpai.com/CourseApi/semesterList"
data_sem_json = {
    "isstudy": "0",
    "search": ""
}
# 其他默认的header不需要自己再去填，只需要填写额外附加的
headers_sem = {"token":login_token}

# 这里的header参数是看requests的**kwargs可选参数
res_sem = requests.post(url_sem, json=data_sem_json, headers=headers_sem)


print(f'响应状态码====：{res_sem.status_code}')

print(f'响应数据json========：{res_sem.json()}')

print(f'响应头======:{res_sem.headers}')

