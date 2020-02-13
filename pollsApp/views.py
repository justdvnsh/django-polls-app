from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Questions

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
    return HttpResponse("Hey there ... You are looking at the results of the %s question number."%question_id)

def vote(request, question_id):
    return HttpResponse("Hey There ... You are at the voting page. Your uestions has %s votes"%question_id)
