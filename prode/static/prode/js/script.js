$( document ).ready(function() {
    $('#aInit').click(function(){
        $('.modal-title').html('Iniciar sesión');
        $('.modal-body').load('login');
    });
    $('#aReg').click(function(){
        $('.modal-title').html('Registrate');
        $('.modal-body').load('signup');
    });
    
    $('#submitForm').click(function(){
        $('#formulario').submit();
    });
});