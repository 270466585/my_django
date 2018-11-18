from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#创建第一个视图
def index(request):
    return HttpResponse("hello ,world .you're at the polls index" )