from django.contrib import admin
from .models import fuser
# Register your models here.


class FcuserAdmin(admin.ModelAdmin):
    list_display = ["username","password"] #사용자이름, 비밀번호가 나오도록 설정 

admin.site.register(fuser,FcuserAdmin) 
