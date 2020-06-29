from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# from polls.models import Question
from polls.models import Question

def home(request):
    return HttpResponse("python-django 3.0")

def detail(request, question_id):
    return HttpResponse("detailmessage:{}".format(question_id))

def results(request, question_id):
    print('-------------')
    response = "resultsmessage {}"
    return HttpResponse(response.format(question_id))

def vote(request, question_id):
    return HttpResponse("votemessage:{}".format(question_id))

def index(request):
    question_list = Question.objects.all()
    print('-------------')
    print(question_list)
    print('-------------')
    output = ', '.join([q.question_text for q in question_list])
    return HttpResponse(output)
