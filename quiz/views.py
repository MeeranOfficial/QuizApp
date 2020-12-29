from django.shortcuts import render
from django.http import HttpResponse
from .models import Quiz
from django.core.paginator import Paginator


user_answer_list = []
answers = Quiz.objects.all()

correct_ans_list = []
for i in answers:
    correct_ans_list.append(i.correct_answer)


def welcome(request):
    user_answer_list.clear()
    return render(request, 'welcome.html')


def quiz(request):
    obj = Quiz.objects.all()
    count = Quiz.objects.all().count()
    paginator = Paginator(obj, 1)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        questions = paginator.page(page)
    except(ValueError):  # EmptyPage, InvalidPage
        questions = paginator.page(paginator.num_pages)

    return render(request, 'quiz.html', {'obj': obj, 'questions': questions, 'count': count})


def result(request):
    score = 0
    for i in range(len(user_answer_list)):
        if user_answer_list[i] == correct_ans_list[i]:
            score += 1
    return render(request, 'result.html', {'score': score, 'user_answer_list': user_answer_list})


def save_ans(request):
    ans = request.GET['ans']
    user_answer_list.append(ans)


