"""
==================
Author:Chloeee
Time:2021/5/30 19:27
Contact:403505960@qq.com
==================
"""

class Data:
    """
    配置可在excel中替换的数据
    动态保存全局变量在此
    """
    user = "15500000000"
    pwd = "12345678"
    admin = "17679571234"
    admin_pwd = "12345678"
    # 设置global_user列表，存放所有用户的用户名，便于在fixture的session前置判断是否有这些数据，没有就注册
    global_user = ["15500000000","17679571234"]

    mock_url = r"https://www.fastmock.site/mock/a25c73220e080afccc5c3362c6782a39/member"



