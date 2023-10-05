//to check whether the given position has set bit or not
#include<stdio.h>
main()
{
	int val=12,pos=2;
	int bitmask=1<<(pos-1);
	if(val&bitmask)
	{
		printf("true");
	}
	else
	{
		printf("false");
	}
	
}
