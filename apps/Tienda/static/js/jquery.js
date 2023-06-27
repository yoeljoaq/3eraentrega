$(function(){
    $("#miFormulario").validate({
        rules:{
            correo:{
                required: true,
                minlength: 5
            },
            nombre:{
                required: true,
                minlength: 3
            },
            password:{
                required: true,
                minlength: 3
            }
        },
        messages:{
            correo:{
                required: "Debe ingresar correo electrónico.",
                minlength: "Debe ingresar minimo 5 caracteres."
            }
        }
    })
})
