"""
==================
Author:Chloeee
Time:2021/6/2 20:59
Contact:403505960@qq.com
==================
"""

import re

test_str = "54848fw4ef1w5e15df15e111gr5Uefe15c22U6"
test_str2 = "r83r9hos#dsfjio##sdnfiwen"
tests_str3 = "{fwejij#pwd#fjiwefji#user#}"
res = re.findall("#(.+?)#", tests_str3)

print(res)