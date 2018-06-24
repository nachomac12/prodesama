$( document ).ready(function() {
    //Carga el cuerpo del modal
    $('#aInit').click(function(){
        $('.modal-title').html('Iniciar sesión');
        $('.modal-body').load('login');
    });
    $('#aReg').click(function(){
        $('.modal-title').html('Registrate');
        $('.modal-body').load('signup');
    });
    
    //Chequea que no se envíen campos del formulario en blanco
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

    //Validar usuario
    $("#id_username").change(function () {
        $.ajax({
            url: '/validate_username/',
            data: {
                'username': $(this).val()
            },
            dataType: 'json',
            success: function (data) {
                if (data.is_taken) {
                    $('.username_validado').attr("disabled", true);
                    alert("Ya existe un usuario con ese nombre");
                } else {
                    $('#.username_validado').attr("disabled", false);
                }
            }
        });
    });
});