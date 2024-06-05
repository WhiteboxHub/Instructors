//ElemenatingDuplicatesinString
function elemenatingDuplicatesinString(input){
     if(input === null || input === undefined || typeof(input) === !String){
        throw new Error("the input must be string")
     }
     const charMap = {};
     for( let i =0;i<input.length ; i++){
        const currentchar = input[i];

        if(!charMap[currentchar]){
            charMap[currentchar] = true;
        }
     }
     const uniqueString = Object.keys(charMap).join("");
     return uniqueString
}
console.log(elemenatingDuplicatesinString("shivapatel"));