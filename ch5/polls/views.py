# 뷰 함수 정의
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from polls.models import Question, Choice
from django.views.generic import ListView, DetailView
import logging
logger = logging.getLogger(__name__)

class IndexView(ListView):
    template_name = "polls/index.html"
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultView(DetailView):
    model = Question
    template_name = 'polls/results.html'

# def index(request):
#     latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
#
# def detail(request, question_id):
#     #pk = question_id 검색조건에 맞는 객체가 없으면 404에러
#     #detail.html 텍스트 데이터를 담은 HttpResponse 객체를 반환
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question':question})


def vote(request, question_id):
    logger.debug("vote().question_id: %s" %question_id)
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question' : p,
            'error_message' : "You didn't select a choice.",
        })
    else :
        selected_choice.votes += 1
        selected_choice.save()
        #reverse() => url패턴으로부터 url스트링을 구할 수 있다
        return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})



