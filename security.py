from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
import base64

PASSWORD = os.getenv('benchmark_password')

def pad_to_16_bytes(s):
    """
    将字符串编码为UTF-8字节序列，并确保长度为16位。
    如果长度不足16位，则在末尾添加填充字节以达到16位。

    :param s: 原始字符串
    :return: 长度为16位的字节序列
    """
    encoded = s.encode('utf-8')
    padding_length = 16 - (len(encoded) % 16)
    padded = encoded.ljust(len(encoded) + padding_length, b'\x00')
    return padded[:16]

def encrypt(plaintext, password):
    # 密钥长度必须为16字节（128位），这里简单地取前16个字节
    key = pad_to_16_bytes(password)

    # 生成一个随机的初始化向量IV
    iv = os.urandom(16)

    # 创建一个新的AES Cipher实例
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)

    # 对明文进行填充
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext.encode('utf-8')) + padder.finalize()

    # 加密
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    combined_data = iv + ciphertext
    encoded_ciphertext = base64.b64encode(combined_data).decode('utf-8')
    return encoded_ciphertext


def decrypt(ciphertext, password):
    # 密钥长度必须为16字节（128位），这里简单地取前16个字节
    key = pad_to_16_bytes(password)

    # 将Base64编码的字符串转换回字节序列
    combined_data = base64.b64decode(ciphertext.encode('utf-8'))

    # 提取出IV部分
    iv = combined_data[:16]
    ciphertext = combined_data[16:]

    # 创建一个新的AES Cipher实例
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)

    # 解密
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # 去除填充
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext.decode('utf-8')

def decrypt_config(config):
    return decrypt(config, PASSWORD)

if __name__ == "__main__":
    plaintext = "Hello World!"
    password = "aaabbb"
    encrypted_data = encrypt(plaintext, password)
    print("Encrypted data:", encrypted_data)

    decrypted_data = decrypt(encrypted_data, password)
    print("Decrypted data:", decrypted_data)
