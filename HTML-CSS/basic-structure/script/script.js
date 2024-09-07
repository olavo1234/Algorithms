var contador = 0;

const botaoModo = document.getElementById("alterarModo");

botaoModo.addEventListener('click', function(){ 
    if (contador % 2 == 0) {
        const elementos = document.querySelectorAll("body");
        elementos.forEach(elemento => {
            elemento.style.background = "white";
        });
        
        const font_elementos = document.querySelectorAll(".text");
        font_elementos.forEach(font_elementos => {
            font_elementos.style.color = 'black'
        });
    }else{
        const elementos = document.querySelectorAll("body");
        elementos.forEach(elemento => {
            elemento.style.background = "black";
        });
        
        const font_elementos = document.querySelectorAll(".text");
        font_elementos.forEach(font_elementos => {
            font_elementos.style.color = 'white'
        });
    }; 
    
    contador++;
});
