class ComentarSite{
    constructor(){
        this.verComentarios = []
    }
    
    setAutor(nomeAutor){
        this.verComentarios.push(nomeAutor)
    }

    setComentario(novoComentario){
        this.verComentarios.push(novoComentario)
    }
}



class Postagem{
    constructor(titulo,mensagem,autor,visulizacoes){;
        this.titulo = titulo;
        this.mensagem = mensagem;
        this.autor = autor;
        this.visualizacoes = visulizacoes;
        // composição
        this.comentario = new ComentarSite()
    }

    estaAoVivo(valorLogigo){
        switch (valorLogigo){
            case true:
            console.log('Está ao vivo');
            break;

            case false:
            console.log('Não está ao vivo');
            break;

            default:
                console.log('não está ao vivo');
                break;
        }
    }
}




const site = new Postagem('melhor anime','steins;gate é bom','olavo',1);

site.estaAoVivo(false);
console.log(site.autor);
console.log(site.visualizacoes)
site.comentario.setAutor('vanderley')
site.comentario.setComentario('esse steins;gate é bom memo')
site.comentario.setAutor('joão')
site.comentario.setComentario('voce tem bom gosto!')
console.log(site.comentario.verComentarios)
