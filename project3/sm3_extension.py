from gmssl import sm3, func

def padded_message(input_message):
    input_length = len(input_message)
    remainder = input_length % 64
    input_message.append(0x80)
    remainder += 1
    range_stop = 56
    if remainder > range_stop:
        range_stop += 64
    for counter in range(remainder, range_stop):
        input_message.append(0x00)
    
    bit_length = input_length * 8
    bit_length_str_arr = [bit_length % 0x100]
    for counter in range(7):
        bit_length = int(bit_length / 0x100)
        bit_length_str_arr.append(bit_length % 0x100)
    for counter in range(8):
        input_message.append(bit_length_str_arr[7-counter])
    return input_message

def run_length_extension_attack():
    Message=b"happy"
    Additional_msg=b"world"

    Message1 = padded_message(func.bytes_to_list(Message))
    Added_msg = Message1 + func.bytes_to_list(Additional_msg)
    sm3_hash1=sm3.sm3_hash(Added_msg)

    sm3_hash2 = sm3.sm3_hash(func.bytes_to_list(Message))
    IV_arr = []
    for counter in range(0,8):
        IV_arr.append(int(sm3_hash2[counter*8:(counter+1)*8],16))
    Message2 = padded_message(Added_msg)
    sm3_cf_hash = sm3.sm3_cf(IV_arr,Message2[64:128])
    Hashed_value2=""

    for item in sm3_cf_hash:
        Hashed_value2 = '%s%08x' % (Hashed_value2, item)
    
    if sm3_hash1==Hashed_value2:
        print("完成长度拓展攻击")
        print("SM3 Hash值为:",sm3_hash1)

if __name__ == '__main__':
    run_length_extension_attack()
