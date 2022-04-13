def tokenize(string):
    string = string.replace('(', ' ( ')
    string = string.replace(')', ' ) ')
    return string.split()


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def hasmore_substrings(string):
    for token in string:
        if token == '(':
            return True
    return False


def isleft_substring(string):
    if string[1] == '(':
        return True
    return False


def isright_substring(string):
    if string[-1:] == [')']:
        return True
    return False


def getleft_substring(string):
    conta = 0
    substring = []
    start_index = 100000
    for index, token in enumerate(string):
        if token == '(':
            conta = conta + 1
            if index < start_index:
                start_index = index
        if token == ')':
            conta = conta - 1
            if conta == 0:
                substring = string[start_index + 1:index]
                break

    return substring


def getright_substring(string):
    string_copy = string[::-1]
    conta = 0
    start_index = 100000
    substring = []
    for index, token in enumerate(string_copy):
        if token == ')':
            conta = conta + 1
            if index < start_index:
                start_index = index
        if token == '(':
            conta = conta - 1
            if conta == 0:
                temp = string_copy[start_index + 1:index]
                substring = temp[::-1]
                break

    return substring


def criar_tuplo(string):
    lista_tuplo = []
    condition = hasmore_substrings(string)
    if not condition:
        for token in string:
            if is_int(token):
                lista_tuplo.append(int(token))
            elif is_float(token):
                lista_tuplo.append(float(token))
            else:
                lista_tuplo.append(token)
    else:
        lista_tuplo.append(string[0])
        if isleft_substring(string):
            lista_tuplo.append(criar_tuplo(getleft_substring(string)))
        if not isleft_substring(string):
            if is_int(string[1]):
                lista_tuplo.append(int(string[1]))
            elif is_float(string[1]):
                lista_tuplo.append(float(string[1]))
            else:
                lista_tuplo.append(string[1])
        if isright_substring(string):
            lista_tuplo.append(criar_tuplo(getright_substring(string)))
        if not isright_substring(string):
            if is_int(string[-1]):
                lista_tuplo.append(int(string[-1]))
            elif is_float(string[1]):
                lista_tuplo.append(float(string[1]))
            else:
                lista_tuplo.append(string[-1])

    tuplo = tuple(lista_tuplo)
    return tuplo


def parse(lista_palavras):
    conta = 0
    start_index = 100000
    lista_tuplos = []
    for index, token in enumerate(lista_palavras):
        if token == '(':
            conta = conta + 1
            if index < start_index:
                start_index = index
        if token == ')':
            conta = conta - 1
            if conta == 0:
                lista_tuplos.append(criar_tuplo(lista_palavras[start_index+1:index]))
                start_index = 100000

    return lista_tuplos


def single_replace(var, valor, tuplo):
    lista_aux = list(tuplo)
    for index, exp in enumerate(lista_aux):
        if isinstance(exp, tuple):
            lista_aux[index] = single_replace(var, valor, exp)
        elif exp == var:
            lista_aux[index] = valor

    return tuple(lista_aux)


def var_replace(lista_tuplos):
    for tuplo in lista_tuplos:
        if tuplo[0] == 'define':
            lista_tuplos = lista_tuplos[1:]
            if lista_tuplos==[]:
                return []
            lista_tuplos[-1] = (single_replace(tuplo[1], tuplo[2], lista_tuplos[-1]))
    return lista_tuplos


def calcula_valor(tuplo):
    lista_temp = list(tuplo)
    valor = 0
    if tuplo[0] == '+':
        if isinstance(tuplo[1], tuple):
            lista_temp[1] = calcula_valor(tuplo[1])
        if isinstance(tuplo[2], tuple):
            lista_temp[2] = calcula_valor(tuplo[2])

        valor = lista_temp[1] + lista_temp[2]

    elif tuplo[0] == '*':
        if isinstance(tuplo[1], tuple):
            lista_temp[1] = calcula_valor(tuplo[1])
        if isinstance(tuplo[2], tuple):
            lista_temp[2] = calcula_valor(tuplo[2])

        valor = lista_temp[1] * lista_temp[2]

    elif tuplo[0] == '-':
        if isinstance(tuplo[1], tuple):
            lista_temp[1] = calcula_valor(tuplo[1])
        if isinstance(tuplo[2], tuple):
            lista_temp[2] = calcula_valor(tuplo[2])

        valor = lista_temp[1] - lista_temp[2]

    elif tuplo[0] == '/':
        if isinstance(tuplo[1], tuple):
            lista_temp[1] = calcula_valor(tuplo[1])
        if isinstance(tuplo[2], tuple):
            lista_temp[2] = calcula_valor(tuplo[2])

        valor = lista_temp[1] / lista_temp[2]

    else:
        return "Error: Operator not recognised"
    return valor


def avalia(lista_tuplos):
    worked_list = var_replace(lista_tuplos)
    if worked_list==[]:
        return "void"
    return calcula_valor(worked_list[0])


def interpreta(string):
    lista_palavras = tokenize(string)
    lista_tuplos = parse(lista_palavras)
    return avalia(lista_tuplos)


def main():
    string = input('Introduza a expressao que pretende interpretar:')
    print(interpreta(string))


main()
