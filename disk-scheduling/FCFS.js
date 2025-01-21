/* FCFS: First Come First Serve */

class FCFS {
  constructor(totalTrack, startTrack, queue) {
    this.startTrack = startTrack;
    this.queue = queue;
    this.currentTrack = startTrack;
  }
  count() {
    let totalDistance = 0;
    let previousState = this.currentTrack;
    this.queue.forEach((request) => {
      totalDistance += Math.abs(previousState - request);

      previousState = request;
    });

    return totalDistance;
  }

  shortCount() {
    return this.queue.reduce(
      (totalDistance, currentState, index, tempQueue) =>
        totalDistance +
        Math.abs(
          (index === 0 ? this.startTrack : tempQueue[index - 1]) - currentState
        ),
      0
    );
  }
}

// const fcfs = new FCFS(200, 50, [82, 170, 43, 140, 24, 16, 190]);

// console.log(fcfs.count());
// console.log(fcfs.shortCount());


const fcfs = new FCFS(200, 50, [88, 15, 44, 173, 30, 15, 195]);
console.log(fcfs.count());