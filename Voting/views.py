from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.
arr = ['Java', 'Python', 'Cplusplus', 'C', 'DotNET', 'JavaScript', 'PHP', 'Swift', 'SQL', 'Ruby', 'Delphi',
       'Objective-C', 'Go', 'Assemblylanguage', 'VisualBasic', 'D', 'R', 'Perl', 'MATLAB']
globalcnt = dict()


# Create your views here.
def index(request):
    return render(request, 'indexvote.html')


def getquery(request):
    q = request.GET['languages']
    if q in globalcnt:
        # if already exist then increment the value
        globalcnt[q] = globalcnt[q] + 1
    else:
        # first occurrence
        globalcnt[q] = 1
    mydictionary = {
        "arr": arr,
        "globalcnt": globalcnt
    }
    return render(request, 'indexvote.html', context=mydictionary)


def sortdata(request):
    global globalcnt
    globalcnt = dict(sorted(globalcnt.items(), key=lambda x: x[1], reverse=True))
    mydictionary = {
        "arr": arr,
        "globalcnt": globalcnt
    }
    return render(request, 'indexvote.html', context=mydictionary)
