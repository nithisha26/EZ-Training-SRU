import java.util.Scanner;
import java.lang.String;
public class stringrevspcl
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
		String input=sc.nextLine();
		String str="";
		for(int i=0;i<input.length();i++)
		{
			if (Character.isDigit(input.charAt(i))
                || Character.isLetter(input.charAt(i)))
			{
				str=input.charAt(i)+str;
			}
		}
		String finalstr="";
		for(int i=0,j=0;i<input.length();i++)
		{
			if(Character.isDigit(input.charAt(i))
                || Character.isLetter(input.charAt(i)))
			{
				char ch=str.charAt(j);
				finalstr+=ch;
				j++;
			}
			else{
				char ch=input.charAt(i);
				finalstr+=ch;
			}
		}
		System.out.print(finalstr);
	}
}

