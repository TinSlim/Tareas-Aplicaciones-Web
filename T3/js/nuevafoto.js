
contadores = [1]
counter_bichos = 0

/**
 * Añade otro input de archivo para el avistamiento del nodo.
 * @param {botón para agregar nueva imagen} node
 * @param {Número del avistamiento del formulario} number
 */

function add_photo(node,number) {
    contadores[number] += 1;
    if (contadores[number] <= 5) {
        var new_node = document.createElement("div");
        new_node.setAttribute("class", "field");
        new_node.innerHTML = `
        <div class="file has-name">
                <label class="file-label">
                    <input class="file-input foto-avistamiento" type="file" name="foto-avistamiento-${number}" onchange="filename_change(this,0)">
                    <span class="file-cta">
                    <span class="file-icon">
                        <i class="fas fa-upload"></i>
                    </span>
                    <span class="file-label">
                        Choose a file…
                    </span>
                    </span>
                    <span class="file-name">
                        Nombre del Archivo                                                  
                    </span>
                </label>
            </div>`
        node.parentNode.getElementsByClassName("archivos")[0].appendChild(new_node);
    }
}


/**
 * Cambia el nombre que aparece en el input de archivo por el archivo ingresado.
 * @param {input de tipo archivo} node
 */
function filename_change(node) {
    node.parentNode.getElementsByClassName("file-name")[0].innerHTML = node.files[0].name;
};


/**
 * Añade un nuevo avistamiento de insecto.
 * @param {botón para agregar un nuevo avistamiento} node
 */
function add_new_bug(node) {
    var fecha = obtenerFecha();
    counter_bichos += 1;
    contadores[counter_bichos] = 1;
    var new_node = document.createElement("div");
    new_node.setAttribute("class", "block");
    new_node.innerHTML =`
    <h2 class="title">Información de Avistamiento:</h2>
            <div class="field">
                <label class="label">Día hora<span class="has-text-danger" >*</span>:</label>
                <input class="input dia-hora-avistamiento" type="text" placeholder="año-mes-diahora:minuto" name="dia-hora-avistamiento" value='${fecha}' size="20">
            </div>
            <div class="field">
              <label class="label">Tipo<span class="has-text-danger" >*</span>:</label>
              <div class="select">
                <select class="tipo-avistamiento" name="tipo-avistamiento" value="tipo-avistamiento">
                  <option value=""> Seleccione un tipo </option>
                  <option value="no sé"> No sé </option>
                  <option value="insecto"> Insecto </option>
                  <option value="arácnido"> Arácnido </option>
                  <option value="miriápodo"> Miriápodo </option>
                </select>
              </div>
            </div>
            <div class="field">
              <label class="label">Estado<span class="has-text-danger" >*</span>:</label>
              <div class="select">
                <select value="estado-avistamiento" name="estado-avistamiento" class="estado-avistamiento">
                  <option value=""> Seleccione un estado </option>
                  <option value="no sé"> No sé </option>
                  <option value="vivo"> Vivo </option>
                  <option value="muerto"> Muerto </option>
                </select>
              </div>
            </div>
            <div class="archivos">
              <div class="field">
                <label class="label">Imagen<span class="has-text-danger" >*</span>:</label>
                <div class="file has-name">
                    <label class="file-label">
                        <input class="file-input foto-avistamiento" type="file" name="foto-avistamiento" onchange="filename_change(this)">
                        <span class="file-cta">
                        <span class="file-icon">
                            <i class="fas fa-upload"></i>
                        </span>
                        <span class="file-label">
                            Choose a file…
                        </span>
                        </span>
                        <span class="file-name">
                          Nombre del Archivo                                                  
                        </span>
                    </label>
                </div>
              </div>
            </div>
            <p class="help">Los formatos compatibles son .jpg .jpeg .png, las imágenes deben pesar menos de 10mb</p>
            <button class="button mt-4" type="button" onclick="add_photo(this,${counter_bichos})">
              Agregar otra foto
            </button>`
    node.parentNode.getElementsByClassName("avistamientos")[0].appendChild(new_node);
}
