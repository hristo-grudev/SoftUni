function addItem() {
    let item_text = document.getElementById('newItemText');
    let item_value = document.getElementById('newItemValue');
    let menu = document.getElementById('menu');

    let option = document.createElement('option');
    option.innerHTML = item_text.value;
    option.value = item_value.value;

    menu.appendChild(option);

    item_text.value = '';
    item_value.value = '';

}
