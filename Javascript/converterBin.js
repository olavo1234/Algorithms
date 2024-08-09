// let array_position = new Array()
// let array_bin = new Array()
// let resultado = new Array()
// let expoente = new Array()


// const N = 2;
// let bin = '1010';


// for (let i = 0; array_bin.length < bin.length; i++) {
//     array_bin.push(parseInt(bin[i]));
//     array_position.unshift(i);
// }

// converteBin();

// function converteBin() {
//     let total = 0

//     for(let i = 0; i < array_bin.length; i++) {
//         n2 = array_position[i]
//         resul = Math.pow(N, n2); 
//         expoente.push(resul);
//         resultado.push(expoente[i] * array_bin[i]);
//         total += resultado[i]
//     }
//     console.log(total) 
// }






function binToDec(bin) {
    const N = 2;
    let total = 0;

    for (let i = 0; i < bin.length; i++) {
        const bit = parseInt(bin[bin.length - 1 - i]);  // Pega o bit na posição correta
        total += bit * (N ** i);  // Calcula o valor decimal do bit
    }

    return total;
}

const bin = '10011011';
console.log(binToDec(bin));  // Deve imprimir 155
