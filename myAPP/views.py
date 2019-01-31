from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Question
from django.shortcuts import render,get_object_or_404
from django.db import models
from myAPP import models

# Create your views here.

#创建第一个视图
# def index(request):
#     return HttpResponse("hello ,world .you're at the polls index" )

# def index(request):
#     latest_question_list=Question.objects.order_by('-pub_date')[:5]
#     template=loader.get_template('myAPP/index232.html')
#     context={
#         'latest_question_list':latest_question_list,
#     }
#     #return HttpResponse(template.render(context,request))
#     return render(request,'myAPP/index232.html',context)

def detail(request,question_id):
    #return HttpResponse("You'er looking at question %s."%question_id)
    latest_question_list=get_object_or_404(Question,pk=question_id)
    return render(request, 'myAPP/index232.html', {'latest_question_list':latest_question_list})

def results(request,question_id):
    response="You're looking at the results of question %s."
    return HttpResponse(response%question_id)

def vote(request,question_id):
    return HttpResponse("Youe're voting on question %s."%question_id)

def createUser(request,username):
    return HttpResponse("Create a user with the account name:%s"%username)

def detail_test(request,question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request,'myAPP/detail.html',{'question':question})

def detail_tests(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'myAPP/detail.html',{'question':question})

def index123(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        models.Usertable.objects.create(name=name,age=age)

    user_list=models.Usertable.objects.all()
    print(user_list)
    return render(request, 'myAPP/index.html', {'data':user_list})

from Public_methods.mysql_tools import MysqlUtil
code_list=[]
def getCode(request):
    code_list.clear()
    if request.method=='POST':
        number=request.POST.get('number')
        print(number)
        A = MysqlUtil()
        temp={'code':A.mysql_getVerify(number)}
        code_list.append(temp)
    return render(request,'myAPP/user_query.html',{'user_code':code_list})

token_list=[]
def getToken(request):
    token_list.clear()
    if request.method=='POST':
        number=request.POST.get('number')
        A = MysqlUtil()
        data=A.mysql_getToken(number)
        temp={'userid':data[0],
              'user_token':data[1],
              'device_info':data[2]}
        token_list.append(temp)
    return render(request,'myAPP/user_query.html',{'user_token':token_list})


def createUrl(request):
    if request.method=='POST':
        name=request.POST.get('name')
        type=request.POST.get('type')
        formal=request.POST.get('formal')
        test=request.POST.get('test')
        models.CreateUrl.objects.create(Product_name=name,type=type,formal=formal,test=test)
    usrl_list = models.CreateUrl.objects.all()
    return render(request, 'myAPP/link_set.html', {'all_url': usrl_list})

def index(request):
    return render(request,'myAPP/index.html')
