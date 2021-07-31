"""
==================
Author:Chloeee
Time:2021/5/11 21:38
Contact:403505960@qq.com
==================
"""

from common.yaml_controller import yaml_config
from common.logger_handler import logger
from common.rsa_encrypt import get_sign
import requests
import json

"""
目的：封装Requests库，使用requests方法就能按需求调用post或get方法
"""

class MyRequests:
    def __init__(self):
        """设置header"""
        self.host = yaml_config["server"]["host"]
        self.headers = yaml_config["headers"]

    def send_requests(self, method, api_name, data, token=None):
        if isinstance(data,str):
            # json字符串格式转换为json字典格式
            data = json.loads(data)
        self.__deal_token(token)
        self.__deal_authorization(data,token)
        url = self.__deal_url(api_name)

        logger.info(f"请求的数据为：{data} \n 请求的地址url为{url} \n 请求头为：{self.headers}")

        if method != "post" and method != "get" and method != "patch":
            logger.error("excel用例中的method列写的不是post或get或patch，请检查")
            raise TypeError

        try:
            if method == "post":
                response = requests.request("post", url=url, json=data, headers=self.headers)
            elif method == "get":
                response = requests.request("get", url=url, param=json.dumps(data), headers=self.headers)
            else:
                response = requests.request("patch", url=url,json=data, headers=self.headers)
        except ConnectionError as ce:
            logger.error("请求失败，请检查请求数据")
            raise ce
        else:
            response.encoding = "utf-8"
            response_json = response.json()
            logger.info(f"响应结果为：{response_json}")
            return response_json
            # if method == "post" or method == "patch":
            #     # 用json格式返回响应体
            #     response_json = response.json()
            #     logger.info(f"响应结果为：{response_json}")
            #     return response_json
            # else:
            #     # 返回响应内容是
            #     # response.content.decode("utf-8")
            #     response.encoding="utf-8"
            #     response_text = response.text
            #
            #     logger.info(f"响应结果为：{response_text}")
            #     return response_text

    def __deal_token(self, p_token):
        """处理存在token时的情况"""
        if p_token:
            self.headers["Authorization"] = f"Bearer {p_token}"
            logger.info(f"存在token值，为请求头增加Bearer Token:{p_token}")


    def __deal_authorization(self, data, token):
        if token and self.headers.get("X-Lemonban-Media-Type") == 'lemonban.v3':
            sign,timestamp = get_sign(token)
            logger.info(f" 当前为lemonban.v3 使用 使用token进行加密处理获得sign:{sign}")
            data["timestamp"] = timestamp
            data["sign"] = sign


    def __deal_url(self,api_name):
        """处理api_name中存在以完成url形式传入过来http://或者https://开头的，或只传入接口地址/api/name"""
        if api_name.startswith("http://") or api_name.startswith("https://"):
            return api_name
        else:
            return self.host + api_name
