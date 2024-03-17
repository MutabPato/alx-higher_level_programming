#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!Number.isInteger(w) || !Number.isInteger(h) || w <= 0 || h <= 0) {
      return ({});
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let i = 0; let j = 0; let row = '';

    for (i = 0; i < this.width; i++) {
      row += 'X';
    }

    for (j = 0; j < this.height; j++) {
      console.log(row);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
