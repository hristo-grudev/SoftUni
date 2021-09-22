function solve(text){
    let formatedWords = [];
    let words = text.split(/\W+/g);
    let output = '';
    for (const word of words){
        output += word.toUpperCase() + ', ';
    }
    output = output.substr(0, output.length - 2);
    return output;
}