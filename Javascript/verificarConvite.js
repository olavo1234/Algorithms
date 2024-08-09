const listaConvidados = new Array(

)

const pessoaQueConvida = ''

function modificarStatus(status){
    let resultado = document.getElementById("verificacao")
    resultado.textContent = status
}
modificarStatus("Pesquisando...")


function gravarValores(){
    let aceito = 0
    // vai quardar o valor do primeiro campo
    let nomeDoUsuario = document.getElementById("nomeConvidado").value.trim()
    
    // vai quardar o valor do segundo campo
    let NomeConvidou = document.getElementById("quemConvidou").value.trim()

    if (NomeConvidou === pessoaQueConvida){
        for (nome of listaConvidados){
            if (nome === nomeDoUsuario){
                modificarStatus("Entrada confirmada")
                return
            }else {
                modificarStatus("Entrada revogada")
            }
        }
    } 
}

document.getElementById("recarregar").addEventListener("click", function(){
    location.reload()
})


document.getElementById("nomeConvidado").value = "";
document.getElementById("quemConvidou").value = "";