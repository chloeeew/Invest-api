"""
==================
Author:Chloeee
Time:2021/5/2 13:34
Contact:403505960@qq.com
==================
"""

import requests

basic_url = "http://api.lemonban.com/futureloan"

# =============  注册接口  ===================
register_url = basic_url + "/member/register"

register_header = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "Content-Type": "application/json"
}

register_data = {
    "mobile_phone": "13800138003",
    "pwd": "12345678",
    "reg_name": "chloe专用"
}

register_res = requests.post(url=register_url, json=register_data, headers=register_header)
register_res_json = register_res.json()
print(f"注册响应体：\n {register_res_json}")


# =============  登录接口  ===================

login_url = basic_url + "/member/login"
login_headers = register_header

login_data = {
    "mobile_phone": "13800138003",
    "pwd": "12345678"
}

login_res = requests.post(url=login_url, json=login_data, headers=login_headers)
login_res_json = login_res.json()
login_id = login_res_json["data"]["id"]
login_token = login_res_json["data"]["token_info"]["token"]

print(f"登录响应体：\n {login_res_json}")



# =============  充值接口  使用到token===================

recharge_url = basic_url + "/member/recharge"

recharge_headers = login_headers
recharge_headers["Authorization"] = f"Bearer {login_token}"

recharge_data = {
    "member_id": f"{login_id}",
    "amount": 17000
}

recharge_res = requests.post(url=recharge_url, json=recharge_data, headers=recharge_headers)
recharge_json = recharge_res.json()
print(f"充值的响应体：\n  {recharge_json}")



