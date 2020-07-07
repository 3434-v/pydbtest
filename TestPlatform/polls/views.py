from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# Create your views here.
from polls.models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic
import json, requests
import polls.inform



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DeleteView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def home(request):
    return HttpResponse("python-django 3.0")


# def detail(request, question_id):
#     return HttpResponse("detailmessage:{}".format(question_id))

def results(request, question_id):
    print('-------------')
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You dint't select a choice.",
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def indextest(request):
    latest_choice_list = Choice.objects.order_by('-votes')[:5]
    print(latest_choice_list)
    context = {'latest_choice_list': latest_choice_list}
    return render(request, 'polls/indextest.html', context)


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


# 请求内容格式转换函数
def bytes_switch_dict(msg: bytes) -> dict:

    msg_str = str(msg, encoding='utf-8')
    # print(msg_str)
    msg_list = []
    msg_dict = {}
    count = 0
    for index in range(len(msg_str)):
        if msg_str[index] == '&':
            msg_list.append(msg_str[count: index])
            count = index + 1
    msg_list.append(msg_str[count:])
    # print(msg_list)
    dict_count = 0
    for list_index in msg_list:
        for index in range(len(list_index)):
            if list_index[index] == '=':
                array = list_index[dict_count: index]
                msg_dict[array] = list_index[index+1:]
    print(msg_dict)
    return msg_dict


def readim(request):
    if request.method == "POST":
        request_data_dict = bytes_switch_dict(request.body)
        if request_data_dict['type'] == '1':
            returndata = polls.inform.WX_robot(request_data_dict['msg'])
            return JsonResponse({"status": "WX_robot", "msg": returndata})
        elif request_data_dict['type'] == '2':
            returndata = polls.inform.DD_robot(request_data_dict['msg'])
            return JsonResponse({"status": "DD_robot", "msg": returndata})
        else:
            return JsonResponse({"status": "-1", "msg": "不支持的请求类型"})
    elif request.method == "GET":
        return JsonResponse({"status": "-1", "msg": "暂不支持GET请求"})


