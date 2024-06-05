// Checking whether a given String is Palindrome or not using pointers
// Unit Test cases
//  length>1 && left pointer char == right pointer char
// For example given string of length n 
// input= MOM, so return palindrome 
function pointerPalindrome(name)
{
    // pointing header to the intial index

    let header = 0;
    // pointing tailer to the last index

    let tailer = name.length-1;
    // Base condition for checking whether the string has more than 0 chars and checking whether every char is equal or not

    if (name.length<1 || name[header]!==name[tailer])
    {
        return -1;
    }
    // Condition for breaking the loop at a certain or needed time

    while(header<=tailer)
    {
        // condition for equal characters

        if (name[header]==name[tailer])
        {
            header++;
            tailer--;
        }
        else{
        return "not palindrome"
        }

    }
    return 'palindrome'
}
console.log(pointerPalindrome('MOON'));

// Big O-notation = O(n) Linear
