from django.db import models

from monquiz.models import Quiz
class Question(models.Model):
    texte = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    cree = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.texte)

    def obtenir_reponses(self):
        return self.reponse_set.all()
class Reponse(models.Model):
    texte = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    cree = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question}, reponse: {self.texte}, correct: {self.correct}"