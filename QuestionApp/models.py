import datetime
from django.utils import timezone

from django.db import models
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
#
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     subject=models.CharField(max_length=200)
#     def __str__(self):
#         return self.question_text
#     def __str__(self):
#         return self.subject
#     def was_published_recently(self):
#         return self.pub_date>=timezone.now()-datetime.timedelta(days=1)
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text

class Question(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    question_text= models.CharField(max_length=200, blank=True)
    subject=models.CharField(max_length=100,blank=True)
    class Meta:
        ordering = ['created']

class Choice(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200,blank=True,default='')

    class Meta:
        ordering = ['created']