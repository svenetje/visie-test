## Quick Details

- **Opdracht ID:** 0
- **Opdracht titel:** Weerdata API
- **Opdracht Programmeertalen en/of tech:** C#
- **Opdracht (geschatte) moeilijkheidsgraad:** Gemiddeld
- **Opdracht Eisen:** Weerdata moet worden opgehaald, verwerkt en in grafieken worden weergegeven
- **Opdracht Extra Omschrijving:**
- **Titel:** Weerdata API
- **Programmeertaal:** C#

## Opdrachtbeschrijving

In deze opdracht ga je een applicatie ontwikkelen die weerdata ophaalt van een externe API, deze verwerkt en in grafieken weergeeft. Je zult gebruik maken van C# als programmeertaal en verschillende bibliotheken om de gegevens te verwerken en de grafieken te genereren. Deze opdracht heeft een gemiddelde moeilijkheidsgraad en is bedoeld om je vaardigheden in het werken met API's, data-analyse en grafische weergave te verbeteren.

## Benodigdheden

1. Visual Studio of een andere geschikte C# ontwikkelomgeving: Je hebt een IDE (Integrated Development Environment) nodig om de code te schrijven, te compileren en te debuggen.
2. Een weerdata API, zoals OpenWeatherMap (https://openweathermap.org/api): Hiermee krijg je toegang tot weerdata zoals temperatuur, luchtvochtigheid, windsnelheid en meer.
3. Een JSON-verwerkingsbibliotheek, zoals Newtonsoft.Json (https://www.newtonsoft.com/json): Deze bibliotheek helpt je bij het eenvoudig verwerken van JSON-gegevens die je van de API ontvangt.
4. Een grafiekbibliotheek, zoals OxyPlot (https://oxyplot.github.io/documentation/): Met deze bibliotheek kun je grafieken genereren om de weerdata visueel weer te geven.

## Stappen

1. Maak een nieuw C# project aan in je ontwikkelomgeving: Kies het type project dat het beste bij je past, bijvoorbeeld een console-applicatie, WPF-applicatie of een ASP.NET-webapplicatie.
2. Voeg de benodigde bibliotheken toe aan je project via NuGet of een andere pakketbeheerder: Dit maakt het eenvoudiger om de bibliotheken te integreren en te beheren binnen je project.
3. Registreer je voor een API-sleutel bij de gekozen weerdata API-provider en sla deze op in je applicatie: Bewaar de API-sleutel op een veilige manier, bijvoorbeeld in een configuratiebestand of als een constante in je code.
4. Schrijf een functie om de API-aanvraag te doen en de ontvangen JSON-gegevens te verwerken: Maak gebruik van de JSON-verwerkingsbibliotheek om de ontvangen gegevens om te zetten naar bruikbare objecten of datastructuren.
5. Creëer een gegevensmodel voor de weerdata die je van de API ontvangt: Definieer klassen of structs die de verschillende gegevensvelden vertegenwoordigen, zoals temperatuur, luchtvochtigheid en windsnelheid.
6. Schrijf een functie om de verwerkte weerdata om te zetten in grafiekpunten: Converteer de gegevens naar een formaat dat de grafiekbibliotheek kan gebruiken om grafieken te genereren.
7. Implementeer de grafiekbibliotheek om de grafieken te genereren op basis van de verwerkte weerdata: Configureer de grafiekbibliotheek volgens de gewenste weergave en stijl, en gebruik de geconverteerde gegevens om de grafieken te tekenen.
8. Voeg gebruikersinterface-elementen toe om de grafieken weer te geven en de gegevens bij te werken wanneer er nieuwe gegevens beschikbaar zijn: Dit kan onder andere een knop zijn om de gegevens te verversen of een selectievakje om te kiezen welke gegevens in de grafiek moeten worden weergegeven.

## Einddoel

Aan het einde van deze opdracht moet je een werkende applicatie hebben die weerdata ophaalt van een externe API, deze verwerkt en in grafieken weergeeft. De grafieken moeten realistische en bruikbare informatie over het weer bevatten, zoals temperatuurverloop, luchtvochtigheid of windsnelheid. Op basis van deze gegevens kunnen gebruikers bijvoorbeeld beter inschatten wat voor kleding ze moeten dragen of welke activiteiten ze kunnen plannen.

Succes met de opdracht!
