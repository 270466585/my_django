from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Question
from django.shortcuts import render,get_object_or_404

# Create your views here.

#创建第一个视图
# def index(request):
#     return HttpResponse("hello ,world .you're at the polls index" )

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    template=loader.get_template('myAPP/index.html')
    context={
        'latest_question_list':latest_question_list,
    }
    #return HttpResponse(template.render(context,request))
    return render(request,'myAPP/index.html',context)

def detail(request,question_id):
    #return HttpResponse("You'er looking at question %s."%question_id)
    latest_question_list=get_object_or_404(Question,pk=question_id)
    return render(request,'myAPP/index.html',{'latest_question_list':latest_question_list})

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