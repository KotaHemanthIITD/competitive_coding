import java.util.*;

/*

	we have better solution with respect to memory by negating the element at index of arr[i]
	1 2 6 1 6 2

*/

public class duplicates_array{	
	public static void main(String []args){
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		/*Checking proper in take of array size*/
		System.out.println("size of arrays is : " + Integer.toString(n));
		int[] arr = new int[n+1];		
		for(int i=0; i<n; i++){
			arr[s.nextInt()] += 1;
		}
		/* Checking the array entires */
		for(int i=0;i<=n;i++){
			System.out.println( " Elements of Repetition Array : " + Integer.toString(arr[i]));
		} 
		Vector out = new Vector(n+1,1);
		for(int i=0; i<=n; i++){
			if(arr[i] > 1)
			{
				out.add(i);
			}
		}
		System.out.println(out);
	}
}