let listaEsercizzi = [];
async function caricaEsercizzi() {
    try {
        const response = await fetch("../json/Es_C++.json");
        const dati = await response.json();
        listaEsercizzi = dati.esercizzi; 
    } catch (error) {
        console.error("Errore nel caricamento:", error);
    }
}
document.addEventListener("DOMContentLoaded", async function() {
    await caricaEsercizzi();
    if (!Array.isArray(listaEsercizzi)) {
        console.error("Errore: listaEsercizzi non è un array");
        return;
    }
    // esercizi semplici
    let divGrande1 = document.getElementById("div1");
    if (!divGrande1) {
        console.error("Elemento con id 'div' non trovato");
        return;
    }
    let primies = listaEsercizzi.filter(elemento => elemento.tipo === "primi es semplici");
    if (primies.length === 0) {
        console.log("Nessun esercizio trovato con tipo 'primi es semplici'");
    }
    let htmlString = "";
    primies.forEach(element => {
        htmlString += `
            <div class="box_contati">
                <a target="_blank" href="`+element.pathpaginahtml+`">
                    <img width="50px" src="../immagini/cpp.png">
                </a>
                <a target="_blank" href="`+element.pathpaginahtml+`">
                    <h1>${element.titolo}</h1>
                </a>
            </div>
        `;
    });
    divGrande1.innerHTML = htmlString;
    // esercizi con if
    let divGrande2 = document.getElementById("div2");
    if (!divGrande2) {
        console.error("Elemento con id 'div' non trovato");
        return;
    }
    let primies2 = listaEsercizzi.filter(elemento => elemento.tipo === "primi es con if ");
    if (primies2.length === 0) {
        console.log("Nessun esercizio trovato con tipo 'primi es semplici'");
    }
    let htmlString2 = "";
    primies2.forEach(element => {
        htmlString2 += `
            <div class="box_contati">
                <a target="_blank" href="`+element.pathpaginahtml+`">
                    <img width="50px" src="../immagini/cpp.png">
                </a>
                <a target="_blank" href="`+element.pathpaginahtml+`">
                    <h1>${element.titolo}</h1>
                </a>
            </div>
        `;
    });
    divGrande2.innerHTML = htmlString2;
    // esercizi con cicli
    let divGrande3 = document.getElementById("div3");
    if (!divGrande3) {
        console.error("Elemento con id 'div' non trovato");
        return;
    }
    let primies3 = listaEsercizzi.filter(elemento => elemento.tipo === "primi es con cicli ");
    if (primies3.length === 0) {
        console.log("Nessun esercizio trovato con tipo 'primi es semplici'");
    }
    let htmlString3 = "";
    primies3.forEach(element => {
        htmlString3 += `
            <div class="box_contati">
                <a target="_blank" href="`+element.pathpaginahtml+`">
                    <img width="50px" src="../immagini/cpp.png">
                </a>
                <a target="_blank" href="`+element.pathpaginahtml+`">
                    <h1>${element.titolo}</h1>
                </a>
            </div>
        `;
    });
    divGrande3.innerHTML = htmlString2;
});

