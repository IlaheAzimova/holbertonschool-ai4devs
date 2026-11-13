
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

function main() {
    console.log(calculateAverage([10, 20, 30]));
    console.log(calculateAverage([]));
}

main();
