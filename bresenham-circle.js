class BresenhamCircleDrawing {
  constructor(redius, centerCord = [0, 0]) {
    this.redius = redius;
    this.centerCordinate = centerCord;

    this.circle = {
      "1st": [],
      "2nd": [],
      "3rd": [],
      "4th": [],
    };
  }

  run() {
    let currentX = this.centerCordinate[0],
      currentY = this.redius;

    // let currentP = 1 - this.redius;
    let currentP = 3 - 2 * this.redius;

    let firstOctant = [];
    let secondOctant = [];

    while (currentX <= currentY) {
      firstOctant.push([currentX, currentY]);
      secondOctant.push([currentY, currentX]);

      if (currentP < 0) {
        // currentP += 2 * currentX + 3;
        currentP += 4 * currentX + 6;
        currentX++;
      } else {
        // currentP += 2 * (currentX - currentY) + 5;
        currentP += 4 * (currentX - currentY) + 10;
        currentX++;
        currentY--;
      }
    }

    secondOctant.pop();

    secondOctant = secondOctant.reverse();

    /* get first quadrant */
    this.circle["1st"] = [...firstOctant, ...secondOctant];

    /* get second quadrant */
    this.circle["2nd"] = this.circle["1st"].map(([x, y]) => [-1 * x, y]);

    /* get third quadrant */
    this.circle["3rd"] = this.circle["2nd"].map(([x, y]) => [x, -1 * y]);

    /* get fourth quadrant */
    this.circle["4th"] = this.circle["1st"].map(([x, y]) => [x, -1 * y]);


    this.circle["1st"] = this.circle["1st"].filter(([x, y]) => {
      return y !== 0;
    });

    this.circle["2nd"] = this.circle["2nd"].filter(([x, y]) => {
      return x !== 0;
    });

    this.circle["3rd"] = this.circle["3rd"].filter(([x, y]) => {
      return y !== 0;
    });

    this.circle["4th"] = this.circle["4th"].filter(([x, y]) => {
      return x !== 0;
    });

    return this.circle;
  }
}

console.log(new BresenhamCircleDrawing(7, [0, 0]).run());
