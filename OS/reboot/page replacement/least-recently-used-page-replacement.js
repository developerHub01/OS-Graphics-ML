class LeastRecentlyUserdPageReplacement {
  constructor(referencesList = [], frameSize = 3) {
    this.referencesList = referencesList;
    this.frameSize = frameSize;
    this.currentFrame = [];
    this.resultList = [];
    this.resultCount = {
      hit: 0,
      miss: 0,
    };
  }

  run() {
    this.referencesList.map((reference, index) => {
      if (this.currentFrame.includes(reference)) {
        this.resultList.push({
          reference,
          type: "hit",
        });
        this.resultCount.hit++;
      } else {
        if (this.currentFrame.length >= this.frameSize) {
          const targetedIndex = this.getOptimalIndex(index);

          this.currentFrame[targetedIndex] = reference;
        } else {
          this.currentFrame.push(reference);
        }
        this.resultList.push({
          reference,
          type: "miss",
        });
        this.resultCount.miss++;
      }
    });

    console.log(this.resultList);
    console.log(this.resultCount);
  }

  getOptimalIndex(pivot) {
    const firstOccurIndex = {};

    for (let i = pivot - 1; i >= 0; i--) {
      const reference = this.referencesList[i];

      if (
        reference in firstOccurIndex ||
        !this.currentFrame.includes(reference)
      )
        continue;

      firstOccurIndex[reference] = i;
    }

    const referanceOutOfTheList = this.currentFrame.findIndex(
      (value) => firstOccurIndex[value] === undefined
    );

    if (referanceOutOfTheList !== -1)
      return this.getCurrentFrameIndexByValue(referanceOutOfTheList);

    const targetedValue = Number(
      Object.entries(firstOccurIndex).sort(
        ([key1, value1], [key2, value2]) => value1 - value2
      )[0][0]
    );

    return this.getCurrentFrameIndexByValue(targetedValue);
  }

  getCurrentFrameIndexByValue(value) {
    return this.currentFrame.findIndex((item) => item === value);
  }
}

const leastRecentlyUserdPageReplacement = new LeastRecentlyUserdPageReplacement(
  [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2]
);
leastRecentlyUserdPageReplacement.run();
