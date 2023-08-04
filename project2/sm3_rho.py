import random
import time
from gmssl import sm3, func

def find_collision(bit_len):
    # 使用随机数生成一个随机消息，长度为给定的比特长度
    msg = hex(random.randint(0, 2**(bit_len+1)-1))[2:]
    #计算哈希值
    hash_1 = sm3.sm3_hash(func.bytes_to_list(msg.encode()))
    # 根据第一个哈希值计算第二个哈希值
    hash_2 = sm3.sm3_hash(func.bytes_to_list(hash_1.encode()))
    # 初始化计数器
    counter = 1
    # 当第一个哈希值和第二个哈希值的前n个比特不同时，继续进行哈希计算
    while hash_1[:bit_len//4] != hash_2[:bit_len//4]:
        counter += 1
        hash_1 = sm3.sm3_hash(func.bytes_to_list(hash_1.encode()))
        hash_2 = sm3.sm3_hash(func.bytes_to_list(sm3.sm3_hash(func.bytes_to_list(hash_2.encode())).encode()))
    # 在找到碰撞前，进行哈希计算的次数
    for _ in range(counter):
        # 若两个哈希值的前n个比特相同，则找到了碰撞
        if sm3.sm3_hash(func.bytes_to_list(hash_1.encode()))[:bit_len//4] == sm3.sm3_hash(func.bytes_to_list(hash_2.encode()))[:bit_len//4]:
            return [hash_1, hash_2, sm3.sm3_hash(func.bytes_to_list(hash_1.encode()))[:bit_len//4]]
        # 否则继续进行哈希计算
        else:
            hash_1 = sm3.sm3_hash(func.bytes_to_list(hash_1.encode()))
            hash_2 = sm3.sm3_hash(func.bytes_to_list(hash_2.encode()))

if __name__ == "__main__":
    n = int(input("请输入攻击比特长度：\n"))
    start = time.time()
    result = find_collision(n)
    end = time.time()
    print("消息一：", result[0])
    print("消息二：", result[1])
    print("碰撞值：", result[2])
    print("攻击时间: {:.6f} 秒\n".format(end-start))
