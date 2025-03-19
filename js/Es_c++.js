let listaEsercizzi = [];
async function caricaEsercizzi() {
    try {
        const response = await fetch("../json/Es_C++.json");
        const dati = await response.json();
        listaEsercizzi = dati.esercizzi; 
        console.log(listaEsercizzi); 
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
    let divGrande = document.getElementById("div");
    if (!divGrande) {
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
                <img width="50px" src="../immagini/cpp.png">
                <a target="_blank" href="`+element.pathpaginahtml+`">
                    <h1>${element.titolo}</h1>
                </a>
            </div>
        `;
    });
    divGrande.innerHTML = htmlString;
});

