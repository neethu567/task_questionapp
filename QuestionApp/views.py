from rest_framework import serializers, status, permissions
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import BaseAuthentication
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views import generic
from rest_framework import generics
from QuestionApp.permissions import IsOwnerOrReadyOnly


from rest_framework import permissions

from QuestionApp.models import Question,Choice
from django.http import Http404

from QuestionApp.permissions import IsOwnerOrReadyOnly
from QuestionApp.serializers import QuestionSerializer, ChoiceSerializer, UserSerializer
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User

# from django.http import HttpResponse
#
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

# @api_view(['GET', 'POST'])
# def question_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         question = Question.objects.all()
#         serializer = QuestionSerializer(question, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = QuestionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class question_list(APIView):
#     def get(self,request,format=None):
#         question=Question.objects.all()
#         serializer=QuestionSerializer(question,many=True)
#         return Response(serializer.data)
#
#     def post(self,request,format=None):
#         serializer=QuestionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# class question_list(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Question.objects.all()
#     serializer_class =QuestionSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
class question_list(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadyOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)




# @api_view(['GET', 'PUT', 'DELETE'])
# def question_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         question = Question.objects.get(pk=pk)
#     except Question.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = QuestionSerializer(question)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = QuestionSerializer(question, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class question_detail(APIView):
#     def get_object(self,pk):
#         try:
#             return Question.objects.get(pk=pk)
#         except Question.DoesNotExist:
#             raise Http404
#
#     def get(self,request,pk,format=None):
#         question=self.get_object(pk)
#         serializer=QuestionSerializer(question)
#         return Response(serializer.data)
#
#     def put(self,request,pk,format=None):
#         question=self.get_object(pk)
#         serializer=QuestionSerializer(question,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk,format=None):
#         question=self.get_object(pk)
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class question_detail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


class question_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadyOnly]

    # authentication_classes = (BaseAuthentication)
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadyOnly]

# @api_view(['GET', 'POST'])
# def choice_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         choice = Choice.objects.all()
#         serializer =ChoiceSerializer(choice, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ChoiceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class choice_list(APIView):
#     def get(self,request,format=None):
#         choice=Choice.objects.all()
#         serializer=ChoiceSerializer(choice,many=True)
#         return Response(serializer.data)
#
#     def post(self,request,format=None):
#         serializer=ChoiceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# class choice_list(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Choice.objects.all()
#     serializer_class =ChoiceSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

class choice_list(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

# @api_view(['GET', 'PUT', 'DELETE','POST'])
# def choice_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#
#     try:
#         choice = Choice.objects.get(pk=pk)
#     except Choice.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ChoiceSerializer(choice)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ChoiceSerializer(choice, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         choice.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# class choice_detail(APIView):
#     def get_object(self,pk):
#         try:
#             return Choice.objects.get(pk=pk)
#         except Question.DoesNotExist:
#             raise Http404
#
#     def get(self,request,pk,format=None):
#         choice=self.get_object(pk)
#         serializer=ChoiceSerializer(choice)
#         return Response(serializer.data)
#
#     def put(self,request,pk,format=None):
#         choice=self.get_object(pk)
#         serializer=ChoiceSerializer(choice,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk,format=None):
#         choice=self.get_object(pk)
#         choice.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class choice_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

# @api_view(['PUT'])
# def vote(request, pk):
#     try:
#         choice = Choice.objects.get(pk=pk)
#     except Choice.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'PUT':
#         choice.votes+=1
#         choice.save()
#         msg = {"Votes" : choice.votes}
#         return Response(msg)

# class Vote(APIView):
#     def vote(self,request,pk,format=None):
#         try:
#             choice=Choice.objects.get(pk=pk)
#         except choice.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def put(self,request,pk,format=None):
#         choice = Choice.objects.get(pk=pk)
#         choice.votes+=1
#         choice.save()
#         msg={"votes":choice.votes}
#         return Response(msg)

# class Vote(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     generics.GenericAPIView):
#     queryset = Choice.objects.all()
#     serializer_class = ChoiceSerializer
#
#     def vote(self, request, pk, format=None):
#         try:
#             choice = Choice.objects.get(pk=pk)
#         except choice.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def put(self, request, *args, **kwargs):
#         choice = Choice.objects.get(pk=pk)
#         choice.votes+=1
#         choice.save()
#         msg={"votes":choice.votes}
#         return Response(msg)
#         return self.update(request, *args, **kwargs)
#
class user_list(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class user_detail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer