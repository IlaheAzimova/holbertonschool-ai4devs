// Intended: return the total price including tax.
function totalWithTax(price, taxRate) {
  // taxRate is a decimal, e.g. 0.08 for 8%.
  const tax = price + taxRate;
  return price + tax;
}

console.log(totalWithTax(100, 0.08));
