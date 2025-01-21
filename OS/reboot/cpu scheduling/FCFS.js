class FCFS {
  constructor(numberOfProcess, arrivalTime, burstTime) {
    this.numberOfProcess = numberOfProcess;
    this.AT = arrivalTime;
    this.BT = burstTime;
    this.CT = [];
    this.TAT = [];
    this.WT = [];
    this.RT = [];
    this.ganttChart = [];
    this.visited = Array(this.numberOfProcess).fill(false);
    this.currentTime = 0;
  }

  run() {
    while (true) {
      const currentProcess = this.findProcessArrivedCurrent();

      if (currentProcess === -1) {
        this.currentTime++;
        continue;
      }

      this.visited[currentProcess] = true;

      const currentBurstTime = this.BT[currentProcess];

      this.ganttChart.push({
        process: currentProcess,
        start: this.currentTime,
        end: this.currentTime + currentBurstTime,
      });

      this.CT[currentProcess] = this.currentTime + currentBurstTime;
      this.TAT[currentProcess] =
        this.CT[currentProcess] - this.AT[currentProcess];
      this.WT[currentProcess] =
        this.TAT[currentProcess] - this.BT[currentProcess];
      this.RT[currentProcess] = this.currentTime - this.AT[currentProcess];

      this.currentTime += currentBurstTime;

      if (this.ganttChart.length >= this.AT.length) break;
    }
    console.log(this.ganttChart);
    console.log(this.CT);
    console.log(this.TAT);
    console.log(this.WT);
    console.log(this.RT);
  }

  findProcessArrivedCurrent() {
    return this.AT.findIndex(
      (item, index) => item <= this.currentTime && !this.visited[index]
    );
  }
}

const fcfs = new FCFS(4, [0, 1, 5, 6], [2, 2, 3, 4]);
fcfs.run();
