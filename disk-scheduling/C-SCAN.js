/* circular scan */

class CSCAN {
  constructor(totalTrack, startTrack, queue) {
    this.startTrack = startTrack;
    this.totalTrack = totalTrack;
    this.queue = queue;
    this.currentTrack = startTrack;
  }

  findLastInLeft() {
    let lastVlaue = -Infinity;

    for (let i = 0; i < this.queue.length; i++) {
      const currentTrack = this.queue[i];
      console.log({ currentTrack });

      if (currentTrack < this.startTrack && currentTrack > lastVlaue)
        lastVlaue = currentTrack;
    }
    console.log({ lastVlaue });

    return lastVlaue;
  }
  count() {
    const rightWayDistance = Math.abs(this.startTrack - (this.totalTrack - 1));

    const leftWayDistance = this.findLastInLeft();

    const backTrackDistance = this.totalTrack - 1;

    return leftWayDistance + backTrackDistance + rightWayDistance;
  }
}

const cscan = new CSCAN(200, 50, [82, 170, 43, 140, 24, 16, 190]);
console.log(cscan.count());
