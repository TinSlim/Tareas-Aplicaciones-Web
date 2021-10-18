/**
 * Selecciona una fila
 * @param {fila} node 
 */
function select_row(node) {
    node.classList.add('is-selected');
}

/**
 * Deselecciona una fila
 * @param {fila} node 
 */
function deselect_row(node) {
    node.classList.remove('is-selected');
}