window.addEventListener('DOMContentLoaded', function() {

    // Obtenir les éléments HTML
    const modal = document.getElementById("card-none");
    const btn = document.getElementById("L1");
    const span = document.getElementById("close")[0];
    const creat = document.getElementById('creat');

    // Lorsque le bouton est cliqué
    btn.addEventListener('mouseover', () => {

        modal.style.display = "block";
        if (true) {

            const assist = document.getElementById("container-mt4_div");
            assist.style.display = "none";
            if (creat.style.display = "none") {


                creat.style.display = "unset";

                if (true) {}





            }

        }
        //alert('hellp');
    });

    // Lorsque l'utilisateur clique en dehors de la fenêtre modale ou sur le bouton de fermeture




    window.onclick =
        function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }

    const itemfiliere = document.getElementById("itemfiliere");

    itemfiliere.addEventListener("click", () => {
        const testzz = document.getElementById("testz");
        //const cdiv = document.createElement("div");
        const cp = document.createElement("p");

        if (creat.style.display = "unset") {

            creat.style.display = "none";
        }






        testzz.textContent = " Heure Lundi Mardi Mercredi Jeudi Vendredi Samedi Dimanche";






    });

});