/**
 * sample
 */
import java.util.*;
public class sample {

    public static void main(String[] args) {

        System.out.println("Merge arrays");

        Scanner scan = new Scanner(System.in);

        System.out.println("Enter first array size");

        int size1 = scan.nextInt();

        System.out.println("enter Second array size");

        int size2 = scan.nextInt();
        

        int []arr1 = new int [size1];
         

        int []arr2 = new int [size2];

        int [] arr3 = new int [size1+size2];

        System.out.println("Enter first array elements");

        for(int i = 0; i<arr1.length  ; i++)
        {
            arr1[i] = scan.nextInt();
        }
        
        System.out.println("Enter second array elements");

        for(int j = 0; j<arr2.length  ; j++)
        {
            arr2[j] = scan.nextInt();
        }

        System.out.println("Merging into 3rd array");

        for(int k =0; k<arr3.length;k++)
        {
            if(k<=arr1.length-1)
            {
                arr3[k] = arr1[k];
            }
            else
            {
                arr3[k] = arr2[k-arr1.length];
            }
        }

        System.out.println("Printing the 3rd array");

        for(int z=0;z<arr3.length;z++)
        {
            System.out.println(arr3[z]);
        }

        int largest = arr3[0];

        System.out.println("Finding the largest number from that array");
        for(int x=1;x<arr3.length;x++){
            if(largest<=arr3[x])
            {
                largest = arr3[x];
            }
        }
        System.out.println(largest);


    }
}
