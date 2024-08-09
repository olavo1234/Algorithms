// função de fabrica em javascript

function criarHumano(nome, corCabelo, corOlho){
    return {
        corOlho,
        corCabelo,
        nome,
        andar(){
            console.log('Andando...')
        } 
    }
}

pessoa = criarHumano('olavo', 'marrom', 'castanho')

pessoa.andar()
console.log(pessoa.nome)
console.log(pessoa.corCabelo)
console.log(pessoa.corOlho)

pessoa2 = criarHumano('sônia', 'marrom claro', 'castano escuro')

pessoa2.andar()
console.log(pessoa2.nome)
console.log(pessoa2.corCabelo)
console.log(pessoa2.corOlho)

