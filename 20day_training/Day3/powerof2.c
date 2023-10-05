//to check whether a number is power of 2
#include<stdio.h>
main()
{
	int count=0,n=32;
	while(n)
	{
		count++;
		n=n&(n-1);
	}
	if(count==1)
	printf("true");
	else
	printf("false");
}
/*  to check whether a number is power 4
    n=n&(n-2)  */
