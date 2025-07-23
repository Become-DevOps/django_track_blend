from django.shortcuts import render,redirect
from calori.models import Food
from calori.models import Consume
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def FoodItems(request):
    if request.method == 'POST':
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user,food_consumed=consume)
        consume.save()
    food = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    context = {
        'food':food,
        'consumed_food': consumed_food
    }
    return render(request,"calories/fooditems.html",context)

@login_required(login_url='login')
def delete_consumed(request,id):
    consumed_food = Consume.objects.get(id=id)
    consumed_food.delete()
    return redirect('calori:food')