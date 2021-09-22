function solve(arr) {
    const result = arr.sort((a,b) => a.localeCompare(b));
    let orderNumer = 1;
    arr.forEach(el => {
        console.log(`${orderNumer}.${el}`);
        orderNumer++;
    });
}

