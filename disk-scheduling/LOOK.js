class LOOK {
  constructor(totalTrack, startTrack, queue) {
    this.startTrack = startTrack;
    this.totalTrack = totalTrack;
    this.queue = queue;
    this.currentTrack = startTrack;
  }

  count() {
    const rightWayDistance = Math.abs(
      this.startTrack - Math.max(...this.queue)
    );

    const leftWayDistance = Math.abs(
      Math.max(...this.queue) - Math.min(...this.queue)
    );

    console.log({ leftWayDistance, rightWayDistance });

    return leftWayDistance + rightWayDistance;
  }
}

// const look = new LOOK(200, 50, [82, 170, 43, 140, 24, 16, 190]);
const look = new LOOK(200, 50, [88, 150, 44, 173, 30, 15, 195]);
console.log(look.count());
