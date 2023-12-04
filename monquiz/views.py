from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.template import RequestContext

from .forms import createuserform, AjoutQuestionForm, AjoutQuizForm, AjoutReponseForm
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from questions.models import Question
from resultats.models import Resultat
from questions.models import Reponse


class QuizListView(ListView):
    model = Quiz
    template_name = 'monquiz/listes_des_quiz.html'
    

def home(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'monquiz/monquiz.html', {"objets": quiz})

def donnees_quiz(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.obtenir_questions():
        reponses = []
        for a in q.obtenir_reponses():
            reponses.append(a.texte)
        questions.append({str(q): reponses})
    return JsonResponse({
        "donnees": questions,
        "temps": quiz.temps,
    })

def sauvegarder_donnees(request, pk):
    #print(request.POST)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        questions = []
        donnees = request.POST
        donnees_ = dict(donnees.lists())
        donnees_.pop('csrfmiddlewaretoken')
        for k in donnees_.keys():
            question = Question.objects.get(texte=k)
            questions.append(question)
        utilisateur = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.nombre_de_questions
        resultats = []
        reponses_correctes = None

        for q in questions:
            reponse_selectionnee = request.POST.get(q.texte)
            if reponse_selectionnee != "":
                reponses_question = Reponse.objects.filter(question=q)
                for a in reponses_question:
                    if reponse_selectionnee == a.texte:
                        if a.correct:
                            score += 1
                            reponse_correcte = a.texte
                    else:
                        if a.correct:
                            reponse_correcte = a.texte
                resultats.append({str(q): {'reponse_correcte': reponse_correcte, 'repondue': reponse_selectionnee}})
            else:
                resultats.append({str(q): 'pas de reponse'})
        score_ = score * multiplier
        Resultat.objects.create(quiz=quiz, utilisateur=utilisateur, score=score_)

        if score_ >= quiz.score_requi_pour_passer:
            return JsonResponse({'passe': True, 'score': score_, 'resultats': resultats})
        else:
            return JsonResponse({'passe': False, 'score': score_, 'resultats': resultats})

def ajoutquestion(request):
    if request.user.is_staff:
        form = AjoutQuestionForm()
        if (request.method == 'POST'):
            form = AjoutQuestionForm(request.POST)
            if (form.is_valid()):
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'monquiz/AjouterQuestions.html', context)
    else:
        return redirect('home')
def ajoutquiz(request):
    if request.user.is_staff:
        form = AjoutQuizForm()
        if (request.method == 'POST'):
            form = AjoutQuizForm(request.POST)
            if (form.is_valid()):
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'monquiz/AjouterQuestions.html', context)
    else:
        return redirect('home')

def ajoutreponse(request):
    if request.user.is_staff:
        form = AjoutReponseForm()
        if (request.method == 'POST'):
            form = AjoutReponseForm(request.POST)
            if (form.is_valid()):
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'monquiz/AjouterQuestions.html', context)
    else:
        return redirect('home')
    
"""
def deconnexion(request):
    logout(request)
    return redirect('/')
"""