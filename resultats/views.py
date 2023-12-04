from django.shortcuts import render

def resultats(request):
    return render(request, 'resultats/resultats.html')
