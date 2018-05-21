const Modal = (function () {

// Abre el modal

function open($modal) {
    const singUpTitle = document.getElementById('sign-up');
    const signInTitle = document.getElementById('sign-in');
    const saveButton = document.getElementById('save-button');
    const logInButton = document.getElementById('log-in-button');

    $modal.classList.add('is-active');
    signUpTitle.classList.add('is-active');
    saveButton.classList.add('is-active');
    signInTitle.classList.add('is-hidden');
    logInButton.classList.add('is-hidden');
}

// Cierra el modal
function close($modal) {    
    $modal.classList.remove('is-active');
}


})();