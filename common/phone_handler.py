"""
==================
Author:Chloeee
Time:2021/6/11 9:47
Contact:403505960@qq.com
==================
"""

from faker import Faker
from common.mysql_manager import MySqlManager

def get_phone_num():
    """
    通过faker获得随机手机号码
    如果经过sql查询后，确认不存在这个手机号码，那么才会返回该手机号码，否则就持续这个步骤，直到满足条件
    :return: phone_num
    """
    while True:
        phone_num = Faker("zh_CN").phone_number()
        sql = f"select id from member where mobile_phone='{phone_num}'"
        msq = MySqlManager().get_query_count(sql)
        if msq == 0:
            return phone_num


def is_phone_exist(phone_num):
    """
    根据传递的phone_num参数，用于结合sql判断是否存在
    :param phone_num:
    :return: True
    """

    sql = f"select id from member where mobile_phone='{phone_num}'"
    msq = MySqlManager().get_query_count(sql)
    if msq == 0:
        return False
    else:
        return True