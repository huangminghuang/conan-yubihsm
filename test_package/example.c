#include <yubihsm.h>
#include <stdio.h>

int main()
{
    yh_init();
    yh_exit();
    printf("Hello\n");
    return 0;
}