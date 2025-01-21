class Bankers {
  constructor() {
    this.resources = [];
    this.maxNeeds = [];
    this.allocatedResources = [];
    this.currentResource = [];
    this.availableResources = [];
    this.visited = [];
    this.safeSequence = [];
  }
  start(resource, maxNeeds, allocatedResources) {
    this.resources = resource;
    this.maxNeeds = maxNeeds;
    this.allocatedResources = allocatedResources;
  }
  run() {
    const totalAllocatedResources = [];
    this.allocatedResources.forEach((resources) => {
      resources.forEach((resource, index) => {
        totalAllocatedResources[index] =
          (totalAllocatedResources[index] ?? 0) + resource;
      });
    });

    this.availableResources = this.resources.map((resource, index) => {
      return resource - totalAllocatedResources[index];
    });

    this.currentResource = this.maxNeeds.map((resources, resourcesIndex) => {
      return resources.map((resource, index) => {
        return resource - this.allocatedResources[resourcesIndex][index];
      });
    });

    while (true) {
      const targetedIndex = this.currentResource.findIndex(
        (resources, rowIndex) => {
          if (this.visited[rowIndex]) return false;

          return resources.every((resource, index) => {
            return resource <= this.availableResources[index];
          });
        }
      );

      if (targetedIndex === -1) break;

      this.visited[targetedIndex] = true;

      this.safeSequence.push(targetedIndex);

      this.availableResources = this.availableResources.map(
        (resource, index) =>
          resource + this.allocatedResources[targetedIndex][index]
      );
    }
  }

  print() {
    console.log("Safe Sequence:", this.safeSequence);
  }
}

const bankers1 = new Bankers();
bankers1.start(
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
bankers1.run();
bankers1.print();
