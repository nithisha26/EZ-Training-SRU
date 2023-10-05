#include <stdio.h>
long long int fact(long long int n)
{
    if(n==1||n==0)
    return 1;
    else
    return n*fact(n-1);
}
int main()
{
    long long int n;
    scanf("%lld",&n);
    printf("%lld",fact(n));
}
