from gmssl import sm2, sm4 # Import sm2 and sm4 libraries for SM2/SM4 encryption
import random # For generating random numbers
import time # For timing system

# 生成随机数的字符串
salt_string = "shandongdaxue202000460066yangkaige00"

# 加密初始矢量
init_vector = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
pri_key = '010203040506070809000A0B0C0D0E0F010203040506070809000A0B0C0D0E0F01'
pub_key = '04E9C91B81872260BEF331A83081A693747D7EA88042927317EB06B9C9A6EF5DDEB0BB2FF6CF5AF347B483F7B9487C018FB4162B8993F3F5D6EADDDE24620207'

# 使用salt_string中的元素生成随机k_val的函数
def random_k_generator():
    k_val = ""
    for i in range(16):
        k_val += salt_string[random.randrange(36)]
    return k_val.encode('utf-8')

# 用于加密数据和会话密钥的函数
def sender_function(msg_to_send):
    #生成一个随机密钥
    random_k = random_k_generator()
    
    #初始化SM4加密对象
    sm4_enc_obj = sm4.CryptSM4()
    
    #设置加密密钥
    sm4_enc_obj.set_key(random_k, sm4.SM4_ENCRYPT)
    
    #加密
    encrypted_message = sm4_enc_obj.crypt_ecb(msg_to_send.encode("utf-8"))
    
    #初始化SM2加密对象
    sm2_enc_obj = sm2.CryptSM2(public_key=pub_key, private_key="")
    
    #加密密钥
    encrypted_key = sm2_enc_obj.encrypt(random_k)
    
    return encrypted_message, encrypted_key

# 解密
def receiver_function(encrypted_message, encrypted_key):
    # 设置SM2加密
    sm2_enc_obj = sm2.CryptSM2(public_key=pub_key, private_key=pri_key)
    
    #解密密钥
    decrypted_key = sm2_enc_obj.decrypt(encrypted_key)
    
    #设置SM4解密器
    decryptor_sm4 = sm4.CryptSM4()
    
    #设置解密器的密钥
    decryptor_sm4.set_key(decrypted_key, sm4.SM4_DECRYPT)
    
    #解密消息
    decrypted_message = decryptor_sm4.crypt_ecb(encrypted_message)
    
    return decrypted_message.decode("utf-8")


user_message = input("Input the message to be encrypted:\n")
start_time = time.time()

# 发送消息
enc_msg, enc_key = sender_function(user_message)

# 接收消息
returned_message = receiver_function(enc_msg, enc_key)
end_time = time.time()

print("Encrypted message is: ", enc_msg)
print("Encrypted session key is: \n",enc_key)

if returned_message == user_message:
    print("Success!")

print("Time elapsed:", end_time - start_time, 'seconds')
