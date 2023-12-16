from django.shortcuts import render, redirect
from .models import UserModel, Order
from datetime import datetime
from .forms import AddMen

def index(request):
    people = UserModel.objects.order_by('-id')
    chel = UserModel.objects.count()
    return render(request, 'posts.html', context={'people': people, 'chel': chel})


def create(request):
    if request.method == 'POST':
        form = AddMen(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            UserModel.objects.create(name=name, age=age)
            return redirect('home')

    form = AddMen()
    return render(request, 'create.html', context={'form': form})


def update(request, id):
    try:
        men = UserModel.objects.get(id=id)
        if request.method == 'POST':
            men.name = request.POST.get('name')
            men.age = request.POST.get('age')
            men.save()
            return redirect('home')
        else:
            return render(request, 'update.html', context={'men': men})
    except:
        return redirect('create')


def delete(request, id):
    try:
        men = UserModel.objects.get(id=id)
        men.delete()
        return redirect('home')
    except:
        return redirect('home')

def user(request, id):
    try:
        men = UserModel.objects.get(id=id)
        return render(request, 'user.html', context={'user':user})
    except:
        return redirect('home')



def order(request):
    createOrders()
    orders = Order.objects.filter(datetime__month__gte=6)
    return render(request, 'orders.html', context={'orders': orders})


def createOrders():
    if Order.objects.count() < 5:
        Order.objects.create(datetime=datetime(2020, 3, 30, 15, 55, 40))
        Order.objects.create(datetime=datetime(2023, 4, 27, 12, 55, 40))
        Order.objects.create(datetime=datetime(2019, 12, 23, 4, 55, 40))
        Order.objects.create(datetime=datetime(2007, 11, 12, 8, 55, 40))
        Order.objects.create(datetime=datetime(2090, 5, 1, 18, 55, 40))