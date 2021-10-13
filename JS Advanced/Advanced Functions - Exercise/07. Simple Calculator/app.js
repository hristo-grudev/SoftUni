function calculator() {
    let firstInput;
    let scondInput;
    let result;
    
    function init(selector1, selector2, selector3) {
        firstInput = document.querySelector(selector1);
        scondInput = document.querySelector(selector2);
        result = document.querySelector(selector3);
    }

    function add() {
        result.value = Number(firstInput.value) + Number(scondInput.value);
    }

    function subtract() {
        result.value = Number(firstInput.value) - Number(scondInput.value);
    }

    return {
        init,
        add,
        subtract
    }
}




