/* DDA (Digital Differential Algorithm) */

class DDA {
  constructor(cord1, cord2) {
    this.cord1 = cord1;
    this.cord2 = cord2;
  }

  run() {
    let [startX, startY] = this.cord1;
    let [endX, endY] = this.cord2;

    const delX = endX - startX;
    const delY = endY - startY;

    const slope = delY / delX;

    let step = slope <= 1 ? delX : delY;

    const xInc = delX / Math.abs(step);
    const yInc = delY / Math.abs(step);

    const output = [[startX, startY]];

    while (true) {
      if (startX === endX || startY === endY) break;

      startX += xInc;
      startY += yInc;

      output.push([startX, startY])
    }

    return output;
  }
}

const dda1 = new DDA([5, 4], [12, 7]).run()
const dda2 = new DDA([5, 7], [10, 15]).run()
const dda3 = new DDA([12, 9], [17, 14]).run()
const dda4 = new DDA([17, 14], [12, 9]).run()

console.log(dda1);
console.log(dda2);
console.log(dda3);
console.log(dda4);
