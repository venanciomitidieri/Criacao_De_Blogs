from django.http import HttpResponse


def hello(request):
    return HttpResponse("Olá, mundo!")


def articles(request, year):
    return HttpResponse('O ano enviado foi: ' + str(year))


def lerbanco(nome):
    lista_nomes = [
        {'nome': 'Ana', 'idade': 27},
        {'nome': 'Pedro', 'idade': 15},
        {'nome': 'Venancio', 'idade': 20}
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome': 'Não encontrado', 'idade': 0}


def fname(request, nome):
    result = lerbanco(nome)
    if result['idade'] > 0:
        return HttpResponse('A pessoa foi encontrada, ela tem ' + str(result['idade']) + 'anos')
    else:
        return HttpResponse('Pessoa não encontrada')



