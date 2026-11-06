// Intended: print each fruit with its zero-based index.
const fruits = ["apple", "banana", "orange"];

function printFruits(items) {
  // BUG: <= allows the loop to access one index past the end.
  for (let i = 0; i <= items.length; i++) {
    console.log(i, items[i].toUpperCase());
  }
}

printFruits(fruits);
console.log("Finished printing fruits.");
