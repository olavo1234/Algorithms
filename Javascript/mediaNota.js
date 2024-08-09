// EXERCICIO PARA APRENDER A MANIPULAR ARRAYS E LOOPS NO JS 


// exercicio nota escola
// obter a me apartir de um array

// para achar a media somar todas as notas e dividir pela quantidade de notas

// 0-59: F
// 60-69: D
// 70-79: C
// 80-89: B
// 90-100: A

const array = [70,70,80];

console.log(mediaDoAluno(array)); 

// principio da responsabilidade unica (cada bloco de codigo tera uma função com sua propria utilidade)
function mediaDoAluno(notas) {
    const media = calcularMedia(notas)// vai chamar a conta e colocar na variavel media
    if (media < 59) return 'F';// sequencia de ifs 
    if (media < 69) return 'D';
    if (media < 79) return 'C';
    if (media < 89) return 'B';
    return 'A';
}
// funçao que vai calcular a media
function calcularMedia(array){
    let soma = 0;// declarar uma variavel com valor 0
    for (let valor of array) { // vai passar por cada valor do array
        soma += valor;// vai somar na variavel soma
    }
    return soma/(array.length)// vai entregar a operação para a função de cima
}
