function getFibonator() {
    let num1 = 0;
    let num2 = 1;
    let result = 0;
 
    return function fib() {
        result = num1 + num2
        num1 = num2;
        num2 = result
        return num1;
    }
}
let fib = getFibonator();

console.log(fib());
console.log(fib());
console.log(fib());
console.log(fib());