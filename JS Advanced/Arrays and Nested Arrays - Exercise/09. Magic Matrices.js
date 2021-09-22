function solve(matrix) {
    let rowSums = [];
    let colSums = [];
    for(let i = 0; i < matrix.length; i++) {
        let row= matrix[i]
        let sum = row.reduce((result,current) => (result+current), 0);
        rowSums.push(sum);
    }

    for (let x = 0; x < matrix.length; x++) {
        let row = matrix[x];
        let newRow = [];
        for(let y = 0; y < matrix.length; y++){
            let index = matrix.length - 1 - y;
            newRow.push(matrix[index][x])
        }
        let sum = newRow.reduce((result, current) => (result+current), 0);
        colSums.push(sum);
    }

    return rowSums.concat(colSums).every((el, index, arr) => el === arr[0]);

}
