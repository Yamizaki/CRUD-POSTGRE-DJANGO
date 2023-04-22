from django.urls import path
from . import views 

urlpatterns = [
    path("", views.lista_tareas),
    path('new/', views.create_task, name="create_task"),
    path('delete_task/<int:task_id>/', views.delete_task, name="delete_task"),
    path('done_task/<int:task_id>/', views.done_task, name="done_task")
]