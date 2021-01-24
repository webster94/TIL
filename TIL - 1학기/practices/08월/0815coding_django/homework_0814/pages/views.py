from django.shortcuts import render
import random
# Create your views here.
def ssafy(request):
    menus = ['피자', '짬뽕', '홍어']
    posts = range(0,10)
    users = []
    context = {
        'menus' : menus,
        'posts' : posts,
        'users' : users
    }
    return render(request,'ssafy.html', context)

def create(request):
    message = request.GET.get('title')
    message1 = request.GET.get('content')
    message2 = request.GET.get('my-site')

    context = {
        'message' : message,
        'message1' : message1,
        'message2' : message2,
    }
    return render(request, 'create.html', context)