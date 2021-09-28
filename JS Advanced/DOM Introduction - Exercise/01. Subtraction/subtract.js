function subtract() {
    const result = document.getElementById('result');
    const num1 = Number(document.getElementById('firstNumber').value);
    const num2 = Number(document.getElementById('secondNumber').value);

    result.innerHTML = (num1-num2).toString();
}