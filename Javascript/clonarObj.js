const celular = {
    'marca': 'samsung',
    'polegadas': 6.5,
    'bateria': 5000,
    'ligar': function (){
        console.log('ligando...')
    }
}

// forma de cópia utilizando o métado assign 
const objetoCopia = Object.assign({
    teste: 'teste'
}, celular)
// console.log(objetoCopia)

// as novas propriedades do método não irá modificar o objeto real
const copiaOriginal = Object.assign({}, celular)
// console.log(copiaOriginal)


// outra forma mais simples
const copiaSimples= {...celular}
console.log(copiaSimples)
