class SJF {
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
    const selectedProcess = this.AT.reduce((acc, current, index) => {
      if (current <= this.currentTime && !this.visited[index]) acc.push(index);

      return acc;
    }, []);

    let targetedProcess = selectedProcess[0];
    let targetProcessBurstTime = this.BT[targetedProcess];

    selectedProcess.forEach((process) => {
      const currentBurstTime = this.BT[process];

      if (currentBurstTime < targetProcessBurstTime) targetedProcess = process;
    });

    if (typeof targetedProcess === "number") return targetedProcess;
    else return -1;
  }
}

// const sjf = new SJF(4, [0, 1, 5, 6], [2, 2, 3, 4]);
const sjf = new SJF(4, [1, 2, 1, 4], [3, 4, 2, 4]);
sjf.run();
