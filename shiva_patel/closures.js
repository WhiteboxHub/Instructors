var x =10;
console.log(x);
const fun1 = function(){
    var y = 20;
    console.log(x,y);
    const fun2 = function(){
        var z =30;
        console.log(x,y,z);
    }
    fun2();
}
fun1();