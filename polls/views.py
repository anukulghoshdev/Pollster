from django.template import loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice


# get questions and display them
def home(request):
    return render(request,'home.html')

def pollquestions(request, ):
    leatest_questions_list = Question.objects.order_by('-pub_date')[:6]
    context = {
        'leatest_questions_list': leatest_questions_list
    }
    return render(request, 'polls/pollquestions.html', context)




# show specific que and details

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)

    except Question.DoesNotExist:
        raise Http404("Question Does not exit")
    return render(request, 'polls/detail.html', {'question':question})


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/result.html',context)


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):

        return render(request, 'polls/detail.html', {
            "question": question,
            'error_message': "You didn't select a choice."
        })

    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))
