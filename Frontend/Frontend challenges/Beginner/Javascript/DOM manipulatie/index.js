const button1 = document.getElementById("button1");
const button2 = document.getElementById("button2");
const button3 = document.getElementById("button3");
const button4 = document.getElementById("button4");

const square = document.getElementById("square");




button1.addEventListener("click", () => {
    square.classList.toggle("blue");
});

button2.addEventListener("click", () => {
    square.classList.toggle("bigger");
})

button3.addEventListener("click", () => {
    square.classList.toggle("rotate");
})

button4.addEventListener("click", () => {
    square.classList.toggle("blue");
    square.classList.toggle("bigger");
    square.classList.toggle("rotate");

    let test = 1+1;
    console.log(test)
})



let input_text = document.getElementById("input_text");
let input_button = document.getElementById("input_button");
let text = document.getElementById("text");

input_button.addEventListener("click", () => {
    text.innerHTML = input_text.value;
});


let number = 20;
let minus = document.getElementById("minus");
let plus = document.getElementById("plus");
let final_number = document.getElementById("final_number");

minus.addEventListener("click", () => {
    number--;
    final_number.innerText = number;
    final_number.style.fontSize = `${number}px`;
});

plus.addEventListener("click", () => {
    number++;
    final_number.innerText = number;
    final_number.style.fontSize = `${number}px`;
});