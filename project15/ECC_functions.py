from gmssl import sm2
import random

CONST_P = 'FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFF'
CONST_G = '32C4AE2C1F1981195F9904466A39C9948FE30BBFF2660BE1715A4589334C74C7BC3736A2F4F6779C59BDCEE36B692153D0A9877CC62A474002DF32E52139F0A0'
CONST_N = 'FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123'

def inverse(u, v):
    u3, v3 = u, v
    u1, v1 = 1, 0
    while v3 > 0:
        quotient = divmod(u3, v3)[0]
        u1, v1 = v1, u1 - v1 * quotient
        u3, v3 = v3, u3 - v3 * quotient
    while u1 < 0:
        u1 = u1 + v
    return u1

def generate_element(): 
    return random.randint(1, int(CONST_N, 16) - 1)

def generate_opposite_point(point_G):
    sm2_instance = sm2.CryptSM2(private_key="", public_key="")
    len_point = len(point_G)
    x_coord_val = point_G[0:sm2_instance.para_len]
    y_coord_val = point_G[sm2_instance.para_len:len_point]
    y_coord_val = int(y_coord_val, 16)
    y_coord_val = (-y_coord_val) % int(CONST_P, 16)
    y_coord_val = hex(y_coord_val)[2:]
    opp_G = x_coord_val + y_coord_val
    return opp_G

def create_pub_key(element, P1):
    modulo_16 = int(CONST_N, 16)
    sm2_inst = sm2.CryptSM2(private_key="", public_key="")
    temp_point = sm2_inst._kg(inverse(element, modulo_16), P1)
    opp_G = generate_opposite_point(CONST_G) # -G
    result = sm2_inst._add_point(temp_point, opp_G) # Adding two points
    result = sm2_inst._convert_jacb_to_nor(result) # Obtaining the final x||y
    return result

def generate_elements(element2, Q1, e):
    modulo_16 = int(CONST_N, 16)
    sm2_instance = sm2.CryptSM2(private_key="", public_key="")
    factor2 = generate_element()
    Q2 = sm2_instance._kg(factor2, CONST_G)
    factor3 = generate_element()
    temp_point = sm2_instance._kg(factor3, Q1)
    result = sm2_instance._add_point(temp_point, Q2) # Adding two points
    result = sm2_instance._convert_jacb_to_nor(result) # Obtaining the final x||y
    x1 = int(result[0:sm2_instance.para_len], 16)
    r = (x1 + int(e.hex(), 16)) % modulo_16
    s2 = (element2 * factor3) % modulo_16
    s3 = element2 * (r + factor2) % modulo_16
    return (r, s2, s3)
