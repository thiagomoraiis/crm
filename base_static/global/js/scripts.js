let inputQuanti = document.getElementById('quantity');

let country = 0;

function updateValue(){
    inputQuanti.textContent = country;
}

function incrementClick(){
    inputQuanti++;
}

function decrementClick(){
    inputQuanti++;
}

let buttonIncremente = document.getElementById('increment');
buttonIncremente.addEventListener('click', incrementClick);

let buttonDecremente = document.getElementById('decrement');
buttonDecremente.addEventListener('click', decrementClick);

