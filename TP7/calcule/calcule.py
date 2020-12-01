def convertion(nbRome):

    if nbRome == 'I':
        return 1
    elif nbRome == 'V':
        return 5
    elif nbRome == 'X':
        return 10
    elif nbRome == 'L':
        return 50
    elif nbRome == 'C':
        return 100
    elif nbRome == 'D':
        return 500
    elif nbRome == 'M':
        return 1000
    else:
        return "erreur, la lettre n'est pas reconnue"


def convertionSomme(nbRome):

    somme = 0
    dernierChiffre = 0
    for i in nbRome:

        if dernierChiffre < convertion(i):
            somme = somme + convertion(i) - (2*dernierChiffre)

        else:
            somme = somme + convertion(i)

        dernierChiffre = convertion(i)

    return somme


def calculatrice(operation, nbRome1, nbRome2):

    nombre1 = convertionSomme(nbRome1)
    nombre2 = convertionSomme(nbRome2)

    if operation == '+':
        return nombre1 + nombre2
    elif operation == '-':
        return nombre1 - nombre2
    elif operation == '*':
        return nombre1 * nombre2
    elif operation == '/':
        return nombre1 // nombre2


def tradRomain(operation, nbRome1, nbRome2):

    nombre = calculatrice(operation, nbRome1, nbRome2)
    nombreEnRomain = ''
    mille = nombre // 1000
    nombre = nombre - (mille * 1000)
    cent = nombre // 100
    nombre = nombre - (cent * 100)
    dix = nombre // 10
    nombre = nombre - (dix * 10)
    unite = nombre


    for i in range(0,mille):
        nombreEnRomain = nombreEnRomain + 'M'
        i += 1

    if cent >= 5:
        nombreEnRomain = nombreEnRomain + 'D'
        cent = cent - 5
    elif unite == 9:
        nombreEnRomain = nombreEnRomain + 'CDD'

    if cent == 4:
        nombreEnRomain = nombreEnRomain + 'CD'
    elif cent > 0 and cent < 4:
        for i in range(0,cent):
            nombreEnRomain = nombreEnRomain + 'C'
            i += 1


    if dix >= 5:
        nombreEnRomain = nombreEnRomain + 'L'
        dix = dix - 5
    elif cent == 9:
        nombreEnRomain = nombreEnRomain + 'XLL'

    if dix == 4:
        nombreEnRomain = nombreEnRomain + 'XL'
    elif dix > 0 and dix < 4:
        for i in range(0,dix):
            nombreEnRomain = nombreEnRomain + 'C'
            i += 1


    if unite >= 5 and unite !=9:
        nombreEnRomain = nombreEnRomain + 'V'
        unite = unite - 5
    elif unite == 9:
        nombreEnRomain = nombreEnRomain + 'IVV'

    if unite == 4:
        nombreEnRomain = nombreEnRomain + 'IV'
    elif unite > 0 and unite < 4:
        for i in range(0,unite):
            nombreEnRomain = nombreEnRomain + 'I'
            i += 1


    return nombreEnRomain
