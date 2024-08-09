/*

// Pascal Case
function Celular(marcaCelular,tamanhoCelular,capacidadeBateria){
// anderline para ter a identificação de algo interno
    this._marcaCelular = marcaCelular,
    this._tamanhoCelular = tamanhoCelular ,
    this._capacidadeBateria = capacidadeBateria,
    this._ligar = function(){
        console.log('Ligando...')
    }
}

const celular = new Celular('sansumg', 6.8,5000)

console.log(celular._marcaCelular)
console.log(celular._capacidadeBateria)
// chamar a função
celular._ligar()

*/


// forma atualizado do metado construtor

class Cellphone{
    constructor(marcaCelular){
        // _ marca com algo interno
        this._marcaCelular = marcaCelular
    }

    // o que acontece quando se tenta  
    // atribuir um valor para essa propriedade
    set marcaCelular(string){
        this._marcaCelular = string
    }

    // o que acontece quandio de tenta
    // pegar o valor dessa propriedade
    get marcaCelular(){
        return this._marcaCelular 
    }

    toConect() {
        return (`O celular ${this._marcaCelular} está ligando...`)
    }
}

const celular = new Cellphone('samsung')

// para setar uma nova marca
celular._marcaCelular = 'iphone'
console.log(celular._marcaCelular)
// 

console.log(celular._marcaCelular)
// utilizando o get
console.log(celular.marcaCelular)
// 
console.log(celular.toConect())






class Pessoa{
    constructor(corPele,corOlho,nome){
        this._corPele = corPele
        this._corOlho = corOlho
        this._nome = nome
    }
}

const pessoa = new Pessoa('branco','castanho','olavo')

console.log(pessoa._corPele)
console.log(pessoa._corOlho)
console.log(pessoa._nome)
