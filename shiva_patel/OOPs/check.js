function eliminateDuplicates(input){
    if(input === undefined || input === null || typeof(input) == !String){
        throw new Error("intput is not a string")
    }
    const charMap = {};
    for(let i = 0;i<input.length;i++){
        const currentChar = input[i];
        if (!charMap[currentChar]){
            charMap[currentChar]= true;
        }
    }
    const uniqueString = Object.keys(charMap).join("")
    return uniqueString;
}
const input = "shivakumaar";
const result = eliminateDuplicates(input);
console.log(result);