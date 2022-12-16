from typing import ItemsView
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import json
from coursework3.models import User, Items


def index(request):
    return HttpResponse('success')

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, ("error"))

    else:
        return render(request, 'authentication/login.html')

@csrf_exempt
def user_api(request:HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return JsonResponse (json.dump({
            'User': [
                user.to_dict()
                for user in User.objects.all()
            ]
        }))

    if request.method == 'POST':
        data = request.body
        data = json.loads(data.decode("utf-8"))
        user = User.objects.create(
            email = data['email'], 
            password= data['password'], 
            #date_of_birth = data['date_of_birth'], 
        )
        return JsonResponse(user.to_dict())

def items_api(request:HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return JsonResponse({
            'items': [
                items.to_dict()

                for items in Items.objects.all()
            ]
        })
    if request.method == 'POST':
        data = request.body
        data = json.loads(data.decode("utf-8"))
        items = Items.objects.create(
            title = data['title'],
            description = data['description'],
            startingPrice = data['startingPrice'],
            auctionEnd = data['auctionEnd'],
            item_pic = data['auctionEnd'],
        )
        return JsonResponse(ItemsView.to_dict())