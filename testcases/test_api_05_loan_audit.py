"""
==================
Author:Chloeee
Time:2021/6/11 9:53
Contact:403505960@qq.com
==================
"""

import pytest
import allure
from common.excel_manager import ExcelManager
from common.replace_handler import replace_excel_dict_by_mark
from common.baseapi import Baseapi


@allure.feature("审核项目测试")
@pytest.mark.usefixtures("class_share_data_init")
class TestLoanAudit:

    @allure.title("审核项目用例")
    @pytest.mark.parametrize("cases", ExcelManager("审核项目接口").get_excel_data())
    def test_loan_audit(self, cases, class_share_data_init):
        with allure.step(f"测试用例名称：{cases.get('title')}-\n步骤一：接口关联，数据替换"):
            cases = replace_excel_dict_by_mark(cases, class_share_data_init)

        with allure.step("步骤二：执行sql语句"):
            ba = Baseapi()
            ba.api_execute_update_by_pre_sql(cases.get("pre_sql"))

        with allure.step("步骤三：发送请求"):
            response_format = ba.api_requests(method=cases["method"],api_name=cases["url"],
                                              data=cases["req_data"],global_data=class_share_data_init)

        with allure.step("步骤四：提取出接口关联所需值"):
            ba.api_extract(response_format,cases.get("extract"),global_data=class_share_data_init)

        with allure.step("步骤五：断言响应结果及数据库"):
            assert ba.api_get_assert_result(response_format,cases.get("assertion"),cases.get("assert_db"))
