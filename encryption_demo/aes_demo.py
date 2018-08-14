from Crypto.Cipher import AES
import base64


class AESCrypt:
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC
        self.aes = AES.new(self.key, self.mode, self.key)

    def encrypt(self, text):
        length = 16  # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度. 不足就补足
        count = len(text)
        if count % length != 0:
            add = length - (count % length)
        else:
            add = 0
        text = text + (b'\x00' * add)
        return self.aes.encrypt(text)

    def decrypt(self, text):
        plain_text = self.aes.decrypt(text)
        return plain_text.rstrip(b'\x00')  # 解密后，去掉补足的空格用strip() 去掉


if __name__ == '__main__':
    pc = AESCrypt('irap1704irap1704')  # 初始化密钥
    # first:base64 decode
    c = base64.b64decode("zpSihbgHrUwsOqs3cMvfSiVfyFcIUK65qq7i77mUbxbPgsE/4lqeB2uUHky6rii+3QSMNrn4+KdGp4rHjvP8yCEfW96oFD8lgQMNUFUtAJvAoWQFRdPwT1SUw4Psmj9iM6HqRURNDNZ0hmSGXOEbhvUmNNQDWSwmaBdYCIG8J7sz0RjHEFqAzsuf64kyw4HLhPLofa8k0h28nM7ujFFumvaRMIWJoc18AFEQA2RAH0rAkJpeeo8xO70jsxK8Om1fMYx1aM58c8CW9yME8mhXbMRGzwueWr9ndFESXeXA3jh+Rfm+uE1nocHWWG2J7U54aK2F/AwPrsL8SoAM+brGQHcomsz/ofhkzjuLVltqz9LH5B1+uyogP06UhFjMnZ8CCFVq/b0GnES8rAV7Fn1iq7IHMVm2QlWmcF4zjybRGJvHOt8Bg+7boWGLy/TXay/VlfkAxn7KSHi14+NpA3kz3kFVee8pDRe71v3OidEOPx69cQLEbEf3rWp2UhMMt8cXuBhUgVJB4UTUiMek9cLmBQ==")
    d = pc.decrypt(c)  # AES decode
    print(d.decode())
    print(base64.b64encode(pc.encrypt(d)))