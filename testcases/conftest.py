"""
==================
Author:Chloeee
Time:2021/6/5 14:32
Contact:403505960@qq.com
==================
"""

from common.myphone import is_phone_exist
from common.myrequests import MyRequests
from common.mydata import Data
import pytest

@pytest.fixture(scope="session",autouse=True)
def global_init():
    """
    Data配置的全局用户信息 - 要确保一定是存在的，所以在每次会话前都要经过这个的前置方法判断
    1、从Data里拿出来判断的用户数据 global_users
    2、调用sql从数据库查询，如果不存在就注册
    """
    phone_num_exist = is_phone_exist(Data.user)
    if not phone_num_exist:
        req_data = {"mobile_phone":Data.user,"pwd":Data.pwd}
        MyRequests().send_requests("post","/member/register",req_data)

    phone_admin_num_exit = is_phone_exist(Data.admin)
    if not phone_admin_num_exit:
        req_data_admin = {"mobile_phone":Data.admin,"pwd":Data.admin_pwd,"type":0}
        MyRequests().send_requests("post", "/member/register", req_data_admin)

@pytest.fixture(scope="class")
def class_share_data_init():
    class_data = Data()
    yield class_data




