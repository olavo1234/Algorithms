let encerrar = 'não'
while(encerrar === 'não' | encerrar === 'nao'){
    let idadeUsuario = prompt('Informe a sua idade')

    if (idadeUsuario >= 18){
        alert('Você é maior de idade')
    }else{
        alert('Você é menor de idade')
    }
    encerrar = prompt('deseja parar?','sim')
}

