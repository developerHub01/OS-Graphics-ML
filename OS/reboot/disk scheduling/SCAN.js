class SCAN {
  constructor(queue, start, end, head) {
    this.queue = queue;
    this.head = head;
    this.start = start;
    this.end = end;
  }

  run() {
    const minPoint = Math.min(...this.queue);

    const totalDistance = this.end - this.head + (this.end - minPoint);

    console.log(totalDistance);

    return totalDistance;
  }
}

const scan = new SCAN([88, 150, 44, 173, 30, 15, 195], 0, 199, 50);
scan.run();
