from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    return render(request, "indexcalc.html")


def submitquery(request):
    q = request.GET['query']
    try:
        ans = eval(q)
        mydictionary = {
            'q': q,
            'ans': ans,
            'error': False,
            'result': True,
        }
        return render(request, 'indexcalc.html', context=mydictionary)
    except:
        mydictionary = {
            'error': True,
            'result': True,
        }
        return render(request, 'indexcalc.html', context=mydictionary)
