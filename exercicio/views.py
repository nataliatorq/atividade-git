from django.shortcuts import render


def natalia_view(request):
    nome = 'Natalia Torquato'

    return render(request, 'exercicio/natalia.html',
                  context={
                      'nome': nome
                  }
                  )
