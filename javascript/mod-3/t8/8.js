function calculate() {
    let num1 = document.getElementById("num1").value;
    let num2 = document.getElementById("num2").value;
    let operation = document.getElementById("operation").value;

    num1 = Number(num1);
    num2 = Number(num2);

    let result;

    if (operation === "add") {
        result = num1 + num2;
    } else if (operation === "sub") {
        result = num1 - num2;
    } else if (operation === "multi") {
        result = num1 * num2;
    } else if (operation === "div") {
        if (num2 === 0) {
            result = "Cannot divide by zero";
        } else {
            result = num1 / num2;
        }
    }

    document.getElementById("result").textContent = result;
}
