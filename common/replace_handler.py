"""
==================
Author:Chloeee
Time:2021/6/5 16:52
Contact:403505960@qq.com
==================
"""

from common.global_data import Data
from common.globalmethod import get_current_time_str_time
from common.phone_handler import get_phone_num
from common.logger_handler import logger
import re


def replace_excel_dict_by_mark(case_dict, data:Data):
    """
    根据用例中标识的标记，进行替换。
    标记可能会被替换成 脚本生成的内容、配置文件的属性、Data类动态生成的值
    :param data : Data类实例对象
    :param case_dict:用例数据，类型是字典
    :return: 替换后的用例数据，类型式字典
    """

    # 将字典转换为字符串
    case_str = str(case_dict)

    # 转换成字符串后，通过正则表达式将符合 #mark# 的表达式提取出来
    re_express = "#(\w+)#"
    # 生成标记列表
    re_result_list = re.findall(re_express,case_str)

    # 处理脚本生成的new_phone(globalmethod封装）,将#phone#替换掉
    if 'phone' in re_result_list:
        new_phone = get_phone_num()
        case_str = case_str.replace('#phone#',str(new_phone))
        logger.info(f"脚本生成随机手机号{new_phone},并替换到#phone#中")

    # 处理脚本生成的时间戳(globalmethod封装）,将#strftime#替换掉
    if 'strftime' in re_result_list:
        time_str = get_current_time_str_time()
        case_str = case_str.replace('#strftime#',time_str)
        logger.info(f"脚本生成时间戳{time_str},并替换到#strftime#中")

    # 遍历标记列表 如果列表中的元素存在phone
    for mark in re_result_list:
        if hasattr(data,mark):
            case_str = case_str.replace(f'#{mark}#',getattr(data,mark))

    # 把该替换的替换完成后，再转换成字典
    case_final_dict = eval(case_str)
    logger.info(f"替换标识符后的用例：{case_final_dict}")
    return case_final_dict




# if __name__ == "__main__":
#     case = {"req_data":'[{"expression":"$..code","expected":0,"type":"equal"},{"expression":"$..msg",'
#                        '"expected":"OK","type":"equal"},{"expression":"$..leave_amount",'
#                        '"expected":#leave_amount#+2000,"type":"equal"}]'}
#
#     replace_excel_dict_by_mark(case)



