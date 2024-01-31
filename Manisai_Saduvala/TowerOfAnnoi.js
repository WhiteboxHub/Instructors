// Tower of anoi
// Test cases
// Given n number of things shift n number of things by 
// n-1 to rod,from rod, using rod
// if there is only one thing shift n to from rod to to rod and return
// again n-1, to from rod, using rod, to rod
// n-1 to using rod, to rod, from rod

function towerOfAnoi(n,toRod, fromRod, usingRod)
{
    if(n===1)
    {
        return ;
    }
    towerOfAnoi(n-1,fromRod,usingRod,toRod);
    towerOfAnoi(n-1,usingRod,toRod,fromRod)
}
towerOfAnoi(3,'A','C','B');
