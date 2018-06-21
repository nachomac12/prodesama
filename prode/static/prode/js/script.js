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
        var form_inputs=$("#formulario").serializeArray();
        var blank=false;

        for (var input in form_inputs){
            if ((form_inputs[input]['value'] == "")) {
                blank=true;
            };
        };

        if (!blank){
            $('#formulario').submit();
        } else {
            alert('Por favor complete todos los campos del formulario')
        };
    });

    $('#list_apuestas').click(function(){
        $(this).css("background-color","white");
    });
});