import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner x = new Scanner(System.in);
		String y = x.next();
		int z = x.nextInt();
		int l = y.length();
		while(z<l)
		{
		 	System.out.print(y.charAt(z));  
		 	z = z + 1;
		}
	}
}
