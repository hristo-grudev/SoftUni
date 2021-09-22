function solve(arr) {
    arr = arr.sort((a,b) => {
        return a-b;
    })
    let result = [];
    while (arr.length) {
        result.push(arr.shift());
        result.push(arr.pop());
    }

    
    return result.filter(num => num != undefined);
}
console.log('asdasdas');
console.log(solve([5, 6, 9, 1, -3, 56, 23, -1]));