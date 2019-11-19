from django.shortcuts import render

# Create your views here.
def mostar_home(request):
    nome = 'Groger'
    idade = 17
    lista_roupas = {
        'Bone da lacroste',
        'Bone da Nike'
        'Cinto do Batiman'
        'toca de meduza'
        'Oculos'
    }

    context = {
        'roupas': lista_roupas,
        'nome': nome,
        'idade': idade
    }    

    
    return render(request,'index.html', context)