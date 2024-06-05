function eraseOverlapIntervals(intervals) {
  if (intervals.length <= 1) {
    return 0; // No overlap to remove if there's only one or zero intervals
  }

  // Sort intervals by their end times
  intervals.sort((a, b) => a[1] - b[1]);

  let count = 0;
  let end = intervals[0][1];

  // Iterate through the sorted intervals
  for (let i = 1; i < intervals.length; i++) {
    const [start, currentEnd] = intervals[i];

    if (start < end) {
      // Overlapping intervals found, remove the one with the larger end time
      count++;
    } else {
      // Non-overlapping interval found, update the end time
      end = currentEnd;
    }
  }

  return count;
}

// Example usage:
const intervals1 = [[1,2],[2,3],[3,4],[1,3]];
console.log(eraseOverlapIntervals(intervals1)); // Output: 1

const intervals2 = [[1,2],[1,2],[1,2]];
console.log(eraseOverlapIntervals(intervals2)); // Output: 2

const intervals3 = [[1,2],[2,3]];
console.log(eraseOverlapIntervals(intervals3)); // Output: 0
