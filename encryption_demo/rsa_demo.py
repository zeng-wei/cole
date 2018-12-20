from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5


def create_rsa_key(password="123456"):
    key = RSA.generate(2048)  # 生成 2048 位的 RSA 密钥
    encrypted_key = key.exportKey(
        # passphrase=password,
        # pkcs=8,
        # protection="scryptAndAES256-CBC"
    )  # 生成私钥
    with open("./encryption_demo/private.pem", "wb") as f:
        f.write(encrypted_key)
    with open("./encryption_demo/public.pem", "wb") as f:
        f.write(key.publickey().exportKey())  # 生成公钥


def encrypt_and_decrypt_test(password=b"123456"):
    # 加载公钥
    recipient_key = RSA.import_key(
        open("./encryption_demo/public.pem").read()
    )
    cipher_rsa = PKCS1_v1_5.new(recipient_key)
    en_data = cipher_rsa.encrypt(password)
    print(len(en_data), en_data)
    # 读取密钥
    private_key = RSA.import_key(
        open("./encryption_demo/private.pem").read(),
        # passphrase=password
    )
    cipher_rsa = PKCS1_v1_5.new(private_key)
    data = cipher_rsa.decrypt(en_data, None)
    print(data)


def rsa_encrypt(bytes_content):
    rsakey = RSA.importKey(open("./encryption_demo/public.pem").read())
    cipher = PKCS1_v1_5.new(rsakey)
    return cipher.encrypt(bytes_content)


def rsa_long_decrypt(msg, length=128):
    res = []
    for i in range(0, len(msg), length):
        m = rsa_encrypt(msg[i:i+length])
        if m:
            res.append(m)
    return b"".join(res)


def enc_common_demo():
    s = b"password"
    encrypt_and_decrypt_test(s)


def enc_long_text_demo():
    s = b"password" * 1000
    print(rsa_long_decrypt(s))


if __name__ == '__main__':
    enc_common_demo()
    enc_long_text_demo()
    # create_rsa_key()