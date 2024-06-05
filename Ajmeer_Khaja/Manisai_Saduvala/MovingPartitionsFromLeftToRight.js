function movingPartition(arr) {
    if (arr.length === 0) return []; // Return an empty array for an empty input
  
    const result = [];
    for (let i = 1; i < arr.length; i++) {
      const left = arr.slice(0, i);
      const right = arr.slice(i);
      result.push([left, right]);
    }
    return result;
  }

  const arr = [1,2,3,4,5];
  const res = movingPartition(arr);
  console.log(res);
