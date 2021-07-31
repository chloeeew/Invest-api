"""
==================
Author:Chloeee
Time:2021/4/21 22:50
Contact:403505960@qq.com
==================
"""

# 实例为旧版课堂派

import requests

# 实例化一个会话对象, 注意Session大写
s = requests.Session()

# 请求地址
login_url = "https://v4.ketangpai.com/UserApi/login"

# 请求体 application/x-www-form-urlencoded
login_data = {
    "email": "leekchlo@icloud.com",
    "password": "admin123",
    "remember": "0"
}

# 发起登录请求，传入请求地址、请求体参数
res_login = s.post(url=login_url, data=login_data)

# 再次发起第二次请求
url_vip = "https://v4.ketangpai.com/VipApi/isVip"
res = s.get(url_vip)

# 获取响应的状态码
print(f'响应状态码====：{res.status_code}')

# 获取响应数据（如果接口的响应数据是json格式，可以用这个方法(否则不能用）， 这个方法执行后的结果是一个字典
print(f'响应数据json========：{res.json()}')

# 获取响应头
print(f'响应头======:{res.headers}')

