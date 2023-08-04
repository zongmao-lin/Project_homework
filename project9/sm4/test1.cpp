#include <fstream>
#include <iostream>
#include "sm4_data.h"
using namespace std;

static size_t getFileSize(FILE* file) {
    fseek(file, 0, SEEK_END);
    size_t read_len = ftell(file);
    fseek(file, 0, SEEK_SET);
    return read_len;
}
int readFromFile1(uint32_t* buf) {
    const char* filePath = "E:/HLS/SM4_code/video.mp4";
    FILE* file = fopen(filePath, "rb");
    size_t fileSize = getFileSize(file);
    if (fileSize != 0) {
        size_t n = fread(buf, sizeof(uint32_t), fileSize, file);
    }
    fclose(file);
    return fileSize;
}

void key_random(uint32_t* buff, int length)
{
    int i = 0;
    srand((unsigned) time(NULL));
    for (i = 0; i < length; i++)
    {
        buff[i] = rand() % (sizeof(uint32_t)*256);
    }

    buff[length] = '\0';

}

int main() {
    uint32_t key[4],rk[32];
    key_random(key, 4);
    keygen(key,rk);
    uint32_t buf[180000],out[180000];
    size_t len = readFromFile1(buf);
//    len = 200;
//    uint32_t ans[200];
    printf("%d\n",len);
    enc_ecb(buf,len,out,rk);
//    dec_ecb(out,len,ans,rk);
//    for(int i = 0; i < len; i++){
//    	printf("%d",ans[i]==buf[i]);
//    }
    return 0;
}
