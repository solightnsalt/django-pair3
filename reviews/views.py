from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "reviews/index.html")

def create(request):
    pass


def update(request):
    pass


def delete(request):
    pass