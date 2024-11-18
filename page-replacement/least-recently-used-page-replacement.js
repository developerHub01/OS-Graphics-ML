/* least recently used page replacement */
class LRUPageReplacement {
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
    let isFrameFull = false;
    this.referenceList.forEach((reference, index) => {
      if (this.currentFrame.includes(reference)) {
        this.resultList.push({
          reference,
          type: "hit",
        });
        this.resultCount.hit++;
      } else {
        if (currentFrameToInsertRef >= this.frameSize) isFrameFull = true;

        if (isFrameFull)
          currentFrameToInsertRef =
            this.findLeastRecentlyUsedReferenceIndex(index);

        this.currentFrame[currentFrameToInsertRef] = reference;

        this.resultList.push({
          reference,
          type: "miss",
        });
        this.resultCount.miss++;

        if (!isFrameFull) currentFrameToInsertRef++;
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

  findLeastRecentlyUsedReferenceIndex(pivot) {
    /* getting existing references count */
    const existingFrameReferences = {};

    this.currentFrame.forEach(
      (reference, index) =>
        (existingFrameReferences[reference] = {
          index,
          count: 0,
        })
    );

    let numberOfUniqueTraversed = 0;

    let selectedReference = this.referenceList[pivot];

    for (let index = pivot - 1; index >= 0; index--) {
      const currentReference = this.referenceList[index];

      if (!this.currentFrame.includes(currentReference)) continue;

      selectedReference = currentReference;

      if (!existingFrameReferences[currentReference]?.count)
        numberOfUniqueTraversed++;

      existingFrameReferences[currentReference].count++;

      if (numberOfUniqueTraversed === this.currentFrame.length) break;
    }

    for (const currentReference in existingFrameReferences) {
      const { count, index } = existingFrameReferences[currentReference];
      if (!count) return index;
    }

    return this.currentFrame.indexOf(selectedReference);
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

const pageReplacement = new LRUPageReplacement(
  [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1],
  4
);

console.log(pageReplacement.run());
