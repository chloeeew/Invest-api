"""
==================
Author:Chloeee
Time:2021/5/30 19:29
Contact:403505960@qq.com
==================
"""

from common.mydata import Data
from common.logger_handler import logger
import jsonpath
import ast



def extract_from_response(response_dict,expression_str, data:Data):
    """
    根据excel中extract列的表达式key为全局变量名。value为jsonpath提取表达式。提取出响应结果response的值
    并按照extract的key值作为全局变量Data类的变量名，提取出的对应值赋给对应的变量
    :param data: Data类实例对象
    :param response_dict: 响应结果response的字典值
    {"code":0,"msg":"OK","data":{"id":101,"leave_amount":6300.02,"token": "eyJhbGciOiJIUzUxMiJ9.eyJtZW"}}
    :param expression_str:字典格式的字符串，为excel提取出来的extract列的值
    :return:None
    """
    # 将字典形式字符串转换为字典
    expression_dict = ast.literal_eval(expression_str)
    logger.info(f"转换提取表达式字符串成字典：{expression_dict}")

    # 提取出字典的key和value，其中key是全局变量名，value是对应的jsonpath表达式
    for key,value in expression_dict.items():
        # jsonpath表达式根据响应结果
        result = jsonpath.jsonpath(response_dict,value)[0]
        setattr(data,key,str(result))
        logger.info(f"设置测试类的全局变量{key},值为{result}")

