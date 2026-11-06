// Print each fruit in uppercase.
function printFruits(items) {
  for (let i = 0; i < items.length; i++) {
    console.log(i, items[i].toUpperCase());
  }
}

const fruits = ["apple", "banana", "orange"];
printFruits(fruits);

// Confirm that the example completed.
console.log("bug2_fixed.js: test completed");
