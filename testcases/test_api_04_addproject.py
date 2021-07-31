"""
==================
Author:Chloeee
Time:2021/6/10 15:46
Contact:403505960@qq.com
==================
"""


import pytest
import allure
from common.myexcel import MyExcel
from common.myreplace import replace_excel_dict_by_mark
from common.baseapi import Baseapi

@allure.feature("新增项目测试")
@pytest.mark.usefixtures("class_share_data_init")
class TestAddProject:

    @allure.title("新增项目用例")
    @pytest.mark.parametrize("cases", MyExcel("新增项目接口").get_excel_data())
    def test_add_project(self, cases, class_share_data_init):
        with allure.step(f"测试用例名称：{cases.get('title')}-\n步骤一：接口关联，数据替换"):
            cases = replace_excel_dict_by_mark(cases, class_share_data_init)

        with allure.step("步骤二：发送请求"):
            ba = Baseapi()
            response_format = ba.api_requests(method=cases["method"], api_name=cases["url"],
                                              data=cases["req_data"],global_data=class_share_data_init)

        with allure.step("步骤三：提取出接口关联所需值"):
            ba.api_extract(response_format,cases.get("extract"),class_share_data_init)

        with allure.step("步骤四：断言响应结果及数据库"):
            assert ba.api_get_assert_result(response_format,cases.get("assertion"),cases.get("assert_db"))

