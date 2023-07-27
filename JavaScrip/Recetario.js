var recetas = [{
    "Nombre": "Brownie"
    "ingredientes" : ["azucar","cacao","manteca","huevos","harina"
    "preparacion": "Derretir la manteca, luego incorporar el cacao, en un boul batir los huevos con la azucar, juntar todo, ponerle la harina y mezclar durante varios minutos, precalentar el horno  "]
}
    {
        "ingredientes": ["arroz; agua; sal "],
        "preparacion": " poner el agua a hervir, colocar arroz y sal"
    },
    {
        "ingredientes": ["huevo, agua"],
        "preparacion": "colocar el agua con los huevos a hervir"
    },

{
    "Nombre":"Chocolatada"
    "ingredientes": ["cacao", "leche", "azucar"]
    "preparacion": "ingresar 3 cucharadas de cacao en una taza, 1 de azucar, leche hasta el borde y removeer "
}
];

var ingredientesDisponibles = [];


function: menu() {
    var html = `
    <button onclick="CrearNuevaReceta"()> NuevaReceta </button>
    <button onclick="Receta"()> encontrarReceta </button> 
    <button onclick="verIngredientes"()> ingredientes </button> 
    ` ;
output (html);
}
menu();



function volverLista() {
    clearInterval()
    verIngredientes();
}

function verIngredientes(){
    clear();
    for(var i=0; i< ingredientesDisponibles.length; i++) {
     output(ingredientesDisponibles[0])
     for( var i=1; i<ingredientesDisponibles.length; i++)
     output("," + ingredientesDisponibles[i])   
}
}

output("<br>");





function encontrarReceta() {
   output("<br>");
   var hayreceta = false
   for (var i = 1; i < recetas.length; i++) {
  if (posibleReceta (recetas[i])) {
    hayreceta = true 
    output( "Recetas disponibles" + recetas[i])
  }
   }    
}

function nuevaReceta() {   
var nuevaRe = input ("Contenido Nueva Receta") 
output(nuevaRe);
}