function printFruits(items) {
  for (let i = 0; i < items.length; i++) {
    console.log(i, items[i].toUpperCase());
  }
}

const fruits = ["apple", "banana", "orange"];
printFruits(fruits);
console.log("bug2_fixed.js: test completed");
