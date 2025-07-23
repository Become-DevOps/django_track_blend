from django.shortcuts import render,redirect
from expense.forms import ExpenseForm
from expense.models import Expense
from django.db.models import Sum
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense:expense')
    form = ExpenseForm()
    return render(request,"expense/add_expense.html",{'form':form})

@login_required(login_url='login')
def expense_list(request):
    all_expense = Expense.objects.all()
    total_expenses = all_expense.aggregate(Sum('amount'))
    
    # calculating for 365 days
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    data = Expense.objects.filter(date__gt=last_year)
    yearly_sum = data.aggregate(Sum('amount'))
    print(yearly_sum)
    
    # calculating for month
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gt=last_month)
    monthly_sum = data.aggregate(Sum('amount'))
    print(monthly_sum)
    
    # calculating for a week
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data = Expense.objects.filter(date__gt=last_week)
    weekely_sum = data.aggregate(Sum('amount'))
    print(weekely_sum)
    
    # calculating dialy sums
    daily_sum = Expense.objects.filter().values('date').order_by('date').annotate(sum=Sum('amount'))
    print(daily_sum)
    
    # calculating catogery sum
    catogery_sum = Expense.objects.filter().values('catogery').order_by('catogery').annotate(sum=Sum('amount'))
    print(catogery_sum)
    
    print(total_expenses)
    context = {
        'all_expense':all_expense,
        'total_expenses':total_expenses,
        'yearly_sum':yearly_sum,
        'monthly_sum':monthly_sum,
        'weekely_sum':weekely_sum,
        'daily_sum': daily_sum,
        'catogery_sum': catogery_sum,
    }
    return render(request,"expense/expense_list.html",context)

@login_required(login_url='login')
def edit_expense(request,id):
    item = Expense.objects.get(id=id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('expense:expense')
    else:
        form = ExpenseForm(instance=item)
    context = {
        'form':form
    }
    return render(request,"expense/edit_expense.html",context)

@login_required(login_url='login')
def delete_expense(request,id):
    item = Expense.objects.get(id=id)
    item.delete()
    return redirect('expense:expense')