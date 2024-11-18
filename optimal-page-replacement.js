class OptimalPageReplacement {
  constructor(referenceList = [], frameSize = 1) {
    this.referenceList = referenceList;
    this.frameSize = frameSize;
    this.currentFrame = [];
    this.resultList = [];
    this.resultCount = {
      hit: 0,
      fault: 0,
    };
  }

  run() {
    let currentFrameToInsertRef = 0;
    let isFrameFull = false;
    this.referenceList.forEach((reference, index) => {
      if (this.currentFrame.includes(reference)) {
        this.resultList.push({
          reference,
          type: "hit",
        });
        this.resultCount.hit++;
      } else {
        if (currentFrameToInsertRef >= this.frameSize) {
          isFrameFull = true;
          currentFrameToInsertRef = this.findOptimalReferenceIndex(index);
        }

        if (isFrameFull)
          currentFrameToInsertRef = this.findOptimalReferenceIndex(index);

        this.currentFrame[currentFrameToInsertRef] = reference;

        this.resultList.push({
          reference,
          type: "fault",
        });
        this.resultCount.fault++;

        if (!isFrameFull) currentFrameToInsertRef++;
      }
    });

    return {
      resultList: this.resultList,
      resultCount: this.resultCount,
      ratio: {
        hitRatio: this.hitRatio(),
        faultRatio: this.faultRatio(),
      },
    };
  }

  findOptimalReferenceIndex(pivot) {
    /* getting existing references count */
    const existingFrameReferences = {};
    this.currentFrame.forEach(
      (reference, index) =>
        (existingFrameReferences[reference] = {
          index,
          count: 0,
        })
    );

    let selectedReference = this.referenceList[pivot];

    for (let index = pivot + 1; index < this.referenceList.length; index++) {
      const reference = this.referenceList[index];

      if (!this.currentFrame.includes(reference)) continue;

      selectedReference = reference;

      existingFrameReferences[reference].count++;

      if (
        Object.values(existingFrameReferences).reduce(
          (total, curr) => total + Boolean(curr.count),
          0
        ) === this.currentFrame.length
      )
        break;
    }

    for (const reference in existingFrameReferences) {
      const { index, count } = existingFrameReferences[reference];
      if (!count) return index;
    }

    return this.currentFrame.findIndex((item) => item === selectedReference);
  }

  hitRatio() {
    return this.ratio(this.resultCount.hit, this.referenceList.length);
  }
  faultRatio() {
    return this.ratio(this.resultCount.fault, this.referenceList.length);
  }

  ratio(first, second) {
    return (first / second) * 100;
  }
}

const optimalPageReplacement = new OptimalPageReplacement(
  [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1],
  4
);

console.log(optimalPageReplacement.run());
