 /*spiral level order traversal of  a binary tree

 Unit test cases consider a binary tree let every node is termed as a root and a tree has n number of levels
 we have to return each level within a bucket (like a array) so, for odd levels reverse the bucket
        1    - 0 level
       / \   
      2   3  - 1
         / \
         6  7  -2

    */
   // so, the output for the tree will be
   //[[1],[3,2],[6,7]]

   var zigzag = function (root)
   {
     // an array to return buckets
    let result = [];
    // an expression that takes root and level of the tree as an parameters
    const levelOfTraversal = (root,level)=>{
        // Base condition checks wheter the tree has a node or not
        if(!root)
        {
            // if false simply return 
            return;
        }
        //main
        //if the tree has a level
        if(result[level])
        {
            // push the  root values to the resultant levels of the array
            result[level].push(root.value)
        }
        // if not push the root for that level
        else
        {
            result[level]=[root.value]
        }
        // calling left root of the current root by incrementing the level recursievly
        levelOfTraversal(root.left,level+1);
        // calling the right root of the current root by incrementing the level recursievly
        levelOfTraversal(root.right,level+1)
    }
    // Finnaly check the levels of tree if it is odd reverse the bucket if even just print that bucket
    return result.map((bucket,i)=>(i%2)?bucket.reverse:bucket)
   }
