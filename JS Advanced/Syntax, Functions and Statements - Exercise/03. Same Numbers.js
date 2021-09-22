function solve(num){
    let numString = String(num);
    let isSame = true
    let sum = numString.length > 0 ? Number(numString[0]) : 0;
    for (let i=0; i < numString.length - 1; i++){
        const element = Number(numString[i]);
        const nextElement = Number(numString[i + 1]);
        if (element !== nextElement){
            isSame = false
        }
        sum += nextElement;
    }
    console.log(isSame)
    console.log(sum)
}