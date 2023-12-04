from django.forms import ModelForm

from questions.models import Question, Reponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class createuserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class AjoutQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"


class AjoutQuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = "__all__"


class AjoutReponseForm(ModelForm):
    class Meta:
        model = Reponse
        fields = "__all__"