"""
==================
Author:Chloeee
Time:2021/5/22 9:33
Contact:403505960@qq.com
==================
"""

from common.yaml_controller import yaml_config
from common.logger_handler import logger
import pymysql

class MyMySql:

    def __init__(self):
        db_info = yaml_config["database"]
        self.con = pymysql.connect(host=db_info["host"],  # 数据库的地址
                                   user=db_info["user"],  # 登录数据库的账号
                                   password=db_info["password"],  # 登录数据库的密码
                                   port=db_info["port"],  # 端口
                                   database=db_info["database"],  # 库名称
                                   charset="utf8",
                                   cursorclass=pymysql.cursors.DictCursor
                                   )
        self.cur = self.con.cursor()


    def get_query_count(self,sql):
        """根据sql获取查询结果的条数"""
        result = self.cur.execute(sql)
        logger.info(f"执行的sql语句为{sql},获取执行条数的执行结果为{result}")

        return result

    def get_query_result(self, sql):
        """获取单个查询结果，以列表+字典形式返回"""
        self.cur.execute(sql)
        result = self.cur.fetchone()
        logger.info(f"执行的sql语句为{sql},执行结果为{result}")
        return result


    def get_query_many_results(self, sql,size=None):
        """获取多个查询结果，以列表+字典形式返回"""
        self.cur.execute(sql)
        if size:
            result = self.cur.fetchmany(size=size)
            logger.info(f"执行的sql语句为{sql},执行条数的执行结果为{result}")
            return result
        else:
            result = self.cur.fetchall()
            logger.info(f"执行的sql语句为{sql},执行结果为{result}")
            return result


    def update_data(self, sql):
        """
        update语句执行 , 如果执行失败就回滚，如果执行成功就commit
        """
        try:
            self.cur.execute(sql)
            logger.info(f"执行的sql语句为{sql}")
        except Exception:
            self.con.rollback()
            logger.warning("执行失败，数据库回滚")
        else:
            self.con.commit()
            logger.warning("执行成功，提交")



    def close_connect(self):
        """关闭连接"""
        self.cur.close()
        self.con.close()


# if __name__ == "__main__":
#     conn = MyMySql()
#     sql = "select l.status from loan l where id='2'"
#     res = conn.get_query_result(sql)
#     print(res)