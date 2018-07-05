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
                    if ($('#dropdownMenuButton').html().trim() !== $('#id_username').val()){
                        msg = '<div id="js-mensaje-usuario" class="alert alert-danger" role="alert">'+data.error_message+'</div>'
                        $('.username_validado').attr("disabled", true);
                        $('.js-message').before(msg)
                    } else {
                        $('.username_validado').attr("disabled", false);
                        $('#js-mensaje-usuario').remove();
                    }
                }
            }
        });
    });

    //Carga form change_password
    $('#div-change-password').load('change_password')

    //Envía el form de apuestas a traves de AJAX
    $('.form-apuestas').on('submit', function(e){
        e.preventDefault();
        datos = $(this).serializeArray()
        $.ajax({
            type: "POST",
            url: 'apuestas',
            data: datos,
            success: function(){
                msg = '<div class="alert alert-info alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button>Apuesta realizada</div>'
                $('#betsCarousel').before(msg)
            },
        });
    });

    //Envía el form de datos de usuario a traves de AJAX
    $('#form-datos').on('submit', function(e){
        e.preventDefault();
        datos = $(this).serializeArray()
        $.ajax({
            type: "POST",
            url: 'datos',
            data: datos,
            success: function(){
                msg = '<div class="alert alert-info alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button>Tus datos se han modificado</div>'
                $('#form-datos').before(msg)
            },
        });
    });
});