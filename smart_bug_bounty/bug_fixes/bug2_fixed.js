
function calculateAverage(scores) {
    if (scores.length === 0) {
        return 0;
    }

    let total = 0;
    for (let i = 0; i < scores.length; i++) {
        total += scores[i];
    }

    return total / scores.length;
}

console.assert(calculateAverage([10, 20, 30]) === 20);
console.assert(calculateAverage([5, 15]) === 10);
console.assert(calculateAverage([]) === 0);
console.log("bug2_fixed.js: Tests completed");
