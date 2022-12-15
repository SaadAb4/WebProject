from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from coursework3.models import User

def index(request):
    return HttpResponse('hello world')

def user_api(request:HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return JsonResponse({
            'User': [
                User.to_dict()
                for user in User.objects.all()
            ]
        })
    if request.method == 'POST':
        data = request.body
        data = json.loads(data.decode("utf-8"))
        user = User.objects.create(
            email = data['email'], 
            password= data['password'], 
            #date_of_birth = data['date_of_birth'], 
        )
        return JsonResponse(user.to_dict())