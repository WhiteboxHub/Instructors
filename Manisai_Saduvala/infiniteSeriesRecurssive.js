// Infinite series of arguments sum by recursion
/* Unit Test cases
   if a function has 2 calling arguments
   add(1)(2)=3;
   add(1)(2)(3)=6;
   add(1)(2)(3)(4)....(n)=?
   constraints -> return function recursievly 
*/
// Declaring a function with one parameter
function addInfiniteArgs(num)
{
    // return another function with the series parameters
    return function(num1)
    {
        // if there exist a series parameters
        if (num1)
        {
            // Return there sum of infinite series
            return addInfiniteArgs(num+num1);
        }
        // else return the sum to turnicate the excecution
        return num;
    }

}
console.log(addInfiniteArgs(1)(2)());

 // we can also make use of Es6 features for the above code
let sum=(x)=>y=>y?sum(x+y):x;
console.log(sum(1)(2)());
