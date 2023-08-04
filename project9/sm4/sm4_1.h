#ifndef OSSL_CRYPTO_SM4_H
# define OSSL_CRYPTO_SM4_H
# pragma once

#include<stdint.h>
#include<stdlib.h>
#include<time.h>
#include<stdio.h>

# ifdef OPENSSL_NO_SM4
#  error SM4 is disabled.
# endif

# define SM4_ENCRYPT     1
# define SM4_DECRYPT     0

# define SM4_BLOCK_SIZE    16
# define SM4_KEY_SCHEDULE  32

typedef struct SM4_KEY_st {
    uint32_t rk[SM4_KEY_SCHEDULE];
} SM4_KEY;

int keygen(const uint32_t key[4], uint32_t *rk);

void enc0(uint32_t in[4], uint32_t out[4],uint32_t rk[32]);

void enc1(uint32_t in[4], uint32_t out[4],uint32_t rk[32]);

void dec0(uint32_t x[4], uint32_t out[4],uint32_t rk[32]);

#endif
