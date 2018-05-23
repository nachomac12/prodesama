var modal = document.getElementById('modal');

const signUpTitle = document.getElementById('sign-up');
const signInTitle = document.getElementById('sign-in');

//Abro el modal según lo que quiera hacer, ya sea register o login
function chooseModal(option) {
  modal.classList.add('is-active');
  switch (option) {
        case 'register':
            signUpTitle.classList.add('is-active');
            signInTitle.classList.add('is-hidden');
            break;
        case 'login':
            signUpTitle.classList.add('is-hidden');
            signInTitle.classList.add('is-active');
            break;
    } 
}

//Cierra el modal
function closeModal() {
  modal.classList.remove('is-active');
}