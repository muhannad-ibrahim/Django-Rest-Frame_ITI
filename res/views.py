from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Todo
from . serializers import TodoSerializer

# Create your views here.
@api_view(['GET'])
def home(request):
    urls=[
        'listTodo/',
        'detailTodo/<str:id>/',
        'createTodo/',
        'updateTodo/<str:id>/',
        'deleteTodo/<str:id>/',
    ]
    return Response(urls)

@api_view(['GET'])
def listTodo(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)
