from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ideas.forms import IdeaForm
from ideas.models import Idea
from ideas.filters import IdeaFilter
# Create your views here.
@login_required()
def home(request):
    ideaform = IdeaForm()
    ideas = Idea.objects.order_by('-created_on')
    f = IdeaFilter(request.GET, queryset=ideas)
    if request.method == "POST":
        ideaform = IdeaForm(request.POST)

        if ideaform.is_valid():
            print(ideaform.cleaned_data)
            idea = ideaform.save(commit=False)
            idea.author = request.user
            idea.save()
            messages.add_message(request, messages.SUCCESS, 'New Idea Posted')
            return redirect("ideas:home")
        else:
            messages.add_message(request, messages.ERROR, 'There was a problem while posting idea')


    return render(request, "ideas/home.html", { 'ideaform': ideaform, "ideas": ideas, "filter": f })

# def create_view(request):
#
#     return render(request, "ideas/create.html")
#
# def detail_view(request, slug):
#     print(slug)
#     return render(request, "ideas/detail.html")