class CriarPostagem{
    constructor(titulo,autor,mensagem){    
        this.titulo = titulo
        this.autor = autor
        this.mensagem = mensagem
        this.visualizacao = 0
        this.aoVivo = false
        this.comentarios = []
    }


    ficarAoVivo(){
        this.aoVivo = true
    }


    getComentario(){
        for(let msg in this.comentarios){
            console.log(this.comentarios[msg])
    }
}

    visualizar(){
        this.visualizacao += 1
    }

    setComentario(comentario){
        this.comentarios.push(comentario)
    }
}

const meuSite = new CriarPostagem('top linquagens','olavo','javascripto',12000)
meuSite.visualizar()
meuSite.visualizar()
meuSite.setComentario('prefiro mais csharpo')
meuSite.setComentario('ea galero do typescripto')
meuSite.getComentario()
console.log(meuSite.visualizacao)
meuSite.ficarAoVivo()
console.log(meuSite.aoVivo)
