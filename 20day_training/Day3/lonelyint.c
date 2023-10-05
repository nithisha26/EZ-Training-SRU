#include<stdio.h>
main()
{
	int a[6]={10,20,30,20,10,10};
	int i=0,lonely_int=0;
	for(i=0;i<6;i++)
	{
		lonely_int=lonely_int^a[i];
	}
	printf("%d",lonely_int);
}
