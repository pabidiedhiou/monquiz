from django.contrib import admin
from django.urls import path
from .import views
app_name = 'monquiz'
urlpatterns = [
    path('', views.QuizListView.as_view(), name="quizlistview"),
    path('ajoutquestion/', views.ajoutquestion, name='ajoutquestion'),
    path('ajoutquiz/', views.ajoutquiz, name='ajoutquiz'),
    path('ajoutreponse/', views.ajoutreponse, name='ajoutreponse'),
    path('<pk>/', views.home, name='home'),
    path('<pk>/sauvegarder', views.sauvegarder_donnees, name='sauvegarder_donnees'),
    path('<pk>/donnees', views.donnees_quiz, name='donnees-quiz'),
]
