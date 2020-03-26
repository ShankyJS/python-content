def begin_play_list(lista):
    def reproduce():
        nonlocal lista
        lista = [1, 2, 3]
        for val in lista:
            print(val)
    reproduce()
    print(lista)


lista = ['track 1', 'track 2', 'track 3', 'track 4']
begin_play_list(lista)
