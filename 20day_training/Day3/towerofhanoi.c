#include <stdio.h>
void towerofhanoi(int n,char s,char h,char d)
{
    if(n==1)
    {
        printf("transfer disk %d from %c to %c\n",n,s,d);
        return;
    }
    else
    {
        towerofhanoi(n-1,s,d,h);
        printf("transfer disk %d from %c to %c\n",n,s,d);
        towerofhanoi(n-1,h,s,d);
    }
}
int main()
{
    int n;
    scanf("%d",&n);
    towerofhanoi(n,'s','h','d');
}
