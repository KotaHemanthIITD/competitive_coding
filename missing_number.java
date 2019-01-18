import java.util.Scanner; 

public class missing_number{

     public static void main(String []args){
         int n = -1;
         Scanner s = new Scanner(System.in);
         n = s.nextInt();
         int arr[] = new int[n];         
         for(int i = 0; i<(n-1); i++){
             arr[i] = s.nextInt();
             System.out.println("arr i item :" + Integer.toString(arr[i]));
         }
         int start = 0;
         int end = n-2;
         boolean found = false;
         int mid,out=-1;
         while(!found){            
            mid = (start + end)/2;
            if(mid == end){ 
                if(arr[mid] > mid+1)
                    out = arr[mid]-1;
                else 
                    out = arr[mid]+1;
                found = true;
            }
            
            if( arr[mid] > (mid+1) )
            {
                end = mid;
            }
            else if(arr[mid] <= (mid+1))
            {
                start = mid+1;
            }
         }
         System.out.println("Missing number is : " + Integer.toString(out));
        // System.out.println("Hello World");
     }
}