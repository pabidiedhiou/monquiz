from django.db import models
import random
DIFF_CHOICES = (
    ('facil', 'facil'),
    ('intermediaire', 'intermediaire'),
    ('difficil', 'difficil'),
)
class Quiz(models.Model):
    nom = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    nombre_de_questions = models.IntegerField()
    temps = models.IntegerField(help_text="durée du quiz en minutes")
    score_requi_pour_passer = models.IntegerField(help_text="Score en %")
    difficulte = models.CharField(max_length=13, choices=DIFF_CHOICES)
    def __str__(self):
        return f"{self.nom}-{self.topic}"
    def obtenir_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.nombre_de_questions]
    class Meta:
        verbose_name_plural = 'Quizes'