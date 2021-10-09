function solve(arr, order) {
    mapOrder = {
        'asc': (a,b) => {return a-b},
        'desc': (a,b) => {return b-a}
    }
    return arr.sort(mapOrder[order])
}

console.log(solve([2, 4, 1, 6], 'desc'));