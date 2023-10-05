//input one matrix and the fire start from '1' i.e is in (0,0)
//and the fire goes around all the trees connected to it 
//find the no.of unburned trees
import java.util.Scanner;

public class treendfire {
    static void fun(int[][] arr,int i,int j,int n)
    {
        if(arr[i][j]==0)
        return;
        if(arr[i][j]==1)
        arr[i][j]=0;
        if(i>0)
        fun(arr,i-1,j,n);//top
        if(i<n-1)
        fun(arr,i+1,j,n);//bottom
        if(j>0)
        fun(arr,i,j-1,n);//left
        if(j<n-1)
        fun(arr,i,j+1,n);//right
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
		fun(arr,0,0,n);
		for(int i=0;i<n;i++)
		{
		    for(int j=0;j<n;j++)
		    {
		        if(arr[i][j]==1){
		            count++;
		        }
		    }
		}
		
		System.out.print(count);
	}
}
