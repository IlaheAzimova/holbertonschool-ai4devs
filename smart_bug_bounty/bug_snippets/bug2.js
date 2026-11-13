
function calculateAverage(scores) {
    if (scores.length === 0) {
        return 0;
    }

    let total = 0;
    for (let i = 0; i <= scores.length; i++) {
        total += scores[i];
    }

    return total / scores.length;
}

const scores = [10, 20, 30];
console.log("Expected: 20");
console.log("Actual:", calculateAverage(scores));
console.log("Empty array:", calculateAverage([]));
