from django.shortcuts import render, redirect
from django.http import JsonResponse
from app.models import Aluno, Ficha_fisica

# Create your views here.


def api(request, pk, param):
    aluno = list(Ficha_fisica.objects.filter(aluno_id=pk).values(param, 'created_at').order_by('-created_at'))[:5]
    
    data = (request.GET or None)
    if data:
        print(f'Get: {data}')
        field = Ficha_fisica.objects.filter(aluno_id=pk).values(data, 'created_at').order_by('-created_at')[:5]
        return JsonResponse(aluno, safe=False)

    print(f'Dados do Aluno: {aluno}')
    return JsonResponse(aluno, safe=False)