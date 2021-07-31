"""
==================
Author:Chloeee
Time:2021/5/12 22:20
Contact:403505960@qq.com
==================
"""

import pytest
import allure
from common.myexcel import MyExcel
from common.baseapi import Baseapi
from common.myreplace import replace_excel_dict_by_mark


@allure.feature("注册测试")
@pytest.mark.usefixtures("class_share_data_init")
class TestRegister:

    @allure.title("注册测试用例")
    @pytest.mark.parametrize("cases",MyExcel("注册接口").get_excel_data())
    def test_register(self, cases, class_share_data_init):
        with allure.step(f"测试用例名称：{cases.get('title')}-\n步骤一：替换值"):
            cases = replace_excel_dict_by_mark(cases, class_share_data_init)


        with allure.step("步骤二：发起请求"):
            ba = Baseapi()
            response_format = ba.api_requests(method=cases["method"], api_name=cases["url"],
                                              data=cases["req_data"], global_data=class_share_data_init)

        with allure.step("步骤三：断言响应和数据库是否满足预期=实际结果"):
            assert ba.api_get_assert_result(response_format, cases.get('assertion'), cases.get('assert_db'))





