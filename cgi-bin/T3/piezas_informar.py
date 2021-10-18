#!/usr/bin/python3
# -*- coding: utf-8 -*-

formulario_informar1 = """
  <div class="columns is-mobile mt-5 mb-5">
    <div class="box column is-three-fifths is-offset-one-fifth">
      <form id="formulario" method="POST" enctype="multipart/form-data" action="informar.py" onsubmit="return validar_todo()">
        <div class="columns">
          <div class="mr-3 block column">
              <h2 class="title">Lugar:</h2> 
              <div class="field">
                  <label class="label">Región<span class="has-text-danger" >*</span>:</label>
                  <div class="select">
                    <select id="region" name="region" onchange="region_change(this)">
                      <option value=""> Seleccione una región</option>
                    </select>
                  </div>
              </div>
              <div class="field">
                  <label class="label">Comuna<span class="has-text-danger" >*</span>:</label>
                  <div class="select">
                    <select id="comuna" name="comuna">
                      <option value=""> Seleccione una comuna</option>
                    </select>
                  </div>
              </div>
              <div class="field">
                  <label class="label">Sector:</label>
                  <input id="sector" class="input" type="text" size="200" name="sector" maxlength="100">
              </div>
          </div>
          <div class="ml-3 block column">
              <h2 class="title">Datos de Contacto:</h2>
              <div class="field">
                  <label class="label">Nombre<span class="has-text-danger" >*</span>:</label>
                  <input id="nombre" class="input" type="text" name="nombre" size="100" maxlength="200">
                  <p class="help">Debe empezar con mayúscula y en caso de ser más de uno separarse con espacios</p>
              </div>
              <div class="field">
                  <label class="label">Email<span class="has-text-danger" >*</span>:</label>
                  <input id="email" class="input" type="text" name="email" size="100">
              </div>
              <div class="field">
                  <label class="label">Número de Celular:</label>
                  <input id="celular" class="input" type="text" name="celular" size="15" placeholder="Ejemplo: +569XXXXXXXX">
              </div>
          </div>
        </div>"""

formulario_informar2 = """<div class="avistamientos">
          <div class="block">
            <h2 class="title">Información de Avistamiento:</h2>
            <div class="field">
                <label class="label">Día hora<span class="has-text-danger" >*</span>:</label>
                <input id="dia-hora-avistamiento-1" class="input dia-hora-avistamiento" type="text" placeholder="año-mes-diahora:minuto" name="dia-hora-avistamiento" size="20">
            </div>
            <div class="field">
              <label class="label">Tipo<span class="has-text-danger" >*</span>:</label>
              <div class="select">
                <select class="tipo-avistamiento" name="tipo-avistamiento">
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
                <select name="estado-avistamiento" class="estado-avistamiento">
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
            <button class="button mt-4" type="button" onclick="add_photo(this,0)">
              Agregar otra foto
            </button>
          </div>
        </div>
        
        <button class="button is-link mt-3" type="button" onclick="add_new_bug(this)">
          Informar otro avistamiento en este sector
        </button>

        <button class="button is-primary mt-3" type="button" onclick=show_modal(this)>
          Enviar información del avistamiento
        </button>
        

        <!-- Modal -->
        <div class="modal">
          <div class="modal-background"></div>
          <div class="modal-card">
            <header class="modal-card-head">
              <h2 class="modal-card-title"> </h2>
            </header>
            <section class="modal-card-body">
              <h2>¿Está seguro que desea enviar esta información? </h2>
              <figure class="image is-128x128">
                <img src="./../../T3/images/cucaMexicana.jpg" alt="Cucaracha con sombrero mexicano">
              </figure>
              <div class="notification is-warning is-hidden" id="notificacion-formulario">
                <button type="button" class="delete" onclick="esconder_notificacion()"><span class="icon">
                <i class="fas fa-times"></i>
              </span></button>
                <div id="notificacion-formato"></div>
              </div>
            </section>
            <footer class="modal-card-foot">
              <div class="buttons">
                <button type="button" class="button is-danger" onclick="hide_modal_form(this)"> No estoy seguro,quiero volver al formulario </button>
                <button class="button is-success"> Sí,estoy total y absolutamente seguro</button>
              </div>
            </footer>
          </div>
        </div>
      </form>
    </div>
  </div>"""
        
hero_informar = """
  <!--Hero Avistamiento-->
  <section class="hero is-primary is-small-with-navbar has-background">
    <img class= "hero-background is-transparent" src="./../../T3/images/hero/pexels-thijs-van-der-weide-792952.jpg" alt="portada formulario">
    <div class="hero-body">
      <div>
        <h2 class="title is-3"> Informar Avistamiento </h2>
      </div>
    </div>
  </section>"""

footer = """
<footer class="footer">
    <div class="columns">
      <div class="column content has-text-centered">
        <div>
          <p><strong>CC5002 - Desarrollo de Aplicaciones Web</strong></p>
        </div>
        <a href="#">Cristóbal Torres Gutiérrez</a>
      </div>
      <div class="column">
      </div>
      <div class="column">
        <p>
          <a href="http://jigsaw.w3.org/css-validator/check/referer">
              <img style="border:0;width:88px;height:31px"
                  src="http://jigsaw.w3.org/css-validator/images/vcss"
                  alt="¡CSS Válido!" />
          </a>
      </p>
      </div>
    </div>
  </footer>
"""
navbar = """<nav class="navbar is-primary">
    <div class="navbar-brand">
      <a class="navbar-item" href="portada.py">
        <span class="icon has-text-white">
          <i class="fas fa-bug fa-lg fa-spin"></i>
        </span>
        <p class="title has-text-white">Vivan los Bichos</p>
      </a>

      <div class="navbar-burger" data-target="navbarShow">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>
    <div id="navbarShow" class="navbar-menu">
      <div class="navbar-start">
        <a class="navbar-item has-text-light" href="portada.py">
          Home
        </a>
        <a class="navbar-item navbar-item has-text-light" href="informar.py">
          Informar Avistamiento
        </a>
        <a class="navbar-item navbar-item has-text-light" href="avistamientos.py">
          Listado de Avistamientos
        </a>
        <a class="navbar-item navbar-item has-text-light" href="../../T3/htmls/estadisticas.html">
          Estadísticas
        </a>
      </div>
    </div>
  </nav>
"""        
