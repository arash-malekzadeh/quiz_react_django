from django.db import models
from django.utils.translation import gettext_lazy as _ 
from autoslug import AutoSlugField
# Create your models here.

class Quiz(models.Model):
    author=models.CharField(_("Author"), max_length=50)
    title=models.CharField(_("Quiz_title"), max_length=225 , unique=True, default=_("New Quiz"))
    created_at=models.DateTimeField(auto_now_add=True)

    @property

    def question_count(self):
        return self.questions.count()
    class Meta:
        verbose_name=_("quiz")
        verbose_name_plural=_("quizzes")
        ordering=['id']
class Question(models.Model):
    quiz=models.ForeignKey(Quiz,related_name="questions",on_delete=models.CASCADE,verbose_name="کوئیز")
    title=models.CharField(max_length=255,default='',verbose_name="متن سؤال")
    created_at=models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at=models.DateTimeField(auto_now=True, verbose_name="تاریخ به روزرسانی")

    class Meta:
        verbose_name=_("question")
        verbose_name_plural=_("questions")
        ordering=['id']
    def __str__(self):
        return self.title
    
class Answer(models.Model):
    question=models.ForeignKey(Question,related_name='answers',on_delete=models.CASCADE,verbose_name="کوئیز")
    answer_text=models.CharField(max_length=255,null=True,blank=True,verbose_name="متن سؤال")
    is_right=models.BooleanField(default=False,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at=models.DateTimeField(auto_now=True, verbose_name="تاریخ به روزرسانی")

    class Meta:
        verbose_name=_("answer")
        verbose_name_plural=_("answers")
        ordering=['id']
    def __str__(self):
        return self.title


