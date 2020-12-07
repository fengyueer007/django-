from django.shortcuts import render
from django.http import HttpResponse

from users.models import User
# Create your views here.

def register(request):
    # 注册页面内容

    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        User.objects.create(username=username,password=password)

        print(f'username:{username}, password:{password}')
        return HttpResponse('成功')