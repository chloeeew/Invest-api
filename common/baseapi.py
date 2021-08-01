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
        """
        传递响应结果、以及excel中给获取到的响应结果断言和数据库断言，
        1、判断断言是否有值
        2、值存在则断言，把断言结果存储到断言结果集合中
        3、如果断言解雇集合中存在False（及断言失败），那么返回False，否则方法返回True
        """
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
        """
        传入响应结果、excel中的提取字段，以及全局变量类实例
        如果提取字段存在值，那么就调用提取方法提取值
        """
        if not extract:
            return None
        extract_from_response(response_json, extract,global_data)


    def api_execute_update_by_pre_sql(self,pre_sql):
        """
        传入响应结果、excel中的pre_sql预执行字段
        如果该字段存在值，那么调用方法执行
        """
        if pre_sql:
            MySqlManager().update_data(pre_sql)


