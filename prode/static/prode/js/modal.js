var modal = document.getElementById('myModal');

//Comando para abrir el modal de 'login'
$('#btnLogin').click(function(){
  $('#loginModal').modal('show');
});

//Comando para abrir el modal de 'signup'
$('#btnSignup').click(function(){
  $('#signupModal').modal('show');
});