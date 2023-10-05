//input a binary matrix consisting of 0 and 1
//0 repesents water and 1 represents land
//find no.of islands
import java.util.*;
public class Island
{
    static void fun(int[][] arr,int i,int j,int n)
    {
        if(arr[i][j]==0)
        return;
        if(arr[i][j]==1)
        arr[i][j]=0;
        if(i>0)
        fun(arr,i-1,j,n);
        if(i<n-1)
        fun(arr,i+1,j,n);
        if(j>0)
        fun(arr,i,j-1,n);
        if(j<n-1)
        fun(arr,i,j+1,n);
    }
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int[][] arr=new int[n+1][n+1];
		for(int i=0;i<n;i++)
		{
		    for(int j=0;j<n;j++)
		    {
		        arr[i][j]=sc.nextInt();
		    }
		}
		int count=0;
		for(int i=0;i<n;i++)
		{
		    for(int j=0;j<n;j++)
		    {
		        if(arr[i][j]==1){
		            count++;
		            fun(arr,i,j,n);
		        }
		    }
		}
		System.out.print(count);
	}
}
