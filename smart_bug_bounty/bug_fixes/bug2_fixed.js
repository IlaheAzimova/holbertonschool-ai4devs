
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

function test(description, actual, expected) {
    if (actual !== expected) {
        console.error("FAIL:", description, "Expected:", expected, "Actual:", actual);
        process.exitCode = 1;
    } else {
        console.log("PASS:", description);
    }
}

test("Average of three numbers", calculateAverage([10, 20, 30]), 20);
test("Average of two numbers", calculateAverage([5, 15]), 10);
test("Average of empty array", calculateAverage([]), 0);
