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
        <a class="navbar-item navbar-item has-text-light" href="estadisticas.html">
          Estadísticas
        </a>
      </div>
    </div>
  </nav>
"""

avistamientos_head = """
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Vivan los Bichos</title>
    <link rel="stylesheet" href="./../../T2/css/mystyles.css">
    <link rel="stylesheet" href="./../../T2/css/hero_style.css">
    <link rel="stylesheet" href="./../../T2/css/pointer_style.css">
    <script src="./../../T2/js/avistamientos.js"></script>
    <script src="https://kit.fontawesome.com/929bc70b66.js" crossorigin="anonymous"></script>
</head>"""

success_head = """
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Vivan los Bichos</title>
  <link rel="stylesheet" href="./../../T2/css/mystyles.css">
  <link rel="stylesheet" href="./../../T2/css/hero_style.css">
  <script src="./../../T2/js/nuevafoto.js"></script>
  <script src="https://kit.fontawesome.com/929bc70b66.js" crossorigin="anonymous"></script>
  <script src="./../../T2/js/new_regiones_comunas.js"></script>
  <script src="./../../T2/js/avistamiento_singular.js"></script>
  <script src="./../../T2/js/validacion.js"></script>
</head>"""

hero_avistamientos = """
<section class="hero is-primary is-small-with-navbar has-background">
    <img class= "hero-background is-transparent" src="./../../T2/images/hero/pexels-pixabay-144243.jpg" alt="portada avistamientos">
    
    <div class="hero-body">
      <div>
        <h2 class="title is-3"> Listado de Avistamientos</h2>
      </div>
    </div>
  </section>"""