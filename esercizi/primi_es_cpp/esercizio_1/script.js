let listaEsercizzi = [];
async function caricaEsercizzi() {
    try {
        const response = await fetch("../../../json/Es_C++.json");
        const dati = await response.json();
        listaEsercizzi = dati.esercizzi; 
    } catch (error) {
        console.error("Errore nel caricamento:", error);
    }
}
document.addEventListener("DOMContentLoaded", async function (){
    await caricaEsercizzi();
    if (!Array.isArray(listaEsercizzi)) {
        console.error("Errore: listaEsercizzi non è un array");
        return;
    }
    let titolo =  document.getElementById("titolo");
    let testo = document.getElementById("testo");
    let schema = document.getElementById("schema");
    let stringhtmlschema =`
                <img width="50px" src="../../`+listaEsercizzi[0].pathimig+`">
                <a target="_blank" href="../../`+listaEsercizzi[0].pathhtml+`">
                    <h1>per l'html</h1>
                </a>`;
    let exe = document.getElementById("exe");
    let stringhtmlexe =`
                <img width="50px" src="../../../immagini/exe.png">
                <a target="_blank" href="../../`+listaEsercizzi[0].pathfileexe+`">
                    <h1>per scaricare il file exe</h1>
                </a>`;
    titolo.innerHTML = listaEsercizzi[0].titolo;
    testo.innerHTML = listaEsercizzi[0].testo;
    schema.innerHTML = stringhtmlschema;
    exe.innerHTML = stringhtmlexe;
});