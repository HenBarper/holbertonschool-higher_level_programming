#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let xCounter;
    let yCounter;
    let output = '';
    for (xCounter = 0; xCounter < this.width; xCounter++) {
      output += 'X';
    }
    for (yCounter = 0; yCounter < this.height; yCounter++) {
      console.log(output);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
