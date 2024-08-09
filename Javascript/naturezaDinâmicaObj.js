// objetos em javascript são dinâmicos

const mouse = {
    'cor': 'red',
    'marca': 'pichau'
}

mouse.velocidade = 5000;
mouse.mudarDPI = function(nDPI){
    mouse.velocidade = nDPI
}

mouse.mudarDPI(1000)
console.log(mouse)
