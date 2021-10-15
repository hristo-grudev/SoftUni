function validate() {
    const inputField = document.getElementById("email");
    const validPattern = /(^[a-z]+@[a-z]+\.[a-z]+$)/;

    inputField.addEventListener("change", ()=> {
        if (!validPattern.test(inputField.value)) {
            inputField.classList.add("error");
        } else {
            inputField.classList.remove("error");
        }
    })
}
