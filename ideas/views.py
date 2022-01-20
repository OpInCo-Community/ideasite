from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ideas.forms import IdeaForm
from ideas.models import Idea, Like
from django.db.models import F

from ideas.filters import IdeaFilter
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required()
def like(request, idea_pk):
    idea = get_object_or_404(Idea, pk=idea_pk)
    try:
        like = Like.objects.get(user=request.user, idea=idea)
        like.delete()
        if(idea.likes > 0):
            idea.likes = idea.likes - 1
        idea.save()
        messages.add_message(request, messages.INFO, 'You disliked the idea')
    except:
        Like.objects.create(user=request.user, idea=idea)
        idea.likes = idea.likes + 1
        idea.save()
        messages.add_message(request, messages.INFO, 'You liked the idea')

    return redirect("ideas:home")

@login_required()
def home(request):
    ideaform = IdeaForm()
    ideas = Idea.objects.order_by("-likes", '-created_on')

    all_likes_by_user = Like.objects.filter(user=request.user)
    likes_array = []
    for like in all_likes_by_user:
        likes_array.append(like.idea.pk)



    f = IdeaFilter(request.GET, queryset=ideas)
    if request.method == "POST":
        ideaform = IdeaForm(request.POST)

        if ideaform.is_valid():

            idea = ideaform.save(commit=False)
            idea.author = request.user
            idea.save()
            messages.add_message(request, messages.SUCCESS, 'New Idea Posted')
            return redirect("ideas:home")
        else:
            messages.add_message(request, messages.ERROR, 'There was a problem while posting idea')


    return render(request, "ideas/home.html", { 'ideaform': ideaform, "ideas": ideas, "filter": f, "likes_array": likes_array })

# def create_view(request):
#
#     return render(request, "ideas/create.html")
#
# def detail_view(request, slug):
#     print(slug)
#     return render(request, "ideas/detail.html")