public class NonZeroPush {

    // Program to  push zero elements to the last of an array
    public static void main(String[] args) {
        int arr[]={1,2,0,3,4,0,5};
        // Intializing nonZeroElements to  0
        int nonZeroElement = 0;
        // Iterating through the array
        for( int i =0; i<=arr.length-1; i++){
            //Edge condition for pushing non- zero elements to ahead of an array

            if(arr[i]!=0){
                arr[nonZeroElement++] = arr[i];
                // nonZeroElement++;
            }

        }

        //now pushing remaining non-zero elements to last of an array
        
        while(nonZeroElement<arr.length)
        {
             arr[nonZeroElement++] = 0;
        }
        
        for (int j =0;j<=arr.length-1;j++){
            System.out.println(arr[j]);
            }
        

    }
}
