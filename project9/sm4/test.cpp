#include"sm4_1.h"
using namespace std;
#include"time.h"
#include<windows.h>
void key_random(uint32_t* buff, int length)
{
    int i = 0;
    srand((unsigned) time(NULL));
    for (i = 0; i < length; i++)
    {
        //buff[i] = rand() % (sizeof(uint32_t)*256);
        buff[i] = 0;
    }

   // buff[length] = '\0';

}

//int main() {
//    double run_time;
//    _LARGE_INTEGER time_start;	//开始时间
//    _LARGE_INTEGER time_over;	//结束时间
//    double dqFreq;		//计时器频率
//    LARGE_INTEGER f;	//计时器频率
//    QueryPerformanceFrequency(&f);
//    dqFreq = (double)f.QuadPart;
//    QueryPerformanceCounter(&time_start);	//计时开始
//  
//    uint32_t key[4], rk[32];
//    uint32_t msg[] = { 0x30303030,0x30303030,0x30303030,0x30303030 };
//    uint32_t c[100086], ans[10086];
//    key_random(key, 4);
//    keygen(key, rk);
//    enc0(msg, c, rk);
//    dec0((uint32_t*)c, (uint32_t*)ans, rk);
//    QueryPerformanceCounter(&time_over);	//计时结束
//    for (int i = 0; i < 4; i++) {
//        printf("%02x ", c[i]);
//    }
//    run_time = 1000000 * (time_over.QuadPart - time_start.QuadPart) / dqFreq;
//    //乘以1000000把单位由秒化为微秒，精度为1000 000/（cpu主频）微秒
//    printf("\nrun_time：%fus\n", run_time);
//
//    
//    return 0;
//}