from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "ideas/home.html")

def create_view(request):
    return render(request, "ideas/create.html")

def update_view(request, slug):
    print(slug)
    return render(request, "ideas/update.html")