/*let inputQuanti = document.getElementById('quantity');

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
*/
const decrementButton = document.querySelector('#decrement');
const incrementButton = document.querySelector('#increment');
const countInput = document.querySelector('#quantity');

// adiciona o comportamento de decremento ao botão de decremento
number = 1;

function less() {
  number--;
  setValue(number);
}

function more() {
  number++;
  setValue(number);
}

function setValue(value) {
  document.getElementById('quantity').value = value;
}

setValue(number);