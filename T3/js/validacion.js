var meses_31_dias = ["01","03","05","07","08","10","12"];
var meses_30_dias = ["02","04","06","09","11"];

var corregir_mensaje = "";

function valida_region(id_region){
    var region = document.getElementById(id_region);
    var region_actual = region.value;
    if (region_actual == ''  || region_actual == -1){
        corregir_mensaje += "<li> Seleccione una región </li>";
        return false;
    }
    return true;
    
}

function valida_comuna(id_comuna){
    var comuna = document.getElementById(id_comuna);
    var comuna_actual = comuna.value;
    if (comuna_actual == ''  || comuna_actual == -1){
        corregir_mensaje += "<li> Seleccione una comuna </li>";
        // Caso cuando no es correcta la comuna
        return false;
    }
    return true;
    
}

function valida_sector(id_sector){
    var sector = document.getElementById(id_sector);
    var sector_actual = sector.value;
    var regex = /^[A-zÜÑÁÉÍÓÚáéíóúüñ0-9]+(\s[A-zÜÑÁÉÍÓÚáéíóúüñ0-9]+)*$/;
    var largo_sector = sector_actual.length;
    // No se escribió un sector, ok pues es OPCIONAL
    if (sector_actual == ""){
        return true;
    }
    if (largo_sector > 200){
        corregir_mensaje += "<li> Sector escrito supera los 100 carácteres </li>";
        return false;
    }
    if (!regex.test(sector_actual)){
        corregir_mensaje += "<li> El sector solo puede contener letras, números y espacios entre palabras</li>";
        return false;
    }
    return true;
}

function validar_nombre(id_nombre) {
    var nombre = document.getElementById(id_nombre);
    var nombre_actual = nombre.value;
    var largo_nombre = nombre_actual.length;
    var regex = /^(([A-ZÜÑÁÉÍÓÚ]+([a-záéíóúüñ]*))(\s[A-ZÜÑÁÉÍÓÚ]+([a-záéíóúüñ]*))*)$/;// Nombres con caracteres especiales
    if (nombre_actual == "") {
        corregir_mensaje += "<li> Ingrese un nombre </li>";
        return false;
    }
    else if (largo_nombre > 100) {
        corregir_mensaje += "<li> Largo no válido </li>";
        return false;
    }
    else if (!regex.test(nombre_actual)) {
        corregir_mensaje += "<li> Los nombres solo puede tener letras y espacios, también deben empezar con mayúsculas</li>";
        return false;
    }
    return true;
}

function validar_email(id_correo) {
    var correo = document.getElementById(id_correo);
    var correo_actual = correo.value;
    var regex = /^[^@]+@[^@]+\.[a-zA-Z]{2,}$/

    if (correo_actual == ""){
        corregir_mensaje += "<li> Ingrese su email </li>";
        return false;
    }
    else if (!regex.test(correo_actual)){
        corregir_mensaje += "<li> El correo electrónico es inválido </li>";
        return false;
    }
    return true;
}

function validar_celular(id_celular) {
    var celular = document.getElementById(id_celular);
    var celular_actual = celular.value;
    var regex = /^\+569\d{8}$/; // Numeros de chile
    if (celular_actual == ""){
        return true; // No escribió celular
    }
    else if (!regex.test(celular_actual)){
        corregir_mensaje += "<li> El número de celular es inválido </li>";
        return false;
    }
    return true;
}

function validar_fecha(clase_fecha) { // Formato año-mes-diahora:minuto 2000-09-11 12:11
    var nodos_fechas = document.getElementsByClassName(clase_fecha);
    var regex = /\d{4}-((0[1-9])|(1[0-2]))-((0[1-9])|([1-2][0-9])|(3[0-1])) (([0-1][0-9])|(2[0-3])):(([0-5][0-9]))$/; // regex fecha
    for (nodo of nodos_fechas) {
        fecha_actual = nodo.value;
        
        // Fecha_vacía
        if (fecha_actual == "") {
            corregir_mensaje += "<li> Ingrese una fecha </li>"
            return false;
        }
        // Formato incorrecto
        if (!regex.test(fecha_actual)) {
            alert("aka4")
            corregir_mensaje += "<li> Fecha Inválida </li>"
            return false;
        }

        anho = fecha_actual.substring(0,4)
        mes = fecha_actual.substring(5,7)
        dia = fecha_actual.substring(8,10)
        anho_numero = parseInt(anho);
        // Febrero
        
        if (mes == "02"){
            if (parseInt(dia) > 29) {
                alert("aka2")
                corregir_mensaje += "<li> Fecha inválida </li>";
                return false;
            } 
            if (dia == "29") {
                if ((((anho_numero % 4 == 0) && (anho_numero % 100 != 0 )) || (anho_numero % 400 == 0))) {
                    // Es biciesto
                    return true;
                }
                alert("aka3")
                corregir_mensaje += "<li> Fecha inválida </li>";
                return false;
            }
        }
        else if ((mes in meses_30_dias) && (dia=="31")){
            alert("aca1")
            corregir_mensaje += "<li> Fecha inválida </li>";
            return false;
        }
    }
    return true;
}

function validar_tipo(clase_tipo) {
    var tipos_lista = document.getElementsByClassName(clase_tipo);
    var cantidad_tipos = tipos_lista.length;
    
    for (tipo of tipos_lista) {
        tipo_actual = tipo.value;
        if (tipo_actual == ''  || tipo_actual == -1){
            if (cantidad_tipos > 1) {
                corregir_mensaje += "<li> Seleccione tipo en todos los avistamientos </li>";
            }
            else {
                corregir_mensaje += "<li> Seleccione un tipo </li>";
            }
            return false;
        }
    }
    return true;
}

function validar_estado(clase_estado) {
    var estados_lista = document.getElementsByClassName(clase_estado);
    var cantidad_estados = estados_lista.length;
    for (estado of estados_lista) {
        estado_actual = estado.value;
        if (estado_actual == ''  || estado_actual == -1){
            if (cantidad_estados > 1) {
                corregir_mensaje += "<li> Seleccione estado en todos los avistamientos </li>";
            }
            else {
                corregir_mensaje += "<li> Seleccione un estado </li>";
            }
            return false;
        }
    }
    return true;
}

function validar_imagenes(clase_imagen) {
    var nodos_lista_imagenes = document.getElementsByClassName(clase_imagen);
    var cantidad_imagenes = nodos_lista_imagenes.length;
    var regex = /\S*.(?:jpg|jpeg|png|JPG|JPEG|PNG)$/; // regex imagen
    for (nodo of nodos_lista_imagenes) {
        imagen = nodo.value;
        if (imagen.length < 1) {
            if (cantidad_imagenes > 1) {
                corregir_mensaje += "<li> No se adjuntaron todas las imágenes </li>";
                return false;
            }
            else {
                corregir_mensaje += "<li> No se adjuntó la imagen </li>";
                return false;
            }
        }
        if (!regex.test(imagen)) {
            if (cantidad_imagenes > 1) {
                corregir_mensaje += "<li> El formato de alguna imagen no es válido </li>";
                return false;
            }
            else {
                corregir_mensaje += "<li> El formato de la imagen no es válido </li>";
                return false;
            }
        }
    }
    return true;
}

function mostrar_notificacion() {
    var notificacion = document.getElementById("notificacion-formulario");
    notificacion.classList.remove('is-hidden');
}

function esconder_notificacion() {
    var notificacion = document.getElementById("notificacion-formulario");
    notificacion.classList.add('is-hidden');
    corregir_mensaje = "";
}

function agregar_correcciones() {
    var nodo_notificacion = document.getElementById("notificacion-formato");
    nodo_notificacion.innerHTML = corregir_mensaje;
}

function validar_todo() {
    corregir_mensaje = "Corrija los siguientes problemas para enviar el formulario:";
    var resultado = true;
    var check_list = [valida_region("region"), valida_comuna("comuna"), valida_sector("sector"), validar_nombre("nombre"),
    validar_email("email"), validar_celular("celular"), validar_fecha("dia-hora-avistamiento"), validar_tipo("tipo-avistamiento"),
    validar_estado("estado-avistamiento"), validar_imagenes("foto-avistamiento")];
    
    for (value of check_list) {
        if (!value) {
            resultado = false;
            break;
        }
    }

    if (!resultado) {
        mostrar_notificacion();
        agregar_correcciones();
        return resultado;
    }
    return resultado;
}


function obtenerFecha() {
    var hoy = new Date();
    var mes = hoy.getMonth() + 1;
    if (mes < 10) {
        mes = '0' + mes;
    }
    var dia = hoy.getDate();
    if (dia < 10) {
        dia = '0' + dia;
    }
    var hora = hoy.getHours();
    if (hora < 10) {
        hora = '0' + hora;
    }
    var minuto = hoy.getMinutes();
    if (minuto < 10) {
        minuto = '0' + minuto;
    }
    var fecha = hoy.getFullYear() + '-' + mes + '-' + dia + ' ' + hora + ':' + minuto;
    return fecha;
}

function actualizarFechaUno() {
    nodo = document.getElementById("dia-hora-avistamiento-1");
    nodo.value = obtenerFecha();
}