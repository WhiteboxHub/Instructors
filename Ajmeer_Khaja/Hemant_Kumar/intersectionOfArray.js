function intersection(nums1, nums2) {
    // const result = [];

    // for (let num1 of nums1) {
    //     for (let num2 of nums2) {
    //         if (num1 === num2 && !result.includes(num1)) {
    //             result.push(num1);
    //             break; // Move to the next element in nums1 once a match is found
    //         } 
    //     }
    // }

    // return result;
const result=[]
    for(ele of nums1 ){
        for(ele1 of nums2){
                if(ele== ele1 && !result.includes(num1) )
                result.push(ele);
            break;
        }
    }
}

console.log(intersection([1,2,3,4,5],[2,5,6,3,6]));
