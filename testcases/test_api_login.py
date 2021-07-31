"""
==================
Author:Chloeee
Time:2021/5/26 21:06
Contact:403505960@qq.com
==================
"""

from common.myrequests import MyRequests
from common.myexcel import MyExcel
from common.myassert import MyAssert
from common.myreplace import replace_excel_dict_by_mark
import pytest
import json


@pytest.mark.usefixtures("class_share_data_init")
class TestLogin:

    @pytest.mark.parametrize("cases",MyExcel("登录接口").get_excel_data())
    def test_login(self, cases, class_share_data_init):
        cases = replace_excel_dict_by_mark(cases, class_share_data_init)
        r_req_data = cases["req_data"]
        r_assertion = cases["assertion"]


        r_requests = MyRequests()
        response_format = r_requests.send_requests(method=cases["method"], api_name=cases["url"],
                                                   data=r_req_data)

        # 存储断言结果的集合
        result_list = []

        r_assert = MyAssert()
        if r_assertion:
            result_list.append(r_assert.assert_by_json(response_format, r_assertion))


        if False in result_list:
            raise AssertionError



