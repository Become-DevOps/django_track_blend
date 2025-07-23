from django.urls import path
from taskmanager import views

app_name = "taskmanager"

urlpatterns = [
    path('',views.index,name="task"),
    path('edit/<int:id>/',views.editTask,name='edit'),
    path('delete/<int:id>/',views.deletetask,name="delete")
]
