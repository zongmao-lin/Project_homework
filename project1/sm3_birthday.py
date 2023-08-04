import random
import time
from gmssl import sm3, func

#将随机数转换为字符串，并用库函数加密，得到随机字符序列
randomtext = str(random.random())
textlen = len(randomtext)
rhash = sm3.sm3_hash(func.bytes_to_list(bytes(randomtext, encoding='utf-8')))

#生日攻击
def Birthday_attack(attacklen):
    num = int(2 ** (attacklen / 2))
    ans = [-1] * 2**attacklen
    #循环遍历，对于每一位
    for i in range(num):
        temp = int(rhash[0:int(attacklen / 4)], 16)
        if ans[temp] == -1:
            ans[temp] = i
        else:
            return hex(temp)

if __name__ == '__main__':
    attack_len = int(input("请输入攻击长度："))
    start = time.time()
    for i in range(10):
        res = Birthday_attack(attack_len)
    
    end = time.time()
    print("前",attack_len,"位碰撞结果为",res)
    print(end- start,'seconds\n')
    
