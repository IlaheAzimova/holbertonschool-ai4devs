function totalWithTax(price, taxRate) {
  const tax = price * taxRate;
  return price + tax;
}

if (totalWithTax(100, 0.08) !== 108) {
  throw new Error("Expected 108");
}

if (totalWithTax(50, 0.1) !== 55) {
  throw new Error("Expected 55");
}

console.log("bug4_fixed.js: all tests passed");
