
// princípio da responsabilidade única

// camelCase
exibirNumeroPrimos(20)

function exibirNumeroPrimos(limite){
    for(let numero = 2; numero <= limite; numero++){
        if(numeroPrimo(numero)) console.log(numero);
        // o que for primo será passado da função para cá
    }
}

// o numero do laço passara como parametro
function numeroPrimo(numero){
    for(let divisor = 2; divisor < numero; divisor++){
        if(numero % divisor === 0){
            return false;
            // o que não for primo será ignorado
        }
    }
    return true;
    // o valor retornado será imprimodo no console
}
