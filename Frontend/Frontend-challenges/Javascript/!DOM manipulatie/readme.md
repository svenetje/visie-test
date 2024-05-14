# JavaScript Beginners Gids

## Inleiding

JavaScript is een programmeertaal die vaak wordt gebruikt voor het toevoegen van interactieve functies aan websites. Deze gids zal je door een eenvoudig voorbeeld leiden om je kennis te laten maken met basis JavaScript-functionaliteiten.

## Stap 1: HTML-structuur

Maak een HTML-bestand genaamd `index.html` en voeg de volgende structuur toe:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DOM</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="left">      
        <div class="square-div">
            <div class="square bigger" id="square"></div>
        </div>
        <div class="left-buttons">
            <button type="button" id="button1">Verander kleur</button>
            <button type="button" id="button2">Verander grootte</button>
            <button type="button" id="button3">Laat draaien</button>
            <button type="button" id="button4">Alles veranderen</button>
        </div>
    </div>

    <div class="right">
        <div class="input_change">
            <input type="text" name="Text" id="input_text">
            <button type="button" id="input_button">Submit</button>
            <p id="text"></p>
        </div>
        <div class="counter">
            <button type="button" id="minus">-</button>
            <p id="final_number">20</p>
            <button type="button" id="plus">+</button>
        </div>
    </div>

    <!-- Link de javascript -->
    <script src="index.js"></script>
</body>
</html>
```

## Stap 2: CSS-stijlen

Maak een CSS-bestand genaamd `style.css` en voeg de volgende stijlen toe:

```css
body
{
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 100vh;
}

.left,
.right
{
    width: 45vw;
    display: flex;
    align-items: center;
    justify-content: center;
}

.square-div
{
    display: flex;
    align-items: center;
    justify-content: center;
    width: 30vw;
    margin-right: 100px;
}

.square 
{
    width: 300px;
    height: 300px;
    background-color: red;
    transition: 1s;
}

.left-buttons
{
    display: flex;
    flex-direction: column;
    gap: 30px;
}

.right
{
    display: flex;
    flex-direction: column;
    gap: 30px;
    align-items: flex-start;
}

button 
{
    width: 200px;
    height: 50px;
    cursor: pointer;
}

.right
{
    display: flex;
    align-items: center;
    justify-content: center;
}

.input_change
{
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.input_change p
{
    height: 30px;
}


.counter
{
    display: flex;
    align-items: center;
    height: 50px;
    gap: 20px;
}

.counter button
{
    width: 50px;
    height: 50px;
    cursor: pointer;
}

/* Custom CSS classes */

.blue
{
    background-color: blue;
}

.bigger
{
    width: 500px;
    height: 500px;
}

.rotate
{
    transform: rotate(180deg);
}
```

## Stap 3: JavaScript-functionaliteit

Maak een JavaScript-bestand genaamd `script.js` en voeg de volgende functionaliteit toe:

```javascript
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
});

button3.addEventListener("click", () => {
    square.classList.toggle("rotate");
});

button4.addEventListener("click", () => {
    square.classList.toggle("blue");
    square.classList.toggle("bigger");
    square.classList.toggle("rotate");
});

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
```

## 1. Selecteren van HTML-elementen

De volgende regels code selecteren HTML-elementen door hun id's. Het `document.getElementById`-gedeelte zoekt naar een element in de HTML met de opgegeven id en wijst deze toe aan een variabele. Dit stelt ons in staat om later interactie te hebben met deze elementen in onze JavaScript-code.

```javascript
const button1 = document.getElementById("button1");
const button2 = document.getElementById("button2");
const button3 = document.getElementById("button3");
const button4 = document.getElementById("button4");
const square = document.getElementById("square");
```

## 2. Toevoegen van Event Listeners

Deze regels code voegen event listeners toe aan de eerder geselecteerde knoppen (`button1`, `button2`, `button3`, en `button4`). Wanneer er op een knop wordt geklikt, wordt de bijbehorende functie uitgevoerd.

- De functies gebruiken `classList.toggle()` om klassen toe te voegen of te verwijderen van het `square`-element. Dit geeft het effect van het wijzigen van de stijl van het vierkant wanneer er op de knoppen wordt geklikt.

```javascript
button1.addEventListener("click", () => {
    square.classList.toggle("blue");
});

button2.addEventListener("click", () => {
    square.classList.toggle("bigger");
});

button3.addEventListener("click", () => {
    square.classList.toggle("rotate");
});

button4.addEventListener("click", () => {
    square.classList.toggle("blue");
    square.classList.toggle("bigger");
    square.classList.toggle("rotate");
    let test = 1 + 1;
    console.log(test);
});
```

## 3. Verwerken van Tekst Input

Deze regels code selecteren een tekst invoerveld (`input_text`), een knop (`input_button`), en een div-element (`text`) waarin we tekst zullen weergeven.

- Een event listener wordt toegevoegd aan `input_button` die wordt geactiveerd wanneer erop wordt geklikt. De functie binnen de event listener wijzigt de `innerHTML` van het `text`-element naar de waarde die is ingevoerd in het `input_text`-veld.

```javascript
let input_text = document.getElementById("input_text");
let input_button = document.getElementById("input_button");
let text = document.getElementById("text");

input_button.addEventListener("click", () => {
    text.innerHTML = input_text.value;
});
```

## 4. Nummer Functionaliteit

Deze regels code declareren een variabele `number` met de waarde `20` en selecteren knoppen met de id's `minus` en `plus`.

- Event listeners worden toegevoegd aan deze knoppen. Wanneer er op de `minus`-knop wordt geklikt, wordt het nummer met 1 verminderd en wordt de nieuwe waarde weergegeven in het `final_number`-element. De lettergrootte van dit element wordt ook aangepast op basis van het nummer.
  
- Op een vergelijkbare manier, wanneer er op de `plus`-knop wordt geklikt, wordt het nummer met 1 verhoogd en worden dezelfde updates toegepast op het `final_number`-element.

```javascript
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
```

# JavaScript Functionaliteit Uitleg

## 1. FunctionaliteitButton

- We selecteren vier knoppen met de `getElementById`-methode en slaan ze op in variabelen: `button1`, `button2`, `button3`, en `button4`.
- Elke knop heeft een event listener die reageert wanneer erop wordt geklikt.
- Als er op `button1` wordt geklikt, wordt de `blue` klasse toegevoegd of verwijderd van het vierkant, waardoor de kleur van het vierkant wordt veranderd.
- Als er op `button2` wordt geklikt, wordt de `bigger` klasse toegevoegd of verwijderd van het vierkant, waardoor het vierkant groter of kleiner wordt.
- Als er op `button3` wordt geklikt, wordt de `rotate` klasse toegevoegd of verwijderd van het vierkant, waardoor het vierkant wordt geroteerd.
- Als er op `button4` wordt geklikt, worden de klassen `blue`, `bigger`, en `rotate` toegevoegd of verwijderd van het vierkant. Ook wordt de variabele `test` geïnitialiseerd met de waarde 2 en wordt deze waarde gelogd naar de console.

## 2. Tekst Input Functionaliteit

- We selecteren een tekst invoerveld (`input_text`) en een knop (`input_button`) om tekst in te dienen.
- Wanneer op de knop wordt geklikt, wordt de tekst die is ingevoerd in het invoerveld weergegeven in een ander element met de id `text`.

## 3. Nummer Functionaliteit

- We initialiseren een variabele `number` met de waarde 20 en selecteren twee knoppen (`minus` en `plus`) om het nummer te verminderen of te verhogen.
- Wanneer op de `minus` knop wordt geklikt, wordt het nummer met 1 verminderd en wordt het weergegeven in het element met de id `final_number`. Ook wordt de lettergrootte van dit element aangepast op basis van het nummer.
- Wanneer op de `plus` knop wordt geklikt, wordt het nummer met 1 verhoogd en wordt het weergegeven in het element met de id `final_number`. Ook wordt de lettergrootte van dit element aangepast op basis van het nummer.
