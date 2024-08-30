class Endereço{
    constructor(rua,cidade,cep){
        this.rua = rua;
        this.cidade = cidade;
        this.cep = cep;
    }

    exibirEndereço(){
        console.log(
            `Rua: ${this.rua}\nCidade: ${this.cidade}\nCEP: ${this.cep}`
        );
    }
}


class Pessoa{
    constructor(nome,idade){
        this.nome = nome
        this.idade = idade
    }
}


const meuEndereço = new Endereço('a','b','c');
const b = meuEndereço;
const c = new Pessoa('olavo',16);
const meuNovoEndereco = new Endereço('a','b','c');


function saoIquais(endereco1,endereco2){
    // função que irá comparar os atributos dos
    // objetos 1 e 2 e retornar true or false
    for (atributos1 in endereco1){
        // primeiro for irá interar as propriedades
        // sobre o objeto1
        for (atributos2 in endereco2){
            // segundo for sobre o objetos 2 
            if (
                // esse if fará a comaparação sobre
                // o nome desses atributos e valores
                atributos1 == atributos2 && 
                endereco1[atributos1] == endereco2[atributos2]
            ){
                // se for igual, continua verificando as próximas propriedades
                continue;
            }else{
                return false;
            }
        }
    }
    // se for iqual irá se true 
    return true;
}

function enderecoMemoriaIqual(endereco1, endereco2){
    if (endereco1 === endereco2) {
        return true;
    }else{
        return false;
    }
}

console.log(saoIquais(meuEndereço, c));
console.log(enderecoMemoriaIqual(meuEndereço, b));












class Pessoa1{
    constructor(nome,idade){
        this.identificador = nome;
        this.anos = idade;
    }
}

const d = new Pessoa1('olavo',16);
const arrayDeProp = Object.getOwnPropertyNames(d);
console.log(arrayDeProp);


function isEquivalent(a, b) {
    // Create arrays of property names
    var aProps = Object.getOwnPropertyNames(a);
    // ele passa esse método get para pegar
    // os nomes das propriedades desses 
    // objetos e colocar no vetor 
    var bProps = Object.getOwnPropertyNames(b);

    // If number of properties is different,
    // objects are not equivalent
    if (aProps.length != bProps.length) {
        return false;
    }

    for (var i = 0; i < aProps.length; i++) {
        var propName = aProps[i];

        // If values of same property are not equal,
        // objects are not equivalent
        if (a[propName] !== b[propName]) {
            return false;
        }
    }

    // If we made it this far, objects
    // are considered equivalent
    return true;
}
console.log(isEquivalent(c,d));
console.log(saoIquais(c,d));
