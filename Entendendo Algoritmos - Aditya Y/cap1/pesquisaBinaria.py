
def pesquisa_binária(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        if meio == item:
            return item
        if meio < item:
            baixo = meio
        if meio > item:
            alto = meio
        print("repetição")
    return None

listaNum = [1,2,3,4,5,6,7,8,9,10]
print(pesquisa_binária(listaNum, 1))


