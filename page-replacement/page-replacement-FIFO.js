class PageReplacementFIFO {
  constructor(referenceList = [], frameSize = 1) {
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
    let currentFrameToInsertRef = 0;
    this.referenceList.forEach((reference) => {
      if (this.currentFrame.includes(reference)) {
        this.resultList.push({
          reference,
          type: "hit",
        });
        this.resultCount.hit++;
      } else {
        currentFrameToInsertRef = currentFrameToInsertRef % this.frameSize;

        this.currentFrame[currentFrameToInsertRef] = reference;

        this.resultList.push({
          reference,
          type: "miss",
        });
        this.resultCount.miss++;
        currentFrameToInsertRef++;
      }
    });

    return {
      resultList: this.resultList,
      resultCount: this.resultCount,
      ratio: {
        hitRatio: this.hitRatio(),
        missRatio: this.missRatio(),
      },
    };
  }

  hitRatio() {
    return this.ratio(this.resultCount.hit, this.referenceList.length);
  }
  missRatio() {
    return this.ratio(this.resultCount.miss, this.referenceList.length);
  }

  ratio(first, second) {
    return (first / second) * 100;
  }
}

const pageReplacementFIFO1 = new PageReplacementFIFO(
  [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 1, 2, 0],
  3
);

console.log(pageReplacementFIFO1.run());
