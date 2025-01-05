class CLOOK {
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
    const rightWayDistance = Math.abs(
      this.startTrack - Math.max(...this.queue)
    );

    const leftWayDistance = Math.abs(
      this.findLastInLeft() - Math.min(...this.queue)
    );

    const backTrackDistance = Math.abs(
      Math.max(...this.queue) - Math.min(...this.queue)
    );

    return leftWayDistance + backTrackDistance + rightWayDistance;
  }
}

const clook = new CLOOK(200, 50, [82, 170, 43, 140, 24, 16, 190]);
console.log(clook.count());
