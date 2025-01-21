class DiskSSTF {
  constructor(tasks, start, end, head) {
    this.tasks = tasks.map((task) => ({
      task,
      visited: false,
    }));
    this.start = start;
    this.end = end;
    this.head = head;
  }

  run() {
    let totalDistance = 0;

    let currentPoint = this.head;

    while (true) {
      const nearestIndex = this.getNearestIndex(currentPoint);

      if (nearestIndex < 0) break;

      const nearestPoint = this.tasks[nearestIndex].task;

      console.log({ nearestPoint });

      this.tasks[nearestIndex].visited = true;
      totalDistance += Math.abs(nearestPoint - currentPoint);

      currentPoint = nearestPoint;
    }

    console.log(totalDistance);
  }

  getNearestIndex(currentPoint) {
    let minDistance = Infinity;
    let nearestIndex = -1;

    this.tasks.forEach(({ task, visited }, index) => {
      if (!visited && Math.abs(task - currentPoint) < minDistance) {
        nearestIndex = index;
        minDistance = Math.abs(task - currentPoint);
      }
    });

    return nearestIndex;
  }
}

const disksstf = new DiskSSTF([88, 15, 44, 173, 30, 15, 195], 0, 199, 50);
console.log(disksstf.run());
