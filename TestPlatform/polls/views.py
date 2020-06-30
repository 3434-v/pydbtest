from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from polls.models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic

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