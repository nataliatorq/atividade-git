from django.shortcuts import render


def natalia_view(request):
    nome = 'Natalia Torquato'

    return render(request, 'exercicio/natalia.html',
                  context={
                      'nome': nome
                  }
                  )

def mikarlla_view(request):
    nome = 'Mikarlla Souza'

    return render(request, 'exercicio/mikarlla.html',
                  context={
                      'nome': nome
                  }
                  )
