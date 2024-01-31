function sum(n1, n2, next){
    sum = n1+n2;
    console.log(next(sum))

}
function s( n){
    return n**sum;
}
sum(10,20,s)
// here s is callback function
// and sum is the higher order function
