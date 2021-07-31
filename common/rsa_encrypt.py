"""
==================
Author:Chloeee
Time:2021/6/12 15:25
Contact:403505960@qq.com
==================
"""


import rsa
import base64
import time


def rsa_encrypt(msg):
    """
    根据公钥对信息做加密处理（开发提供的公钥）
    :param msg: message that need to be encrypted
    :return: encrypted message
    """
    # 公钥信息
    server_public_key = """
    -----BEGIN PUBLIC KEY-----
    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDQENQujkLfZfc5Tu9Z1LprzedE
    O3F7gs+7bzrgPsMl29LX8UoPYvIG8C604CprBQ4FkfnJpnhWu2lvUB0WZyLq6sBr
    tuPorOc42+gLnFfyhJAwdZB6SqWfDg7bW+jNe5Ki1DtU7z8uF6Gx+blEMGo8Dg+S
    kKlZFc8Br7SHtbL2tQIDAQAB
    -----END PUBLIC KEY-----
    """

    # 生成公钥对象
    public_key_btye = server_public_key.encode("utf-8")
    public_key_obj = rsa.PublicKey.load_pkcs1_openssl_pem(public_key_btye)

    # 将要加密的信息转换成字节对象
    msg_byte = msg.encode("utf-8")

    # 根据字典结对和公钥对象进行加密，返回加密文本
    crypt_msg = rsa.encrypt(msg_byte, public_key_obj)
    # 使用base64转换成对应字符串
    crypt_base64_msg = base64.b64encode(crypt_msg)
    return crypt_base64_msg.decode()


def get_sign(token):
    """
    根据鉴权规则获得签名，签名由token前50位+当前时间戳加密生成
    :param token: 登录响应结果返回的token值
    :return: sign_encrypt加密后的sign，还有timestamp当前时间戳
    """
    token_50 = token[:50]
    timestamp = int(time.time())
    # 将前50位的token 和 当前时间戳拼凑
    sign_msg = token_50 + str(timestamp)
    # 加密拼凑后的sign
    sign_encrypt = rsa_encrypt(sign_msg)
    # print(sign_encrypt)
    # print(timestamp)
    return sign_encrypt,timestamp




# if __name__ == "__main__":
#     get_sign("123456789012345678901234567890123456789012345678901234567890")


