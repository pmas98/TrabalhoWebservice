from django.urls import path
from .views import (
    CreateTaskView,
    GetAllItemsView,
    GetSingleItemView,
    UpdateTaskView,
    DeleteTaskView
)

urlpatterns = [
    path('tasks/create', CreateTaskView.as_view(), name='create-task'),
    path('tasks/', GetAllItemsView.as_view(), name='get-all-items'),
    path('tasks/<int:pk>/', GetSingleItemView.as_view(), name='get-single-item'),
    path('tasks/<int:pk>/update/', UpdateTaskView.as_view(), name='update-task'),
    path('tasks/<int:pk>/delete/', DeleteTaskView.as_view(), name='delete-task'),
]
