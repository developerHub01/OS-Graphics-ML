class MidPointEllipse {
  constructor(centerX, centerY, a = 0, b = 0) {
    this.centerX = centerX;
    this.centerY = centerY;
    this.a = a;
    this.b = b;

    this.ellipse = {
      "1st": [],
      "2nd": [],
      "3rd": [],
      "4th": [],
    };
  }

  draw() {
    let x = 0;
    let y = this.b;

    let dx = 2 * x * this.b ** 2;
    let dy = 2 * y * this.a ** 2;

    console.log(dx, dy);

    let p = this.b ** 2 - this.a ** 2 * this.b + this.a ** 2 / 4;

    while (dx < dy) {
      this.ellipse["1st"].push([x, y]);

      if (p < 0) {
        x++;
        dx += 2 * this.b ** 2;
        p += dx + this.b ** 2;
      } else {
        x++;
        y--;
        dx += 2 * this.b ** 2;
        dy -= 2 * this.a ** 2;
        p += dx - dy + this.b ** 2;
      }
    }

    let q =
      this.b ** 2 * (x + 1 / 2) ** 2 +
      this.a ** 2 * (y - 1) ** 2 -
      this.a ** 2 * this.b ** 2;

    while (y >= 0) {
      this.ellipse["1st"].push([x, y]);

      if (q > 0) {
        y--;
        dy += -2 * this.a ** 2;
        q += this.a ** 2 - dy;
      } else {
        y--;
        x++;
        dx += 2 * this.b ** 2;
        dy -= 2 * this.a ** 2;
        q += dx - dy + this.a ** 2;
      }
    }

    this.ellipse["1st"].forEach(([x, y]) => {
      this.ellipse["2nd"].push([-1 * x, y]);
      this.ellipse["3rd"].push([-1 * x, -1 * y]);
      this.ellipse["4th"].push([x, -1 * y]);
    });

    return this.ellipse;
  }
}

const midPointEllipse1 = new MidPointEllipse(0, 0, 10, 15);

console.log(midPointEllipse1.draw());
