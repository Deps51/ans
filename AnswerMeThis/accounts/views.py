from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .forms import SignUpForm, AskQuestionForm
from .models import Question

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            print('logged in')
            return redirect('/../accounts/profile/')

    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form':form})



def profile(request):
    if request.user.is_authenticated():
        user = User.objects.get(username=request.user.username)
        question_objects = Question.objects.filter(author=user)
        questions = []
        for question in question_objects:
            _question = question.question
            Option1 = question.option1
            try:
                Option1_percentage = (question.option1_votes / question.no_of_votes) * 100
            except:
                Option1_percentage = 0
            Option2 = question.option2
            Option2_percentage = 100 - Option1_percentage
            No_of_votes = question.no_of_votes

            if No_of_votes == 0:
                state1 = 'minority'
                state2 = 'minority'
                Option2_percentage = 0
            elif Option1_percentage > Option2_percentage:
                state1 = 'majority'
                state2 = 'minority'
            elif Option1_percentage < Option2_percentage:
                state1 = 'minority'
                state2 = 'majority'
            else:
                state1 = 'majority'
                state2 = 'majority'

            questions.append([_question, Option1, state1, Option1_percentage, Option2, state2, Option2_percentage, No_of_votes])

        return render(request, 'accounts/profile.html', {'questions': questions})
    #add redirect to sign up page

def ask(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = AskQuestionForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                question = post.question.replace(' ', '')
                question = question.replace('/', '')
                question = question.replace('?', '')
                post.link = question
                post.save()
                #form.save()
                return redirect('/../accounts/profile/')

        else:
            form = AskQuestionForm()
        return render(request, 'accounts/ask.html', {'form':form})
    else:
        return redirect("../")

def get_question(request, username, question, oneortwo = None):
    if request.method == 'POST':
        u = request.session['u']
        q = request.session['q']
        print('u: ' + u)
        print('q: ' + q)
        print(username)
        print(question)
        print(oneortwo)


        u = User.objects.get(username=u)
        list_of_user_questions = Question.objects.filter(author=u)
        for _question in list_of_user_questions:
            #print(_question)
            if _question.link == question:
                print('QUESTION FOUND FOR LOOP POST get_question')
                q = _question
                break

        if oneortwo == "one":
            print('one')
            q.no_of_votes += 1
            q.option1_votes += 1

        elif oneortwo == "two":
            q.no_of_votes += 1

        elif oneortwo is None:
            print('ELSE @@')

        q.save()
        Option1_percentage = (q.option1_votes / q.no_of_votes) * 100
        Option2_percentage = 100 - Option1_percentage

        if Option1_percentage > Option2_percentage:
            state1 = 'majority'
            state2 = 'minority'
        elif Option1_percentage < Option2_percentage:
            state1 = 'minority'
            state2 = 'majority'
        else:
            state1 = 'majority'
            state2 = 'majority'

        request.session['q'] = ''
        request.session['u'] = ''
        return render(request, "accounts/results.html", {'question': [q.question, q.option1, state1, Option1_percentage, q.option2, state2, Option2_percentage]})
    else:
        try:
            u = User.objects.get(username=username)
            print('got user')
            print(u)
        except:
            print("except username")

        try:
            list_of_user_questions = Question.objects.filter(author=u)
            for _question in list_of_user_questions:
                print(_question)
                if _question.link == question:
                    print(_question)
                    q = _question
                    print('found q: ' + q)
                    break
        except:
            print("except question")

        form_question = q.question
        option1 = q.option1
        option2 = q.option2

        request.session['u'] = u.username
        request.session['q'] = q.question

        return render(request, 'accounts/answer.html', {'question': [form_question, option1, option2, q.link]})
