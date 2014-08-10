# coding: utf-8
"""
#old 1

from django.http import HttpResponse
from django.template import loader, Context

def homepage(request):
    t = loader.get_template('index.html')
    c = Context()   
    
    content = t.render(c)

    return HttpResponse(content) 

"""

# REFATORAÇÃO 1
# REFATORAÇÃO 2 - IMPUTANDO VARIAVEIS NO CONTEXTO
# REFATORAÇÃO 3 - IMPORTANDO REQUESTCONTEXT PARA NÃO EXPLICITAR DICT CONTENDO VARIÁVEIS DE TEMPLATE
# REFATORAÇÃO 4 - IMPORTANDO RENDER - DRY ++  SHORCURTS (+ ENXUTO)
# coding: utf-8
from django.shortcuts import render


def homepage(request):
    return render(request, 'index.html')
 


