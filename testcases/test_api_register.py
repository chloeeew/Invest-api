"""
==================
Author:Chloeee
Time:2021/5/12 22:20
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
class TestRegister:


    @pytest.mark.parametrize("register_case",MyExcel("注册接口").get_excel_data())
    def test_register(self, register_case,class_share_data_init):

        register_case = replace_excel_dict_by_mark(register_case,class_share_data_init)
        r_req_data = register_case["req_data"]
        r_assertion = register_case["assertion"]
        r_assert_db = register_case["assert_db"]

        # json格式转换成字典
        r_req_data_json = json.loads(r_req_data)

        r_requests = MyRequests()
        response_format = r_requests.send_requests(method=register_case["method"],api_name=register_case["url"],
                                                   data=r_req_data_json)

        # 存储断言结果的集合
        result_list = []

        r_assert = MyAssert()
        if r_assertion:
            result_list.append(r_assert.assert_by_json(response_format, r_assertion))

        if r_assert_db:
            result_list.append(r_assert.assert_database(r_assert_db))

        if False in result_list:
            raise AssertionError






