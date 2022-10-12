$(document).ready(function () {
  consultarSubCategorias();
  consultarCategorias();
  dejarBarra();
});
  








 


async function consultarCategorias() {
  data = await obtenercategorias();
  
    
    for (i = 0; i < 4; i++) {
      
      cat = JSON.stringify(data.categorias[i].categoria).replace('"', '').replace('"', '').toLowerCase();
      
      $(document).on('load', 
      
      $(".listaCategorias").append('<a  id="'+ cat +'" class="nav-link ml-5 elementoNav nav" href="">' + cat + '</a>')
      
      );
    }
  
  
  


}

async function consultarSubCategorias() {
  categorias = await obtenercategorias();
  subcategorias = await obtenerSubcategorias();
 $(".elementoNav").mouseenter(function () {
  $("#opcionesBarra").empty();
  elemento = $(this).attr('id');
  
  console.log(elemento);
    $("#opcionesBarra").animate({ width: '100%' }, 700);

    categorias.categorias.forEach(cat => {

      if (cat.categoria.toLowerCase() == elemento) {
        b = 0;
        for (i = 0; i <= 11; i++) {
          
          if (subcategorias.categorias[i].categoria_id == cat.id) {
            subElemento = JSON.stringify(subcategorias.categorias[i].subcategoria).replace('"', '').replace('"', '').toLowerCase();
            $("#opcionesBarra").append('<a class="nav-link float-left subcategoria" href="">' + subElemento + '</a><div class="float-left lateralBarraSubcategoria"></div>');

            b++;
          }

        }

      }
    });

    $('.lateralBarraSubcategoria').animate({height: "70%", width: "2px"}, 700);

    
  });

}










async function obtenercategorias() {
  let url = new URL("http://127.0.0.1:8000/libreria/obtenercategorias/");
  const dataRequest = {
    method: 'GET'
  };
  let response = await fetch(url, dataRequest);
  result = await response.json();
  return result;
}

async function obtenerSubcategorias() {
  let url = new URL("http://127.0.0.1:8000/libreria/obtenersubcategorias/");
  const dataRequest = {
    method: 'GET'
  };
  let response = await fetch(url, dataRequest);

  result = await response.json();
  return result;
}

/*function cargarImgPromo(){
  $('.divPromos').children().attr('class', 'img-fluid ');
  $('.divTodasLasPromos').children().attr('class', 'divPromos col-1 m-3'); 
}*/

function dejarBarra(){
  $("#barraEntera").mouseleave(function () {
    $("#opcionesBarra").animate({ width: '0%' }, 1000).empty();
    
  });

  $("#opcionesBarra").mouseleave(function () {
    $("#opcionesBarra").animate({ width: '0%' }, 1000).empty();
    
  });
  
}