/* anonymous functions:
(function(){
    console.log('anonymous function ');
})
();

parameters & arguments

var a =100,b=200,c=300,d=400;// parameters
function add(a,b){
    return a+b;
}
console.log(add (a,b));//arguments
console.log(add (c,d));
console.log(add (a,b));
*/


var obj1 =
{
    fName:'sai',
    lName:'ram',
    fullName:function()
    {
        return (`${this.fName}${this.lName}`)
    }
}
console.log(obj1.fullName());