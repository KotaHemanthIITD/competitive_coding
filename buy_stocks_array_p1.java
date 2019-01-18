import java.util.*;
public class buy_stocks_array_p1{
	public static void main(String args[]){
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		int[] arr = new int[n];
		int lmin = 0, lmax = 0;
		for(int i=0;i<n;i++){
			arr[i] = s.nextInt();
			if(arr[i] < arr[lmin])
			{
				lmin = i;
			}
			if(arr[i] > arr[lmax])
			{
				lmax = i;
			}
		}
		int out = 0;
		if(lmin<lmax)
			out = arr[lmax]-arr[lmin];
		else if(lmax==0&&lmin==(n-1))
			out = 0;
		else if(lmin>lmax){
			int tmn=lmax, tmx=lmin;
			for(int i=(lmin+1);i<n;i++){
				if(arr[i] > arr[tmx])
					tmx = i; 
			}
			for(int i=0;i<lmax;i++)
			{
				if(arr[i]<arr[tmn])
					tmn = i;
			}
			out = arr[tmx]-arr[lmin];
			if ((arr[lmax]-arr[tmn]) > (arr[tmx]-arr[lmin]))
				out = arr[lmax]-arr[tmn];
		}
		System.out.println(" Max profit : " + Integer.toString(out));
	}
}