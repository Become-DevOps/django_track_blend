from django.urls import path 
from calori import views

app_name = "calori"

urlpatterns = [
    path('',views.FoodItems,name='food'),
    path('delete/<int:id>/',views.delete_consumed,name='delete')
]
