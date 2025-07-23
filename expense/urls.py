from django.urls import path 
from expense import views 

app_name = "expense"

urlpatterns = [
    path('',views.add_expense,name='add'),
    path('expense',views.expense_list,name='expense'),
    path('edit/<int:id>/',views.edit_expense,name='edit'),
    path('delete/<int:id>/',views.delete_expense,name='delete')
    
]
