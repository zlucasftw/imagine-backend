/* let banner = document.querySelector('.imagem'); */
/* let imgTAG = document.createElement('img'); */
let imgTAG = document.querySelector('.imagem_carousel');

const botao = document.querySelectorAll("[data-botao-carousel]");
/* const carousel = document.querySelector("") */
const carousel = document.querySelector("[data-carousel]");

let slideAtivo;
botao.forEach(botao => {
    botao.addEventListener("click", () => {
        const proximo = botao.dataset.botaoCarousel === "proximo" ? 1 : -1;
        const slides = botao.closest("[data-carousel]").querySelector("[data-slides]");

        slideAtivo = slides.querySelector("[data-ativo]");

        let novoIndice = [...slides.children].indexOf(slideAtivo) + proximo;
        if (novoIndice < 0) {
            novoIndice = slides.children.length - 1;
        }

        if (novoIndice >= slides.children.length) {
            novoIndice = 0;
        }

        slides.children[novoIndice].dataset.ativo = true;
        delete slideAtivo.dataset.ativo;
    });
});

setInterval(() => {
    const slides = carousel.querySelector("[data-slides]");

    slideAtivo = slides.querySelector("[data-ativo]");

    let indice = [...slides.children].indexOf(slideAtivo) + 1;
    
    if (indice < 0) {
        indice = slides.children.length - 1;
    }

    if (indice >= slides.children.length) {
        indice = 0;
    }

    slides.children[indice].dataset.ativo = true;
    delete slideAtivo.dataset.ativo;

}, 6000)

/* setInterval(() => {
    const slides = carousel.querySelectorAll("[data-slides]");

    slideAtivo = slides[1].querySelectorAll("[data-ativo]");

    let indice = [...slides[1].children].indexOf(slideAtivo[1]) + 1;
    
    if (indice < 0) {
        indice = slides[1].children.length - 1;
    }

    if (indice >= slides[1].children.length) {
        indice = 0;
    }

    slides[1].children[indice].dataset.ativo = true;
    delete slideAtivo[1].dataset.ativo;

}, 6000) */


/* banner.appendChild(imgTAG); */

/* let contador = 1;
 */
/* window.onload(() => { */
    /* trocarImagem(); */
    /* setInterval(() => {
        imgTAG.src = `img/musicasbannerimg0${contador}.webp`;
        contador++; */
        /* if (contador == 2) {
            contador = 1;
        } */
    /* }, 1000) */
/* }) */


/* function trocarImagem() {
    setInterval(() => {
        imgTAG.src = `img/musicasbannerimg0${contador}.webp`;
        contador++; */
        /* if (contador == 2) {
            contador = 1;
        } */
/*     }, 1000)
} */

/* setInterval(() => {
    imgTAG.src = `img/musicasbannerimg0${contador}.webp`;
    contador++;
    if (contador > 4) {
        contador = 1;
    }
}, 3000) */

/* if (contador == 2) {
    contador = 1;
} */