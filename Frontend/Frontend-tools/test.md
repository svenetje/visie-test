# Over Vue

Om Vue te leren is basiskennis van HTML, CSS en JavaScript nodig. Ook kan op den duur basiskennis van Node.js, npm/npx of Yarn nodig zijn.

Vue is een front-end JavaScript framework dat volgens Vue-specifieke syntax-regels met minder code een webapplicatie op een snellere wijze laat bouwen. Je hoeft slechts middels de `<script>` tag een verbinding te maken met Vue.js om te zorgen dat Vue alles voor je regelt.

```html
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
```

Vergelijkbare frameworks zijn Angular, React en Svelte. Vue is eenvoudiger dan Angular en React om mee te beginnen. Vue is template gebaseerd. Het Vue framework genereert op het moment van laden of met een build commando met Node voornamelijk alle JavaScript code.

Er zijn 2 manieren om in Vue code te schrijven:
1. Options API
2. Composition API

## Een eenvoudig voorbeeld:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Mijn eerste Vue pagina</title>
</head>
<body>

  <div id="app">
    {{ message }}
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>

  <script>
    const app = Vue.createApp({
      data() {
        return {
          message: "Welkom op mijn eerste Vue-pagina!"
        }
      }
    })

   app.mount('#app')

  </script>
</body>
</html>
```

## Uitleg voorbeeld:

In bovenstaand voorbeeld wordt na het laden van Vue een instance/class aangemaakt en toegewezen aan de constante `app`. Vervolgens koppelt/mount Vue deze aan de `<div>` met de id="app" waarna de browser de `{{message}}` variabele invult met de waarde die de `message` eigenschap van de app class heeft, die vermeld staat onder het kopje `data()` nl "Welkom op mijn eerste Vue-pagina!".

## Wat kun je zoal met Vue bouwen:
1. SPA, Single Page Application / enkele webpagina
2. Volledige website / webapplicatie
3. Front-end met een koppeling naar een back-end zoals Laravel of Wordpress

## Reactief framework:
Vue is een reactief framework. Dat betekent dat bij verandering van data of bijvoorbeeld een klik de template opnieuw wordt opgebouwd terwijl de pagina op zich niet wordt herladen. Slechts een deel van de pagina HTML-code wordt dan aangepast/gemanipuleerd.

## Grote opdracht/project:
Mijn luidsprekerconfigurator project als basis?

## Bronnen:

- [W3Schools](https://www.w3schools.com)