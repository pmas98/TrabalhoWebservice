from rest_framework import generics
from .models import Task
from .serializers import ToDoItemSerializer
from rest_framework.response import Response
from rest_framework import status  

class CreateTaskView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = ToDoItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetAllItemsView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = ToDoItemSerializer

class GetSingleItemView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = ToDoItemSerializer

class UpdateTaskView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = ToDoItemSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class DeleteTaskView(generics.DestroyAPIView):
    queryset = Task.objects.all()