def make_album(artista, títuloAlbum, NroCanciones=None):
    """Return a dictionary of information about a person."""
    Album = {'Nombre': artista, 'Titulo Album': títuloAlbum}
    return Album

while True:
    print("Escriba quit si desea salir")
    f_artista = input("\nIngrese un Artista: ")

    if f_artista =='quit':
        break
        
    f_títuloAlbum = input("\nIngrese el Titulo de un Album: ")
    if f_títuloAlbum == 'quit':
        break
       
    album_completed = make_album(f_artista, f_títuloAlbum)
    print(f"El Album es: {album_completed}")


