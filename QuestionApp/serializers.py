from rest_framework import serializers
from QuestionApp.models import Question, Choice
from django.contrib.auth.models import User


class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'subject','owner']

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id','choice_text',"question",'votes']

class UserSerializer(serializers.ModelSerializer):
    questions=serializers.PrimaryKeyRelatedField(many=True,queryset=Question.objects.all())
    class Meta:
        model=User
        fields=['id','username','questions']

