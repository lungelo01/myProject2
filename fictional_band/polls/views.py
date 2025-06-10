from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice
from django.urls import reverse
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


# Create your views here.
"""index view

"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "index.html", context)


"""detail view

"""
@login_required
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question':question})

"""vote view

"""
def vote(request):
    question = get_object_or_404(Question)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice']
        )

    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(
            reverse('polls:results')
        )

"""register view

"""
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('polls:index')  # Redirect to the polls index page
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})
