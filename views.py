from django.shortcuts import render
from .models import fuser
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

def register(request):
    #두가지 경우
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == 'POST':   
        #username = request.POST.get('username',None)
        #password = request.POST.get('password',None)
        #re_password = request.get('re-password',None)
        
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re-password']
        
        res_data = {}

        if not (username and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다.'
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else: 
            Fuser = fuser(
             username=username, 
             password=make_password(password)
         )

            #저장
            Fuser.save()

        return render(request, 'register.html', res_data)