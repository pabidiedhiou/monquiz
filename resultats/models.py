from django.conf import UserSettingsHolder
from Quiz.settings import AUTH_USER_MODEL
from django.db import models
from django.contrib.auth.models import User

from monquiz.models import Quiz
class Resultat(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.FloatField()
    def __str__(self) :
        return str(self.pk)
