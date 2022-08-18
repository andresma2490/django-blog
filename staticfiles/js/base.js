document.getElementById("year").innerHTML = new Date().getFullYear();

function loadModal(url, id = "mainModal") {
    const modal = document.getElementById(id);
    const modal_bs = new bootstrap.Modal(modal);
    fetch(url)
        .then((response) => response.text())
        .then((html) => {
            modal.querySelector(".modal-content").innerHTML = html;
            modal_bs.show();
        })
        .catch((error) => {
            console.error(error);
        });
}

function submitForm(id) {
    const form = document.getElementById(id);
    form.submit();
}
