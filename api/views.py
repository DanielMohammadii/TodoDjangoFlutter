from rest_framework import generics
from .models import Todo
from .serializers import *


# Crud Operations
class ListTodo(generics.ListAPIView):  # Read
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateAPIView):  # Update
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CreateTodo(generics.CreateAPIView):  # Create
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DeleteTodo(generics.DestroyAPIView):  # Delete
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
