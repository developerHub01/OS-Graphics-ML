class Bankers {
  constructor() {
    this.resourceTypes = [];
    this.maxResources = [];
    this.allocatedResources = [];
    this.currentResourceNeed = [];
    this.availableResources = [];
    this.visited = {};
  }

  start(resourceTypes, maxResources, allocatedResources) {
    this.resourceTypes = resourceTypes;
    this.maxResources = maxResources;
    this.allocatedResources = allocatedResources;

    /* initial available resources */
    this.availableResources.push(
      this.substractTwoArray(
        this.resourceTypes,
        this.getAllocatedResourcesSum()
      )
    );

    /* current resources column */
    this.generateCurrentResource();

    this.run();
  }

  getAllocatedResourcesSum() {
    const sumList = [];

    this.allocatedResources.forEach((process) => {
      process.forEach((resources, index) => {
        sumList[index] = sumList[index] ?? 0;

        sumList[index] += resources;
      });
    });

    return sumList;
  }

  generateCurrentResource() {
    this.maxResources.forEach((process, processIndex) => {
      this.currentResourceNeed[processIndex] =
        this.currentResourceNeed[processIndex] ?? [];

      process.forEach((resource, resourceIndex) => {
        this.currentResourceNeed[processIndex][resourceIndex] =
          resource - this.allocatedResources[processIndex][resourceIndex];
      });
    });
  }

  getTargetedAvailableResources() {
    return this.availableResources[this.availableResources.length - 1];
  }

  isSelectable(currentResourceNeeded, targetResource) {
    for (const index in currentResourceNeeded)
      if (currentResourceNeeded[index] > targetResource[index]) return false;

    return true;
  }

  sumTwoArray(arr1, arr2) {
    return arr1.map((value, index) => value + arr2[index]);
  }
  substractTwoArray(arr1, arr2) {
    return arr1.map((value, index) => value - arr2[index]);
  }

  run() {
    while (true) {
      const targetedAvailableResources = this.getTargetedAvailableResources();

      const selectedProcessIndex = this.currentResourceNeed.findIndex(
        (process, index) => {
          if (this.visited[index]) return false;

          return this.isSelectable(process, targetedAvailableResources);
        }
      );

      if (selectedProcessIndex === -1) break;

      const currentAllocatedResources =
        this.allocatedResources[selectedProcessIndex];

      this.availableResources.push(
        this.sumTwoArray(targetedAvailableResources, currentAllocatedResources)
      );
      this.visited[selectedProcessIndex] = true;
    }
  }

  printTable() {
    console.log("Current resources need: ");
    console.log("============================");
    console.log(this.currentResourceNeed);
    console.log("available resources: ");
    console.log("============================");
    console.log(this.availableResources);
  }
}

const bankers = new Bankers();
bankers.start(
  [10, 5, 7],
  [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3],
  ],
  [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2],
  ]
);
bankers.printTable();
