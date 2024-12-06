//Cambiar el header cuando el usuario haga scroll

const header = document.querySelector("header");

window.addEventListener("scroll", function(){
    header.classList.toggle("sticky", this.window.scrollY > 60)
})
/*
//Mostrar un mensaje de alerta cuando haga un clic en el boton
document.querySelector('.btn').addEventListener('click', function(){
    alert('¡Tus datos se ingresaran!');
});

document.querySelector('.btn2').addEventListener('click', function(){
    alert('¡Tu infomacion es confidencial!');
});

//Aplicar a todos los botones de clase .btn
/*document.querySelectorAll('.btn').forEach(function(button){
    button.addEventListener('click', function(){
        alert("¡Tu informacion es confidencial!")
    })
})
*/
//Funcion para el primer boton
document.getElementById("btn-inf").addEventListener('click', function(){
    alert("¡Ingrese su informacion!");
})

//funcion para el segundo boton
document.getElementById("btn2-cita").addEventListener('click', function(){
    alert("Agenda tu cita");
})

//Seleccionar todos los enclaces dentro de la clase .navar
document.querySelectorAll('.navar a[href^="#"]').forEach(function(enlace){
    enlace.addEventListener('click', function(e){
        e.preventDefault();//prevenir el comportamiento por defecto del enlace
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'instant' 
        })
    })
})
/*
//Cambiar la imagen de fondo cada cierto segundo
const imagenes = [
        '../staticfiles/clientes/IMG/fondo.png',
        '../staticfiles/clientes/IMG/bienestar.jpg',
        '../staticfiles/clientes/IMG/fondo3.jpg',
        '../staticfiles/clientes/IMG/bien.jpg'
];
const homeSection = document.querySelector('.home');
const intervalo = 5000; //5000 ms=5s
let indiceImagen = 0;
function cambiarFondo(){
    homeSection.style.backgroundImage = `linear-gradient(to left,
    rgba(211,103,103,0.5),
    rgba(190,190,190,0.3)
), url(${imagenes[indiceImagen]})`;
indiceImagen =(indiceImagen + 1) % imagenes.length;
}
setInterval(cambiarFondo, intervalo);
*/

let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');
let enlaces = document.querySelectorAll('.navbar a');

menu.onclick = () => {
    navbar.classList.toggle('open');
    menu.classList.toggle('bx-x'); //hace que haga un intervalo de menu y x para cerrar
}

//esto hace que al seleccionar se cierre el enclace y se muestre
enlaces.forEach(link => {
    link.onclick = () => {
    navbar.classList.remove('open');
    menu.classList.remove('bx-x');
    }
})

var typed = new Typed('#typed', {
    strings: ['Tu salud', 'Es nuestra', 'Fortaleza'],
    typeSpeed:50,
    loop: "true",
    showCursor: "true",
    cursorChar: "_",
    backSpeed:20,
})