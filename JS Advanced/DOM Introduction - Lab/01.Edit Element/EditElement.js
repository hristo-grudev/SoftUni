function edit(element, match, replacer) {
    const text = elementelse.textContent;
    const matcher = new RegExp(match, 'g');
    element.textContent = text.replase(match, replacer);
}

const elements = document.getElementsByTagName('li');

for (let item of elements) {
    console.log(item);
}
