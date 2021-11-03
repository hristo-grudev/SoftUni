function solution() {
    let button = document.querySelector(`span.button`);
    let butonName = document.getElementsByClassName(`button`)[0];
    let divHiden = document.getElementById(`extra`);
 
    button.addEventListener(`click`,()=>{
 
        if(butonName.textContent == `More`) {
            divHiden.style.display = `block`;
            butonName.textContent = `Less`;
        } else if(butonName.textContent == `Less`) {
            
                divHiden.style.display = `none`;
                butonName.textContent = `More`;
        }
       
    })
}