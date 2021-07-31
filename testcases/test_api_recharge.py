"""
==================
Author:Chloeee
Time:2021/5/30 19:42
Contact:403505960@qq.com
==================
"""

from common.myrequests import MyRequests
from common.myexcel import MyExcel
from common.myassert import MyAssert
from common.myextract import extract_from_response
from common.myreplace import replace_excel_dict_by_mark
import pytest
import json

@pytest.mark.usefixtures("class_share_data_init")
class TestRecharge:


    @pytest.mark.parametrize("cases", MyExcel("充值接口").get_excel_data())
    def test_recharge(self, cases, class_share_data_init):
        cases = replace_excel_dict_by_mark(cases, class_share_data_init)
        r_assertion = cases["assertion"]
        r_assert_db = cases["assert_db"]
        r_requests = MyRequests()

        # 检查有没有token值，如果有就传上token
        if hasattr(class_share_data_init, "token"):
            response_format = r_requests.send_requests(method=cases["method"], api_name=cases["url"],
                                                       data=cases["req_data"],
                                                       token=getattr(class_share_data_init,"token"))
        else:
            response_format = r_requests.send_requests(method=cases["method"], api_name=cases["url"],
                                                       data=cases["req_data"])

        # 提取出接口关联所需值
        if cases["extract"]:
            extract_from_response(response_format, cases["extract"],class_share_data_init)

        # 存储断言结果的集合
        result_list = []

        r_assert = MyAssert()
        if r_assertion:
            result_list.append(r_assert.assert_by_json(response_format, r_assertion))

        if r_assert_db:
            result_list.append(r_assert.assert_database(r_assert_db))

        if False in result_list:
            raise AssertionError
