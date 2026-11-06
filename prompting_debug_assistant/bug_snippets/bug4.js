// Intended: return the total price including tax.
function totalWithTax(price, taxRate) {
  // taxRate is a decimal, e.g. 0.08 for 8%.
  // BUG: tax should be a proportion of price, not price + taxRate.
  const tax = price + taxRate;
  return price + tax;
}

const itemPrice = 100;
const rate = 0.08;
const total = totalWithTax(itemPrice, rate);
console.log("Price:", itemPrice);
console.log("Tax rate:", rate);
console.log("Total with tax:", total);
