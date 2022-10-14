from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.
def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('reviews:index')

    else:
        form = ReviewForm()

    return render(request, 'reviews/create.html', {'form': form})


def index(request):
    users = Review.objects.all().order_by('id')

    return render(request, "reviews/index.html", {'users': users})


def detail(request, user_id):
    review = Review.objects.get(id=user_id)

    return render(request, "reviews/detail.html", {'review': review})


def update(request):
    pass


def delete(request):
    pass