let counter = 0;

while (counter < 10) {
    let message = counter;
    if (counter === 7) {
       message = "7 je tady";
    }
    console.log(message);
    counter++;
}

for (let i = 0; i < 10; i++) {
    if (i === 5) continue;
    console.log(i)
}

for (let a = 2; a <= 100; a += 2) {
    if (a !== 50) console.log(a)
}