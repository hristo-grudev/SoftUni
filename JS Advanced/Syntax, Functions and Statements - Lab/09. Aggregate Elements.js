function solve(array){
    let sum1 = 0;
    let sum2 = 0;
    let result = '';
    for (let i = 0; i < array.length; i++) {
        sum1 += array[i];
        sum2 += 1/array[i];
        result = result.concat(array[i]);
    }

    console.log(sum1)
    console.log(sum2)
    console.log(result)

}