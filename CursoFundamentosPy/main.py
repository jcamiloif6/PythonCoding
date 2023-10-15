# * -> Tupla
# ** -> Diccionario

def promedio(*args):
    return sum(args) / len(args)


def usuarios(**kwargs):
    print(kwargs)
    print(type(kwargs))


usuarios(cody='Cody', eduardo='eduardo_gpg')
