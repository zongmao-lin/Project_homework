#include <stdio.h>
#include <openssl/evp.h>
#include<windows.h>
using namespace std;
#define SM4_KEY_LENGTH 16
#define SM4_BLOCK_SIZE 16

// SM4 ECBģʽ����
void sm4_ecb_enc(const uint8_t* in, uint8_t* out, const uint8_t* key, size_t length)
{
    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
    if (!ctx)
    {
        printf("Fail in creating cipher ctx.\n");
        return;
    }
    if (EVP_EncryptInit_ex(ctx, EVP_sm4_ecb(), NULL, key, NULL) != 1)
    {
        printf("Fail in encrypt init.\n");
        return;
    }
    int outlen1, outlen2;
    if (EVP_EncryptUpdate(ctx, out, &outlen1, in, length) != 1)
    {
        printf("Fail in encrypt update.\n");
        return;
    }
    if (EVP_EncryptFinal_ex(ctx, out + outlen1, &outlen2) != 1)
    {
        printf("Fail in encrypt final.\n");
        return;
    }
    EVP_CIPHER_CTX_free(ctx);
}

// SM4 ECBģʽ����
void sm4_ecb_dec(const uint8_t* in, uint8_t* out, const uint8_t* key, size_t length)
{
    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
    if (!ctx)
    {
        printf("Fail in creating cipher ctx.\n");
        return;
    }
    if (EVP_DecryptInit_ex(ctx, EVP_sm4_ecb(), NULL, key, NULL) != 1)
    {
        printf("Fail in decrypt init.\n");
        return;
    }
    int outlen1, outlen2;
    if (EVP_DecryptUpdate(ctx, out, &outlen1, in, length) != 1)
    {
        printf("Fail in decrypt update.\n");
        return;
    }
    if (EVP_DecryptFinal_ex(ctx, out + outlen1, &outlen2) != 1)
    {
        printf("Fail in decrypt final.\n");
        return;
    }
    EVP_CIPHER_CTX_free(ctx);
}

int main(void)
{
    uint8_t plaintext[SM4_BLOCK_SIZE] = { 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, };
    uint8_t ciphertext[100] = { 0 };
    uint8_t deciphertext[100] = { 0 };
    const uint8_t key[SM4_KEY_LENGTH] = { 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 };
    printf("plaintext:");
    for (int i = 0; i < SM4_BLOCK_SIZE; i++) {
        printf("%02x", plaintext[i]);
    }

    double run_time;
    _LARGE_INTEGER time_start;	//��ʼʱ��
    _LARGE_INTEGER time_over;	//����ʱ��
    double dqFreq;		//��ʱ��Ƶ��
    LARGE_INTEGER f;	//��ʱ��Ƶ��
    QueryPerformanceFrequency(&f);
    dqFreq = (double)f.QuadPart;
    QueryPerformanceCounter(&time_start);	//��ʱ��ʼ

    sm4_ecb_enc(plaintext, ciphertext, key, SM4_BLOCK_SIZE);

    QueryPerformanceCounter(&time_over);	//��ʱ����

    printf("ciphertext: ");
    for (int i = 0; i < SM4_BLOCK_SIZE; i++)
    {
        printf("%02X ", ciphertext[i]);
    }
    printf("\n");
    run_time = 1000000 * (time_over.QuadPart - time_start.QuadPart) / dqFreq;
    //����1000000�ѵ�λ���뻯Ϊ΢�룬����Ϊ1000 000/��cpu��Ƶ��΢��
    printf("\nrun_time��%fus\n", run_time);
    
    return 0;
}