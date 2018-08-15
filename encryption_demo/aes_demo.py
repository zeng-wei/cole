from Crypto.Cipher import AES
import base64
import json


class AESCrypt:

    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    def get_encrypt_str(self, obj):
        """
        obj转加密的str
        :param obj: python基本数据类型，dict、list等
        :return: 加密的str
        """
        return base64.b64encode(self.encrypt(json.dumps(obj).encode())).decode()

    def get_decrypt_obj(self, s):
        """
        str转obj
        :param s: str类型，加密的字符串
        :return: python基本数据类型
        """
        return json.loads(self.decrypt(base64.b64decode(s)).decode())

    def encrypt(self, text):
        crypt = AES.new(self.key, self.mode, self.key)  # 每次都需要创建新实例
        length = 16  # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度. 不足就补足
        count = len(text)
        if count % length != 0:
            add = length - (count % length)
        else:
            add = 0
        text = text + (b'\x00' * add)
        return crypt.encrypt(text)

    def decrypt(self, text):
        crypt = AES.new(self.key, self.mode, self.key)
        plain_text = crypt.decrypt(text)
        return plain_text.rstrip(b'\x00')  # 解密后，去掉补足的空格用strip() 去掉


if __name__ == '__main__':
    crypt = AESCrypt('irap1704irap1704')  # 初始化密钥
    obj_dec = crypt.get_decrypt_obj("3kT8kDfWfy5lSO8ZGg+TghFkrkWpKdRRpurukBia94IO37lJfhicHfOeGLH7nPh2G73u8SSEQvb+K+ybej1ciSEvUhDpDdmXmgiO/evRx6Jfef7I02u7aDaAaQxzNfvp")
    print(obj_dec)
    enc_str = crypt.get_encrypt_str({'ExCode': 'SYS001', 'ErrCode': 0, 'ErrText': '获取信息成功！'})
    print(enc_str)