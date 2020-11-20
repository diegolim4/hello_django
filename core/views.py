from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(request, num1, num2):
    return HttpResponse(f'A soma de {num1}+{num2} é {num1+num2} A subtração:{num1-num2}  A multiplicação: {num1*num2} '
                        f'A Divisão{num1/num2}')

