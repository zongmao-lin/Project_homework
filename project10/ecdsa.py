from pycoin.ecdsa import generator_secp256k1, sign, verify
import hashlib, secrets

class ECDSA:

    #哈希函数
    @staticmethod
    def sha3_256Hash(msg):
        hashBytes = hashlib.sha3_256(msg.encode("utf8")).digest()
        return int.from_bytes(hashBytes, byteorder="big")

    #将私钥和消息签名进行对应
    @staticmethod
    def sign_message(msg, privKey):
        msgHash = ECDSA.sha3_256Hash(msg)
        signature = sign(generator_secp256k1, privKey, msgHash)
        return signature

    #验证签名是否与消息和公钥相符
    @staticmethod
    def verify_message(msg, signature, pubKey):
        msgHash = ECDSA.sha3_256Hash(msg)
        valid = verify(generator_secp256k1, pubKey, msgHash, signature)
        return valid

#将上述函数进行具体使用来进行验证
if __name__ == "__main__":

    # ECDSA签署消息
    msg = "Message for ECDSA signing"
    private_key = secrets.randbelow(generator_secp256k1.order())
    signature = ECDSA.sign_message(msg, private_key)
    print("消息:", msg)
    print("私钥:", hex(private_key))
    print("签名: r=" + hex(signature[0]) + ", s=" + hex(signature[1]))

    # 创建一个公钥并用以验证签名
    public_key = (generator_secp256k1 * private_key).pair()
    valid = ECDSA.verify_message(msg, signature, public_key)
    print("\n消息:", msg)
    print("公钥: (" + hex(public_key[0]) + ", " + hex(public_key[1]) + ")")
    print("签名是否有效?", valid)

    # ECDSA验证篡改签名
    tampered_msg = "Tampered message"
    valid = ECDSA.verify_message(tampered_msg, signature, public_key)
    print("\n消息:", tampered_msg)
    print("签名是否有效(篡改后)?", valid)
