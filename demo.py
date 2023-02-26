def make_album(nom_artista,titulo,numero=None):
    album ={'nombre':nom_artista,'titulo':titulo}
    if numero:
        album[numero]=numero
    return  album


make_album('juanes','la camisa negra',5)