class Movie():
    """ Classe de objetos Movie. Para instanciá-lo, importe o arquivo media.py e crie o objeto chamando media.Movie() """
    def __init__(self, titulo, elenco, genero, cartaz, link_youtube):
        self.titulo = titulo
        self.elenco = elenco
        self.genero = genero
        self.cartaz = cartaz
        self.link_youtube = link_youtube
