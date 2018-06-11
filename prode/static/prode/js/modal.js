var modal = document.getElementById('myModal');

const signUpTitle = document.getElementById('sign-up');
const signInTitle = document.getElementById('sign-in');
const registerButton = document.getElementById('register-button');
const loginButton = document.getElementById('login-button');
const loginBody = document.getElementById('login-body');
const registerBody = document.getElementById('register-body');

//Abro el modal según lo que quiera hacer, ya sea register o login
function chooseModal(option) {
  modal.classList.add('is-active');
  if (option=='register') {  //sign up
    signInTitle.classList.add('is-hidden'); 
    loginButton.classList.add('is-hidden');
    loginBody.classList.add('is-hidden');
    signUpTitle.classList.remove('is-hidden');
    registerButton.classList.remove('is-hidden');
    registerBody.classList.remove('is-hidden');
    }   
  else {  //sign in
    signInTitle.classList.remove('is-hidden'); 
    loginButton.classList.remove('is-hidden');
    loginBody.classList.remove('is-hidden');
    signUpTitle.classList.add('is-hidden');
    registerButton.classList.add('is-hidden');
    registerBody.classList.add('is-hidden');
  }
}

//Cierra el modal
function closeModal() {
  modal.classList.remove('is-active');
}

//Comando para abrir el modal de 'login'
$('#btnLogin').click(function(){
  $('#loginModal').modal('show');
});

//Comando para abrir el modal de 'signup'
$('#btnSignup').click(function(){
  $('#signupModal').modal('show');
});