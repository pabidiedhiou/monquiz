const url = window.location.href;
const boxQuiz = document.getElementById("box-quiz");
const arret = document.getElementById("arret");
const boxConteur = document.getElementById("box-conteur");
//----------HORLOGE-------------------------------------
const activeConteur = (temps) => {
  if (temps.toString().length < 2) {
    boxConteur.innerHTML = `<b>0${temps}:00</b>`;
  } else {
    boxConteur.innerHTML = `<b>${temps}:00</b>`;
  }
  let minutes = temps - 1;
  let secondes = 60;
  let deployerSecondes;
  let deployerMinutes;
  const compteur = setInterval(() => {
    secondes--;
    if (secondes < 0) {
      secondes = 59;
      minutes--;
    }
    if (minutes.toString().length < 2) {
      deployerMinutes = "0" + minutes;
    } else {
      deployerMinutes = minutes;
    }
    if (secondes.toString().length < 2) {
      deployerSecondes = "0" + secondes;
    } else {
      deployerSecondes = secondes;
    }
    if ((minutes === 0 && secondes === 0) || temps === 0) {
      boxConteur.innerHTML = `<b>00:00</b>`;
      setTimeout(() => {
        clearInterval(compteur);
        alert("C'est fini !!");
        envoyerDonnees();
      }, 500);
    }
    boxConteur.innerHTML = `<b>${deployerMinutes}:${deployerSecondes}</b>`;
  }, 1000);
  arret.addEventListener("click", () => {
    clearTimeout(compteur);
  });
};
//---------FIN HORLOGE----------------------------------
$.ajax({
  type: "GET",
  url: `${url}donnees`,
  success: function (response) {
    const donnees_recuperees = response.donnees;
    donnees_recuperees.forEach((element) => {
      for (const [question, reponses] of Object.entries(element)) {
        boxQuiz.innerHTML += `
                        <hr>
                        <div>
                            <b>${question}</b>♠♠
                        </div>
                    
                    `;
        reponses.forEach((reponse) => {
          boxQuiz.innerHTML += `

                        <div>
                            <input type="radio" class="reponse" id="${question}-${reponse}" name="${question}" value="${reponse}">
                            <label for="${question}">${reponse}</label>
                        </div>
                    `;
        });
      }
    });
    activeConteur(response.temps);
  },
  error: function (error) {
    console.log(error);
  },
});
/**/
const formQuiz = document.getElementById("form-quiz");
//const formQuiz = document.querySelector(".form-quiz")
const csrf = document.getElementsByName("csrfmiddlewaretoken");
const boxScore = document.getElementById("box-score");
const boxResultat = document.getElementById("box-resultat");

//---------------------------------------------------------------
const envoyerDonnees = () => {
  const elements = [...document.getElementsByClassName("reponse")];
  const donnees = {};
  donnees["csrfmiddlewaretoken"] = csrf[0].value;
  elements.forEach((element) => {
    if (element.checked) {
      donnees[element.name] = element.value;
    } else {
      if (!donnees[element.name]) {
        donnees[element.name] = null;
      }
    }
  });
  $.ajax({
    type: "POST",
    url: `${url}sauvegarder`,
    data: donnees,
    success: function (response) {
      const resultats = response.resultats;
      //console.log(resultats)
      formQuiz.classList.add("invisible");
      resultats.forEach((resultat) => {
        const divResultat = document.createElement("div");
        for (const [question, reponse] of Object.entries(resultat)) {
          //console.log(reponse)
          divResultat.innerHTML += question;
          const cls = ["container", "p-3", "text-light", "h3"];
          divResultat.classList.add(...cls);

          if (reponse == "pas de reponse") {
            divResultat.innerHTML += "- pas de reponse";
            divResultat.classList.add("bg-danger");
          } else {
            const answer = reponse["repondue"];
            const correcte = reponse["reponse_correcte"];

            if (answer == correcte) {
              divResultat.classList.add("bg-success");
              divResultat.innerHTML += `repondue: ${answer}`;
            } else {
              divResultat.classList.add("bg-danger");
              divResultat.innerHTML += `| reponse correcte :${correcte}`;
              divResultat.innerHTML += `| repondue :${answer}`;
            }
          }
        }
        //const body = document.getElementsByTagName("BODY")[0]
        boxResultat.append(divResultat);
      });
      boxScore.innerHTML = `${
        response.passe ? "Félicitation mon cher" : "yow khamo dara 🙈"
      } Votre resultat est: ${response.score}%`;
    },
    error: function (error) {
      console.log(error);
    },
  });
};

formQuiz.addEventListener("submit", (e) => {
  e.preventDefault();
  envoyerDonnees();
});
