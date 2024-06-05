let map1 = new Map();
map1.set(101,"shiva")
console.log(map1);
const key1 = " hello ", key2 = { }, key4 = function(){};
map1.set(key1,"hello shiva");
map1.set(key2, "object");
map1.set(key4,"function")
//console.log(map1);
// getting values from map
//console.log(map1.get(key1))

// getting size of a maps
//console.log(map1.size)

// we can use loops to print keys and values 
for ( const [k,v] of map1){
   // console.log(k, " : ", v)
}

// we can get only key by using lops
for(const key of map1.keys()){
    console.log(key)
}
// with foreach loop
map1.forEach((value ,key ) => {
  //  console.log(value ,key)
})

for(const value of map1.values()){
    console.log(value)
}