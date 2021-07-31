"""
==================
Author:Chloeee
Time:2021/5/26 21:06
Contact:403505960@qq.com
==================
"""
import pytest
import allure
from common.myexcel import MyExcel
from common.baseapi import Baseapi
from common.myreplace import replace_excel_dict_by_mark


@allure.feature("登录测试")
@pytest.mark.usefixtures("class_share_data_init")
class TestLogin:

    @allure.title('登录测试用例')
    @pytest.mark.parametrize("cases",MyExcel("登录接口").get_excel_data())
    def test_login(self, cases, class_share_data_init):

        with allure.step(f"测试用例名称：{cases.get('title')}-\n步骤一：接口关联，数据替换"):
            cases = replace_excel_dict_by_mark(cases, class_share_data_init)

        with allure.step("步骤二：发送请求"):
            ba = Baseapi()
            response_format = ba.api_requests(method=cases["method"], api_name=cases["url"],
                                              data=cases["req_data"],global_data=class_share_data_init)

        with allure.step("步骤三：断言响应结果及数据库"):
            assert ba.api_get_assert_result(response_format,cases.get("assertion"),cases.get("assert_db"))



