let switch_div = document.getElementById('switch_div');
let circle = document.getElementById('circle');

switch_div.addEventListener('click', () => {
    if (circle.classList.contains('left')) {
        circle.classList.remove('left');
        circle.classList.add('right');
        change_prices();
    } else {
        circle.classList.remove('right');
        circle.classList.add('left');
        change_prices()
    }
});

change_prices = () => {
    let basic = document.getElementById('basic');
    let professional = document.getElementById('professional');
    let master = document.getElementById('master');

    if (basic.innerHTML === '$19.99') {
        basic.innerHTML = '$199.99';
        professional.innerHTML = '$249.99';
        master.innerHTML = '$399.99';
    } else {
        basic.innerHTML = '$19.99';
        professional.innerHTML = '$24.99';
        master.innerHTML = '$39.99';
    }
}