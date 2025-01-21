class OptimalPageReplacement {
  constructor(referenceList = [], frameSize = 3) {
    this.referenceList = referenceList;
    this.frameSize = frameSize;
    this.currentFrame = [];
    this.resultList = [];
    this.resultCount = {
      hit: 0,
      miss: 0,
    };
  }

  run() {
    this.referenceList.forEach((reference, index) => {
      if (this.currentFrame.includes(reference)) {
        this.resultList.push({
          reference,
          type: "hit",
        });
        this.resultCount.hit++;
      } else {
        if (this.currentFrame.length >= this.frameSize) {
          const optimalIndex = this.getOptimalIndex(index);

          this.currentFrame[optimalIndex] = reference;
        } else {
          this.currentFrame.push(reference);
        }
        this.resultCount.miss++;
        this.resultList.push({
          reference,
          type: "miss",
        });
      }
      console.log(this.currentFrame);
      
    });
    console.log(this.resultCount);
  }

  getOptimalIndex(startIndex) {
    const firstOccurIndex = {};

    for (let i = startIndex + 1; i < this.referenceList.length; i++) {
      const reference = this.referenceList[i];

      if (
        reference in firstOccurIndex ||
        !this.currentFrame.includes(reference)
      )
        continue;

      firstOccurIndex[reference] = i;
    }

    console.log({ firstOccurIndex });

    for (let i = 0; i < this.currentFrame.length; i++) {
      const reference = this.currentFrame[i];
      const firstOccuredIndex = firstOccurIndex[reference];

      if (firstOccuredIndex === undefined) {
        return this.getCurrentFrameIndexByValue(reference);
      }
    }

    const sortedFirstOccurIndex = Object.entries(firstOccurIndex).sort(
      ([key1, value1], [key2, value2]) => value2 - value1
    );

    const selectedValue = Number(sortedFirstOccurIndex[0][0]);

    return this.getCurrentFrameIndexByValue(selectedValue);
  }

  getCurrentFrameIndexByValue(value) {
    return this.currentFrame.findIndex((item) => item === value);
  }
}

const optimalPageReplacement1 = new OptimalPageReplacement([
  2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2,
]);
optimalPageReplacement1.run();
