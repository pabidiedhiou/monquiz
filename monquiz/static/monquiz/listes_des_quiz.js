//Création du modal
window.onload = () => {
    // On récupère tous les boutons d'ouverture de modale
    const modalButtons = document.querySelectorAll("[data-toggle=modal]");

    for(let button of modalButtons){
        button.addEventListener("click", function(e){
            // On empêche la navigation
            e.preventDefault();
            // On récupère le data-target
            let target = this.dataset.target

            // On récupère la bonne modale
            let modal = document.querySelector(target);
            // On affiche la modale
            modal.classList.add("show");

            // On récupère les boutons de fermeture
            const modalClose = modal.querySelectorAll("[data-dismiss=dialog]");

            for(let close of modalClose){
                close.addEventListener("click", () => {
                    modal.classList.remove("show");
                });
            }

            // On gère la fermeture lors du clic sur la zone grise
            modal.addEventListener("click", function(){
                this.classList.remove("show");
            });
            // On évite la propagation du clic d'un enfant à son parent
            modal.children[0].addEventListener("click", function(e){
                e.stopPropagation();
            })
        });
    }
}
//------------------------------------------------------------------
// Mes traitements
const modalBtns =[...document.getElementsByClassName('modal-button')];
const modalBody = document.getElementById('modal-body');
const boutonCommencer = document.getElementById('commencer');
const url =window.location.href
modalBtns.forEach(i=>i.addEventListener('click', ()=>{
    const pk = i.getAttribute('data-pk')
    const nomQuiz = i.getAttribute('data-quiz')
    const nbreQuestions = i.getAttribute('data-questions')
    const niveau = i.getAttribute('data-difficulte')
    const temps = i.getAttribute('data-temps')
    const score = i.getAttribute('data-score')

    modalBody.innerHTML = `
        <div> Êtes vous sure de vouloir commencer ${nomQuiz}?</div>
        <div>
            <ul>
                <li>Difficulté: <b>${niveau}</b></li>
                <li>Nombre de questions: <b>${nbreQuestions}</b></li>
                <li>Niveau: <b>${niveau}</b></li>
                <li>Durée: <b>${temps}min</b></li>
                <li>Score pour passer: <b>${score}%</b></li>
            </ul>
        </div>
    `

    boutonCommencer.addEventListener('click', (e)=>{
        e.preventDefault()
        const nouveauUrl =url+pk;
        window.location.href = nouveauUrl
        console.log(nouveauUrl)
    })
}))
