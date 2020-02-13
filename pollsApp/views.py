from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Questions, Choice

# Create your views here.

def index(request):
    latest = Questions.objects.order_by('-pub_date')[:5]
    context = {
        'latest': latest
    }
    return render(request, "pollsApp/index.html", context)

def details(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, "pollsApp/detail.html", {'question': question})

def results(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, "pollsApp/results.html", {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try :
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "pollsApp/detail.html", {
            'question': question,
            'error_message': "You didn't select a choice"
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
