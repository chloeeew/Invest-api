"""
==================
Author:Chloeee
Time:2021/7/31 19:06
Contact:403505960@qq.com
==================
"""
from common.requests_manager import RequestsManager
from common.global_data import Data
from common.assert_manager import AssertManager
from common.mysql_manager import MySqlManager
from common.extract_manager import extract_from_response
from common.replace_handler import replace_excel_dict_by_mark

class Baseapi:


    def api_requests(self,method,api_name,data,global_data:Data):
        """根据token的情况请求数据"""
        r_requests = RequestsManager()
        if hasattr(global_data, "token"):
            response_format = r_requests.send_requests(method=method, api_name=api_name,
                                                       data=data,
                                                       token=getattr(global_data,"token"))
        else:
            response_format = r_requests.send_requests(method=method, api_name=api_name,
                                                       data=data)
        return response_format



    def api_get_assert_result(self,response_json:dict,assertion,assert_db):
        # 存储断言结果的集合
        result_list = []

        r_assert = AssertManager()
        if assertion:
            result_list.append(r_assert.assert_by_json(response_json, assertion))
        if assert_db:
            result_list.append(r_assert.assert_database(assert_db))

        if False in result_list:
            return False
        else:
            return True


    def api_extract(self,response_json:dict,extract,global_data:Data):
        if not extract:
            return None
        extract_from_response(response_json, extract,global_data)


    def api_execute_update_by_pre_sql(self,pre_sql):
        if pre_sql:
            MySqlManager().update_data(pre_sql)


