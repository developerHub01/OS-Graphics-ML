class SCAN {
  constructor(totalTrack, startTrack, queue) {
    this.startTrack = startTrack;
    this.totalTrack = totalTrack;
    this.queue = queue;
    this.currentTrack = startTrack;
  }
  count() {
    const minRequest = Math.min(...this.queue);

    const rightWayDistance = Math.abs(this.startTrack - (this.totalTrack - 1));

    const leftWayDistance = Math.abs(this.totalTrack - 1 - minRequest);

    return leftWayDistance + rightWayDistance;
  }
}

const scan = new SCAN(200, 50, [82, 170, 43, 140, 24, 16, 190]);
console.log(scan.count());
