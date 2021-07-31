"""
==================
Author:Chloeee
Time:2021/5/18 21:19
Contact:403505960@qq.com
==================
"""
from decimal import Decimal
from common.logger_handler import logger
from common.mypymysql import MyMySql
import jsonpath

# 用 jsonpath 方式提取出response的值

class MyAssert:

    def assert_by_json(self, response_dict, assert_str):
        """
        按照预期结果断言application/json的内容
        :param response_dict: json，就是response.json()
        :param assert_str: 用例文件的断言格式列表字符串'[{},{}]’
        :return:
        step1---- assert_str 用ast转换成assert_list
        step2---- 遍历提取出json表达式，结合获取的response_dict获取实际结果
        [
        {"expression":"$..code",
        "expected":2,
        "type":"equal"},
        {"expression":"$..msg",
        "expected":"用户昵称长度超过10位",
        "type":"equal"}
         ]
        step3---- 根据对比的方式，预期结果跟实际结果的对比，True?False?存放到一个列表中 result_bool_list
        step4---- 根据列表 result_bool_list 是否存在False，抛出AssertionError
        """
        assert_list = eval(assert_str)
        logger.info(f"转换断言响应结果的字符串成对应格式{assert_list}")
        result_bool_list = []

        for each_assert in assert_list:
            jp_express = each_assert["expression"]  # 表达式
            assert_expect = each_assert["expected"]
            assert_type = each_assert["type"]

            actual = jsonpath.jsonpath(response_dict, jp_express)[0]
            if not actual:
                # 表达式找不到actual==False
                logger.error(f"{jp_express}无法在{response_dict}中提取出来，请检查表达式")
                raise TypeError

            if assert_type == "equal":
                result_bool_list.append(assert_expect == actual)
                logger.info(f"对比实际提取结果{actual},和预期结果{assert_expect}，是否相等：{assert_expect == actual}")
            elif assert_type == "contains":
                result_bool_list.append(assert_expect in actual)
                logger.info(f"对比实际提取结果{actual},和预期结果{assert_expect}，是否为包含关系：{assert_expect in actual}")

        if False in result_bool_list:
            logger.error("存在断言响应结果失败的情况，请检查断言与实际响应结果")
            return False
        else:
            logger.info("断言响应结果成功")
            return True


    def assert_database(self,assert_str):
        """
        断言数据库，不需要去获取响应结果，只需要读取excel中assert_db列的数据，根据比对方式校对sql
        excel实例：[{"sql":"select id from member where mobile_phone='#phone#'","expected":1,"db_type":"count"}]
        step1：将列表字符串用literal_eval转换成列表
        step2：遍历列表
        step3：获取列表中的对应sql、expected和db_type的字典值，根据db_type去决定调用数据库类mypymysql的哪个方法
        step4：调用方法返回的实际结果与期望结果的expected比对
        :param assert_str:excel提取出来的assert_db列
        :return:
        """
        result_bool_list = []

        # 转换成列表
        assert_db_list = eval(assert_str)
        logger.info(f"转换断言数据库字符串成对应格式{assert_db_list}")
        # 建立数据库连接
        db = MyMySql()

        # 遍历比对
        for check_dict in assert_db_list:
            if check_dict["type_db"] == "count":
                result = db.get_query_count(check_dict["sql"])
            elif check_dict["type_db"] == "equal":
                result = db.get_query_result(check_dict["sql"])
                for key,value in result.items():
                    # 处理返回值是Decimal的情况，需要转换为float
                    if isinstance(value,Decimal):
                        result[key] = float(value)
            else:
                # excel写得不对
                raise Exception
            logger.info(f'对比实际结果{result},和预期结果{check_dict["expected"]}，是否相等：'
                        f'{check_dict["expected"] == result}')
            result_bool_list.append(check_dict["expected"] == result)


        if False in result_bool_list:
            logger.error("存在断言数据库结果失败的情况，请检查断言与实际响应结果")
            return False
        else:
            logger.info("断言数据库结果成功")
            return True


if __name__ == "__main__":
    # db_list = '[{"sql":"select id from member where mobile_phone=\'15697042402\'","expected":1,"type_db":"count"}]'
    # print(MyAssert().assert_database(db_list))
    fake_json = {
        "code":200,
        "msg":"abc"
    }
    fake_expression_str = '[{"expression":"$..qq","expected":0,"type":"equal"}]'
    MyAssert().assert_by_json(fake_json, fake_expression_str)