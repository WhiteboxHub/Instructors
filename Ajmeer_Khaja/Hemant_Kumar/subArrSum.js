function subArraySum(arr){
    
let sum=0,max=arr[0]
for(let i=0;i<arr.length;i++){
    sum+=arr[i]
    if(sum>max)
    max=sum
if(sum<0)
sum=0

}
return max
}
console.log( subArraySum([-2,1,-3,4,-1,2,1,-5,4]))


// Unit Test Cases ------------

// Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
// Expected Output: 6


// Input: nums = [1]
// Expected Output: 1

// Input: nums = [5,4,-1,7,8]
// Expected Output: 23
