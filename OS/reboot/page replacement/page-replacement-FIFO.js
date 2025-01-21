class FIFOPage {
  constructor(referenceList = [], frameSize = 3) {
    this.referenceList = referenceList;
    this.currentFrame = [];
    this.resultList = [];
    this.frameSize = frameSize;
    this.resultCount = {
      miss: 0,
      hit: 0,
    };
  }

  run() {
    let currentFrameInsert = 0;

    this.referenceList.forEach((reference) => {
      if (this.currentFrame.includes(reference)) {
        this.resultList.push({
          reference,
          type: "hit",
        });
        this.resultCount.hit++;
      } else {
        const currentReferenceIndexToInsert =
          currentFrameInsert % this.frameSize;

        this.currentFrame[currentReferenceIndexToInsert] = reference;

        this.resultList.push({
          reference,
          type: "miss",
        });
        this.resultCount.miss++;
        currentFrameInsert++;
      }
    });

    console.log(this.resultCount);
  }
}

const fifoPage = new FIFOPage([2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2]);
fifoPage.run();
