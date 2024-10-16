#include <stdio.h>

void convert_to_binary(int n)
{
    if (n == 0)
        return;

    convert_to_binary(n / 2);
    printf("%d", n % 2);
}

void input_and_convert_to_binary()
{
    int num;

    printf("양의 정수를 입력하세요: ");
    scanf_s("%d", &num);

    if (num == 0)
    {
        printf("0\n");
        return;
    }

    convert_to_binary(num);
    printf("\n"); 
}

int main(void)
{
    input_and_convert_to_binary();
    return 0;
}
