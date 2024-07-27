from django.contrib import admin
from .models import Question,Quiz,Answer



class QuizAdmin(admin.ModelAdmin):
    list_display=["id","title"]

admin.site.register(Quiz,QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)

# Register your models here.
