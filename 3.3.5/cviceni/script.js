let number = 10;
let message;

if (number > 0) {
    message = "Kladné číslo";
} else {
    message = "Není kladné";
}

console.log(message)

// řešení pomocí ternárního operátoru

let number2 = 10;
let message2 = (number2 > 0) ? "KLadné číslo" : "Není kladné";

console.log(message2)

let age =20;
if (age >= 18) {
    console.log("Můžeš řídit")
} else {
    console.log ("Jsi moc mladý/á na řízení")
}

age = 17;
console.log(age >= 18 ? "Můžeš řídít" : "Nemůžeš")

let podminka = !false;

podminka = true && false;

podminka = false || true;

console.log(podminka);
