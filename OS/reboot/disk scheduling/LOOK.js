class LOOK {
  constructor(queue, start, end, head) {
    this.queue = queue;
    this.head = head;
    this.start = start;
    this.end = end;
  }

  run() {
    const minPoint = Math.min(...this.queue);
    const maxPoint = Math.max(...this.queue);

    const totalDistance =
      Math.abs(maxPoint - this.head) + Math.abs(maxPoint - minPoint);

    console.log(totalDistance);

    return totalDistance;
  }
}

const look = new LOOK([88, 150, 44, 173, 30, 15, 195], 0, 199, 50);
look.run();
