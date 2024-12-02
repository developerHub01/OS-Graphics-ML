/* SSTF: First Come First Serve */

class SSTF {
  constructor(totalTrack, startTrack, queue) {
    this.startTrack = startTrack;
    this.queue = queue;
    this.currentTrack = startTrack;
  }
  count() {
    const tempQueue = this.queue.map((request) => ({
      value: request,
      visited: false,
    }));

    let totalDistance = 0;
    let currentState = this.startTrack;

    while (true) {
      const nearestIndex = this.getNearestIndex(tempQueue, currentState);

      if (nearestIndex < 0) break;

      const nearestState = this.queue[nearestIndex];

      totalDistance += Math.abs(currentState - nearestState);

      currentState = nearestState;
      tempQueue[nearestIndex].visited = true;
    }

    return totalDistance;
  }

  getNearestIndex(queue, currentState) {
    let minDistance = Infinity;
    let nearestIndex = -1;

    queue.forEach(({ value, visited }, index) => {
      if (!visited && Math.abs(value - currentState) < minDistance) {
        minDistance = Math.abs(value - currentState);
        nearestIndex = index;
      }
    });

    return nearestIndex;
  }
}

const sstf = new SSTF(200, 50, [82, 170, 43, 140, 24, 16, 190]);
console.log(sstf.count());
