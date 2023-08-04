#include<stdint.h>
#include<stdlib.h>
#include<time.h>
#include<stdio.h>

# define SM4_ENCRYPT     1
# define SM4_DECRYPT     0

# define SM4_BLOCK_SIZE    16
# define SM4_KEY_SCHEDULE  32

int keygen(const uint32_t key[4], uint32_t *rk);

void enc1(uint32_t in[4], uint32_t out[4],uint32_t rk[32]);

void enc_ecb(uint32_t in[180000], uint16_t inlen, uint32_t out[180000], uint32_t rk[32]);

void dec_ecb(uint32_t in[180000], uint16_t inlen, uint32_t out[180000], uint32_t rk[32]);

void dec0(uint32_t x[4], uint32_t out[4],uint32_t rk[32]);

