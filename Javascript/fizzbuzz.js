// divisivel por 3 => fizz
// divisivel por 5 => buzz
// dividivel por 3 e 5 => fizzbuzz
// nao é divisivel 3 ou 5 => entrada
// nao é um numero => "nao é um numero"


// Um número é divisível por outro quando 
// o resto da divisão entre ambos é igual a zero



// versao longo do codigo e mais complexa 
// let resultado = (fizzbuzz(15));

// function fizzbuzz(entrada) {
//     valor_1 = entrada % 3;
//     valor_2 = entrada % 5;
//     if (valor_1 === 0 && valor_2 === 0) {
//         console.log("fizzbuzz");
//     }
//     else{
//         if(valor_1 === 0) {
//             console.log("fizz");
//         }
//         else if(valor_2 === 0) {
//             console.log("buzz");
//         }
//         else if(valor_1 > 1 || valor_2 > 1){
//             console.log(entrada);
//         }
//         else if (typeof entrada !== 'nunber') {
//             console.log('não é um numero');
//         }
// }
// }


// versao curta e menos complexa 
let resultado = fizzbuzz(15);
console.log(resultado);
// utilizou o return 
function fizzbuzz(entrada){
    if(typeof entrada !== 'number' ) // se for diferente 
        return 'não é um numero';
    if(entrada % 3 === 0 && entrada % 5 === 0) //comparador de iqualdade com 3 para somente numeros
        return 'fizzbuzz';
    if (entrada % 3 === 0)
        return 'fizz';
    if (entrada % 5 === 0) // parte falha do codigo
        return 'buzz';

    return entrada;
}
