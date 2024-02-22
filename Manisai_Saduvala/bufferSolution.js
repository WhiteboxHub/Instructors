const createBuffer = (limit) => {
  const peopleQueue = [];

  const movePeople = (peopleCount) => {
    const moveBatch = (count) => {
      const currentBatch = Math.min(limit, count);
      const movedPeople = peopleQueue.splice(0, currentBatch);

      // Simulate moving people to another point
      console.log(Moved ${movedPeople.length} people to another point.);

      return count - currentBatch;
    };

    return peopleCount <= 0
      ? "Invalid number of people to move."
      : peopleQueue.length === 0
      ? Waiting for ${peopleCount} people to arrive in the queue.
      : moveBatch(peopleCount);
  };

  const addToQueue = (...people) => {
    peopleQueue.push(...people);
  };

  return { movePeople, addToQueue };
};

// Example Usage:
const buffer = createBuffer(3); // Limiting to move 3 people at a time

buffer.addToQueue('Person1', 'Person2', 'Person3', 'Person4', 'Person5');

console.log(buffer.movePeople(2)); // Should move 2 people
console.log(buffer.movePeople(5)); // Should wait for more people to arrive
console.log(buffer.movePeople(3)); // Should move the remaining 3 people
