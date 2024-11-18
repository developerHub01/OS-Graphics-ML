class Bresenham {
  constructor(cord1, cord2) {
    this.cord1 = cord1;
    this.cord2 = cord2;
    this.output = [this.cord1];
  }

  run() {
    console.log(
      `(${this.cord1[0]}, ${this.cord1[1]}), (${this.cord2[0]}, ${this.cord2[1]})`
    );
    
    const delX = this.cord2[0] - this.cord1[0],
      delY = this.cord2[1] - this.cord1[1];

    const slope = delY / delX;

    console.log(`delX = ${this.cord2[0]} - ${this.cord1[0]} = ${delX}`);
    console.log(`delY = ${this.cord2[1]} - ${this.cord1[1]} = ${delY}`);

    
    let currentP = slope < 1 ? 2 * delY - delX : 2 * delX - delY;
    let currentX = this.cord1[0],
    currentY = this.cord1[1];

    console.log(`slope == ${slope}`);
    
    
    if (slope < 1) console.log(`p = 2 * ${delY} - ${delX} = `, currentP);
    else console.log(`p = 2 * ${delX} - ${delY} = `, currentP);

    while (
      (delX >= delY && currentX < this.cord2[0]) ||
      (delX < delY && currentY < this.cord2[1])
    ) {
      let operatorStr = "";

      if (slope < 1 && currentP < 0) {
        operatorStr = `${currentP} + 2 * ${delY}`;
        currentP += 2 * delY;
        currentX++;
      } else if (slope < 1 && currentP >= 0) {
        operatorStr = `${currentP} + 2 * ${delY} - 2 * ${delX}`;
        currentP += 2 * delY - 2 * delX;
        currentX++;
        currentY++;
      } else if (slope >= 1 && currentP < 0) {
        operatorStr = `${currentP} + 2 * ${delX}`;
        currentP += 2 * delX;
        currentY++;
      } else if (slope >= 1 && currentP >= 0) {
        operatorStr = `${currentP} + 2 * ${delX} - 2 * ${delY}`;
        currentX++;
        currentY++;
        currentP += 2 * delX - 2 * delY;
      }

      console.log(
        `xi = ${currentX}, yi = ${currentY}, ${operatorStr} = ${currentP}`
      );

      this.output.push([currentX, currentY]);
    }

    return this.output;
  }
}

console.log(new Bresenham([2, 3], [8, 6]).run());
console.log(new Bresenham([2, 5], [5, 12]).run());
console.log(new Bresenham([3, 4], [7, 10]).run());
console.log(new Bresenham([2, 3], [8, 7]).run());
