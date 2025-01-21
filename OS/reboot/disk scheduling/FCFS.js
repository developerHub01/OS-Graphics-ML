class DiskFCFS {
  constructor(tasks, start, end, head) {
    this.tasks = tasks;
    this.start = start;
    this.end = end;
    this.head = head;
  }

  run() {
    let totalDistance = 0;

    let startPoint = this.head;

    this.tasks.forEach((task) => {
      totalDistance += Math.abs(task - startPoint);
      startPoint = task;
    });

    return totalDistance;
  }
}

const diskfcfs1 = new DiskFCFS([88, 15, 44, 173, 30, 15, 195], 0, 199, 50);
console.log(diskfcfs1.run());
