from django.contrib import admin
from .models import Question, Reponse

class AnswerInline(admin.TabularInline):
    model = Reponse

    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_filter =('quiz',)
    
class ReponseAdmin(admin.ModelAdmin):
    list_filter =('question',)
    
admin.site.register(Question,QuestionAdmin)
admin.site.register(Reponse,ReponseAdmin)
